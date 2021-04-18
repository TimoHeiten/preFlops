""" import kivy
kivy.require('1.10.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class MasterButtons:

    def __init__(self, preFlops, screens):
        self.preFlops = preFlops
        self.screens = screens

    def build(self):
        box = kivy.uix.boxlayout.BoxLayout(orientation='vertical')
        for p in self.preFlops:
            btn = Button(text=p.name, size_hint=(1,1.5))
            box.add_widget(btn)
            detail = Detail(p.name, list(p))
            self.screens.add_screen(detail)
            temp = p.name
            btn.on_release = lambda i=temp: self.screens.move_to()

        return box


class Detail(Screen):

    def __init__(self, name, image_names):
        self.name = name
        self.imgs = image_names
        super(Detail, self).__init__()

    def build(self):
        box = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        for i in self.imgs:
            btn = Button(text=i.split(".")[0]) # $img.jpg , get only $img
            temp = i
            box.add_widget(btn)
        return box


class MainPage(Screen):

    def __init__(self, masterButtons, screens):
        self.master_buttons = masterButtons
        self.screens = screens
        self.name = "master-view"
        super(MainPage, self).__init__()

    def build(self):
        '''
        [  back  ] [ master-view ]
        -------------------------- //  below is changed from master to detail view
        [       Cold 4           ]
        [       rfi              ]
        [       etc              ]
        '''
        outer = kivy.uix.boxlayout.BoxLayout(orientation='vertical')
        inner = kivy.uix.boxlayout.BoxLayout(orientation='horizontal')

        back_btn = Button(text="back", size_hint=(1, 0.25))
        root_btn = Button(text="master-view", size_hint=(1, 0.25))
        # root_btn.on_release = sm.switch_to()

        inner.add_widget(back_btn)
        inner.add_widget(root_btn)

        outer.add_widget(inner)
        outer.add_widget(self.master_buttons.build())
        self.screens.add_screen(self)

        return outer """