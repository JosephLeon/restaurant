import kivy
kivy.require('1.9.0')
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window


# Filters input value to be 1-5 and only one char long.
class OneToFiveInput(TextInput):
    pat = re.compile('[^1-5]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = re.sub(pat, '', substring)
        s = s[:1 - len(self.text)]
        return super(OneToFiveInput, self).insert_text(s, from_undo=from_undo)


# Filters input value to be a float.
class FloatInput(TextInput):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class RestaurantMate(App):
    def build(self):
        global starting_tip
        starting_tip = 10

        # Layout.
        Window.clearcolor = (1, 1, 1, 1)
        controls = AnchorLayout(
            anchor_x='right',
            anchor_y='top',
        )
        box = BoxLayout(
            orientation='vertical',
            padding=10,
        )

        # Title.
        apptitle = Label(
            text='Restaurant Mate',
            font_size=20,
            shorten=True,
            halign='left',
            strip=True,
            color=[0, 0, 0, 1],
        )

        # Service label and input.
        service_rating_label = Label(
            text='On a scale of 1 to 5 how would you rate the service?',
            font_size=18,
            color=[0, 0, 0, 1],
        )
        service_rating = OneToFiveInput(
            font_size=18,
            multiline=False,
            input_type='number',
            hint_text='Enter a number 1 through 5',
        )

        # Food label and input.
        food_rating_label = Label(
            text='On a scale of 1 to 5 how would you rate the food?',
            font_size=18,
            color=[0, 0, 0, 1],
        )
        food_rating = OneToFiveInput(
            font_size=18,
            multiline=False,
            input_type='number',
            hint_text='Enter a number 1 through 5',
        )

        # Food/Meal cost label and input.
        food_cost_label = Label(
            text='How much did the meal cost?',
            font_size=18,
            color=[0, 0, 0, 1],
        )
        food_cost = FloatInput(
            font_size=18,
            hint_text='Enter cost of meal without "$"',
        )

        # Calc button.
        input_btn = Button(
            text='Calculate Tip',
            font_size=20,
            size_hint_x=None,
            width=200,
            background_color=[0, 1.7, 0, 1]
        )

        # Adjust the starting_tip value.
        def adjust_tip(rating):
            global starting_tip
            if rating == 1:
                starting_tip = starting_tip - 5
            elif rating == 2:
                starting_tip = starting_tip - 2.5
            elif rating == 3:
                starting_tip = starting_tip + 2.5
            elif rating == 4:
                starting_tip = starting_tip + 3.5
            else:
                starting_tip = starting_tip + 5
            return starting_tip

        # Calculate the tip and tip percentage.
        def calculate_tip(instance):
            service_rating_value = float(service_rating.text)
            food_rating_value = float(food_rating.text)
            adjust_tip(service_rating_value)
            adjust_tip(food_rating_value)

            meal_cost = float(food_cost.text)
            tip = meal_cost * (starting_tip/100)
            format_tip = "${:.2f}".format(tip)
            popup = Popup(
                title='Suggested Tip',
                content=Label(
                    text='Your suggested tip is\n ' + str(starting_tip) + '%\n' + 'Which is ' + str(format_tip),
                    multiline=True,
                ),
                size_hint=(None, None),
                size=(300, 200),
                font_size=18,
            )
            popup.open()

        input_btn.bind(on_press=calculate_tip)

        # Render the objects.
        controls.add_widget(box)
        box.add_widget(apptitle)
        box.add_widget(service_rating_label)
        box.add_widget(service_rating)
        box.add_widget(food_rating_label)
        box.add_widget(food_rating)
        box.add_widget(food_cost_label)
        box.add_widget(food_cost)
        box.add_widget(input_btn)

        return controls

if __name__ == '__main__':
    RestaurantMate().run()
