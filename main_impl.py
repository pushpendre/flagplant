from kivy.uix.textinput import TextInput
from kivy.utils import platform
from kivy_garden.xcamera import XCamera
from kivy_garden.xcamera.platform_api import LANDSCAPE, PORTRAIT, set_orientation


class CustomTextInput(TextInput):
    def _hide_cut_copy_paste(self, win=None):
        bubble = self._bubble
        if not bubble:
            return

# class XCameraWrapper(XCamera):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self._camera.bind(on_load=self.loaded)

#     def loaded(self, platform_camera):
#         if platform == 'android':
#             from android import mActivity
#             mActivity.setRequestedOrientation(LANDSCAPE)
