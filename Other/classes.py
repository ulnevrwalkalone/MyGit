# practice excercises for using classes in python

class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_rest(self):
        #prints info about the name and cuisine type of the Restaurant
        print(self.name.title() + " is a(n) " + self.cuisine + ' restaurant')

    def open(self):
        # prints whether the restaurant is open or not
        print(self.name.title() + " is now open.")

rest_1= Restaurant('Pizza Hut','Pizza')

rest_1.open()

rest_2= Restaurant('AAB','Indian')


rest_2.describe_rest()
