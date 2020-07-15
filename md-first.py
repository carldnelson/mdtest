from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='hellow', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        label = MDLabel(text='hellow workd', halign='center', theme_text_color='Error', font_style='H2')

        screen.add_widget(btn_flat)
        screen.add_widget(label)
        return screen

DemoApp().run()
