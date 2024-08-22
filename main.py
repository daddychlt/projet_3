from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: 'vertical'
    MDTopAppBar:
        title: 'My KivyMD App'
    MDLabel:
        text: 'Hello, KivyMD!'
        halign: 'center'
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyApp().run()