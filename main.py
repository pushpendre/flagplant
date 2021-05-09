"""
# Widget > Layout > UXWidget

The TabbedPanel widget manages different widgets in tabs,
  with a header area for the actual tab buttons and a content
  area for showing the current tab content.

BoxLayout arranges children in a vertical or horizontal box

"""
import os, time, re
from os.path import dirname, join
os.environ['PASSLIB_MAX_PASSWORD_SIZE'] = str(2 * (1024 ** 3)) # 2GB
import typing as PT

from passlib.hash import pbkdf2_sha512
from passlib.utils.binary import ab64_decode, ab64_encode

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.layout import Layout
from kivy.uix.filechooser import FileChooser
from kivy.properties import StringProperty, BooleanProperty
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.READ_EXTERNAL_STORAGE,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.CAMERA,
        # Permission.INTERNET,
    ])

def cleanup(s):
    """ Length must be divisible by 4
    [a-zA-Z0-9.]*

    https://tools.ietf.org/html/rfc3548.html#page-4
    """
    s = re.sub('[^0-9a-zA-Z.]', '.', s)
    m = len(s) % 4
    s = s + ('.'*(4 - m) if m else '')
    return s


class MainLayout(BoxLayout):
    fchash_text = StringProperty()
    username_transformed = StringProperty()

    def on_file_select(self, fc: FileChooser, filenames: PT.List[str]):
        assert len(filenames) == 1
        fn = filenames[0]
        ut = self.username_transformed
        custom_salt = ab64_decode(cleanup(ut)) if ut else None
        hasher = (pbkdf2_sha512.using(salt=custom_salt, rounds=1600)
                  if custom_salt
                  else pbkdf2_sha512.using(rounds=1600, salt_size=10))
        try:
            h = hasher.hash(open(fn, 'rb').read())
        except:
            h = 'Unable to open!'
        try:
            self.fchash_text = os.path.basename(fn) + '\n\n' + h
        except Exception as exception:
            print(exception)
        return

    def camera_picture_capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        fn = "IMG_{}.png".format(timestr)
        camera.export_to_png(fn)
        print("Captured " + fn)

    def username_textinput_callback(self, text):
        self.username_transformed = cleanup(text)
        return

class MainApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    app = MainApp()
    app.run()
