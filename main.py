import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup


class Test:
  print 'test worked'


class CapitalInput(TextInput):

    def insert_text(self, substring, from_undo=False):
        s = substring.upper()
        return super(CapitalInput, self).insert_text(s,\
        from_undo=from_undo)


class RestaurantMate(App):
    def build(self):
        global starting_tip
        starting_tip = 10

        controls = AnchorLayout(
            anchor_x='right',
            anchor_y='top',
        )
        box = BoxLayout(
            orientation='vertical'
        )

        service_rating_label = Label(
            text='On a scale of 1 to 5 how would you rate the service?',
            font_size=18,
        )

        def on_text(instance, value):
            global length_value
            length_value = len(value)
            return length_value

        def one_to_five(value, is_undo):
            # if '1' <= value <= '5' and length_value < 1:
            if '1' <= value <= '5':
                return value
            return ''

        service_rating = TextInput(
            font_size=18,
            multiline=False,
            input_filter=one_to_five,
            input_type='number',
            hint_text='Must be a number 1 through 5',
            hint_text_color=[255, 0, 0, 1],
        )
        food_rating_label = Label(
            text='On a scale of 1 to 5 how would you rate the food?',
            font_size=18,
        )
        food_rating = TextInput(
            font_size=18,
            multiline=False,
            input_filter=one_to_five,
            input_type='number',
            hint_text='Must be a number 1 through 5',
            hint_text_color=[255, 0, 0, 1],
        )
        food_cost_label = Label(
            text='How much did the meal cost?',
            font_size=18,
        )
        food_cost = TextInput(
            font_size=18,
            size_hint_x=None,
            width=200
        )

        service_rating.bind(text=on_text)
        # food_rating.bind(text=on_text)

        input_btn = Button(
            text='Calculate Tip',
            font_size=20,
            size_hint_x=None,
            width=200,
            background_color=[0, 1.7, 0, 1]
        )

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

        ''' Testing classes'''
        Test()

        test = CapitalInput(
            font_size=18,
            multiline=False,
            hint_text='Test',
            hint_text_color=[255, 0, 0, 1],
        )

        controls.add_widget(box)

        ''' Testing classes'''
        box.add_widget(test)
        ''' End Testing classes'''
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
