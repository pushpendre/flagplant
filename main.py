"""
# Widget > Layout > UXWidget

The TabbedPanel widget manages different widgets in tabs,
  with a header area for the actual tab buttons and a content
  area for showing the current tab content.

BoxLayout arranges children in a vertical or horizontal box

"""
import os, time
from os.path import dirname, join
os.environ['PASSLIB_MAX_PASSWORD_SIZE'] = str(2 * (1024 ** 3)) # 2GB
import typing as PT

from passlib.hash import pbkdf2_sha512

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

class MainLayout(BoxLayout):
    fchash_text = StringProperty()
    # TODO: allow user to customize the salt based on their email-address/username.
    # binary encode their ascii input to create the salt bytes.
    hasher = pbkdf2_sha512.using(rounds=1600, salt_size=10)

    def on_file_select(self, fc: FileChooser, filenames: PT.List[str]):
        assert len(filenames) == 1
        fn = filenames[0]
        h = self.hasher.hash(open(fn, 'rb').read())
        # print(fn, h)
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

class MainApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    app = MainApp()
    app.run()
