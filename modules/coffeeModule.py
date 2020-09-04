 
#You can import any required modules here
from coffeecontrol import BrewCoffee
from twitter import Twitter
import time

moduleName = "coffeeModule"
#All of the words must be heard in order for this module to be executed
commandWords = ["make","coffee"]

def execute(command):
    print("Gathering Twitter Vote")
    twit=Twitter()
    coffee_choice=twit.getVote()
    brew=BrewCoffee(coffee_choice)
    brew.displayCoffeeChoice(coffee_choice)
    #brew.startHotWater()
    #brew.pourBean()
    #brew.waitToBoil
    #brew.pourWater()
    #brew.mix()
    #brew.steep()
    return