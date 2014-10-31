import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class GetUserInput(BoxLayout):
    def __init__(self, **kwargs):
        super(GetUserInput, self).__init__(**kwargs)
        # layout = BoxLayout(orientation='vertical')
        # btn1 = Button(text='Hello')
        # btn2 = Button(text='World')
        # layout.add_widget(btn1)
        # layout.add_widget(btn2)
        self.orientation = 'vertical'
        self.size_hint = (1.0, None)
        self.height = 30
        self.add_widget(Label(text='On a scale of 1 to 5 how would you rate the service_rating?'))
        self.service_rating = TextInput(multiline=False)
        self.add_widget(self.service_rating)
        self.add_widget(Label(text='On a scale of 1 to 5 how would you rate the food?'))
        self.food_rating = TextInput(multiline=False)
        self.add_widget(self.food_rating)
        self.add_widget(Button(text='Submit'))

class RestaurantMate(App):
    def build(self):
        return GetUserInput()


if __name__ == '__main__':
    RestaurantMate().run()
