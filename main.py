import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class GetUserInput(GridLayout):
    def __init__(self, **kwargs):
        super(GetUserInput, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='On a scale of 1 to 5 how would you rate the service_rating?'))
        self.service_rating = TextInput(multiline=False)
        self.add_widget(self.service_rating)
        self.add_widget(Label(text='On a scale of 1 to 5 how would you rate the food?'))
        self.food_rating = TextInput(multiline=False)
        self.add_widget(self.food_rating)

class RestaurantMate(App):
    def build(self):
        return GetUserInput()


if __name__ == '__main__':
    RestaurantMate().run()