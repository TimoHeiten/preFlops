import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout as pL
from kivy.uix.stacklayout import StackLayout

import preflop_layout as layouts
import img_locator as imgs

from kivy.uix.screenmanager import ScreenManager, Screen

class PreFlopScreenManger(ScreenManager):
    pass

class MainPage(Screen):
    
    def __init__(self, sm):
        super(MainPage, self).__init__()
        self.sm = sm
        self.name = 'main'
        box = BoxLayout(orientation="vertical")
        for p in imgs.all_flops:
            display = DisplayPreFlopBtns(self.sm, p)
            btn = Button(text=p.name)
            temp = p.name
            btn.on_release = lambda i=temp: self.set_to_disply(i)
            box.add_widget(btn)
        self.add_widget(box)
        self.sm.add_widget(self)

    def set_to_disply(self, display_name):
        self.sm.current = display_name



# buttons for all possible images
class DisplayPreFlopBtns(Screen):
    
    def __init__(self, sm, associated_preFlop):
        super(DisplayPreFlopBtns, self).__init__()
        self.name = associated_preFlop.name
        self.sm = sm
        sm.add_widget(self)

        box = BoxLayout(orientation="vertical")
        for img, path in list(associated_preFlop):
            flop = FlopDisplay(self.sm, img, path)
            btn_to_flop = Button(text=img)
            temp_flop = img
            btn_to_flop.on_release = lambda i=img: self.set_to_flop(i)
            box.add_widget(btn_to_flop)

        self.add_widget(box)

    def set_to_flop(self, name):
        self.sm.current = name



# actual image
class FlopDisplay(Screen):

    def __init__(self, sm, name, path):
        super(FlopDisplay, self).__init__()
        self.name = name
        self.path = path
        self.sm = sm
        sm.add_widget(self)

        box = BoxLayout(orientation='vertical')
        button = Button(text='back', size_hint=(0.75, 0.25), on_release=self.set_main)
        img = Image(source=self.path)
        box.add_widget(button)
        box.add_widget(img)
        self.add_widget(box)

    def set_main(self, x):
        self.sm.current = 'main'


root_widget = Builder.load_file("./kvs/master.kv")
class Main3(App):

    def __init__(self, sm):
        self.sm = sm
        super(Main3, self).__init__()

    def build(self):
        main = MainPage(self.sm)
        root_widget.current = 'main'
        return root_widget

    def set_to_display(self, name):
        self.sm.current = name


Main3(root_widget).run()


# use stack for img buttons
