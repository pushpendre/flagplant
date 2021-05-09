from kivy.uix.textinput import TextInput

class CustomTextInput(TextInput):
    def _hide_cut_copy_paste(self, win=None):
        bubble = self._bubble
        if not bubble:
            return
