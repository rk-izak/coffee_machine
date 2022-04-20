import math


class CoM:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        a = input()
        if str(a) == 'back':
            pass
        elif int(a) == 1:
            n_water = math.floor(self.water / 250)
            n_coffee = math.floor(self.coffee / 16)
            n_cups = math.floor(self.cups / 1)
            n_milk = (self.milk / 1)

            not_enough_val = [n_water, n_milk, n_coffee, n_cups]
            not_enough_nam = ['water', 'milk', 'coffee', 'cups']
            index = not_enough_val.index(min(n_water, n_milk, n_coffee, n_cups))
            if min(n_water, n_milk, n_coffee, n_cups) >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1
            else:
                print("Sorry, not enough {}!".format(not_enough_nam[index]))

        elif int(a) == 2:
            n_water = math.floor(self.water / 350)
            n_milk = math.floor(self.milk / 75)
            n_coffee = math.floor(self.coffee / 20)
            n_cups = math.floor(self.cups / 1)

            not_enough_val = [n_water, n_milk, n_coffee, n_cups]
            not_enough_nam = ['water', 'milk', 'coffee', 'cups']
            index = not_enough_val.index(min(n_water, n_milk, n_coffee, n_cups))
            if min(n_water, n_milk, n_coffee, n_cups) >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7
                self.cups -= 1
            else:
                print("Sorry, not enough {}!".format(not_enough_nam[index]))


        elif int(a) == 3:
            n_water = math.floor(self.water / 200)
            n_milk = math.floor(self.milk / 100)
            n_coffee = math.floor(self.coffee / 12)
            n_cups = math.floor(self.cups / 1)

            not_enough_val = [n_water, n_milk, n_coffee, n_cups]
            not_enough_nam = ['water', 'milk', 'coffee', 'cups']
            index = not_enough_val.index(min(n_water, n_milk, n_coffee, n_cups))
            if min(n_water, n_milk, n_coffee, n_cups) >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6
                self.cups -= 1
            else:
                print("Sorry, not enough {}!".format(not_enough_nam[index]))

        return self.water, self.milk, self.coffee, self.cups, self.money

    def fill(self):
        print("Write how many ml of water you want to add: ")
        a = input()
        water_add = int(a)
        self.water += water_add
        print("Write how many ml of milk you want to add: ")
        a = input()
        milk_add = int(a)
        self.milk += milk_add
        print("Write how many grams of coffee beans you want to add: ")
        a = input()
        coffee_add = int(a)
        self.coffee += coffee_add
        print("Write how many disposable cups of coffee you want to add: ")
        a = input()
        cups_add = int(a)
        self.cups += cups_add

        return self.water, self.milk, self.coffee, self.cups

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money -= self.money
        return self.money

    def remain(self):
        print("""\nThe coffee machine has:
{} ml of water
{} ml of milk
{} g of coffee beans
{} disposable cups
${} of money""".format(self.water, self.milk, self.coffee, self.cups, self.money))


machine = CoM()

while True:

    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == 'buy':
        machine.buy()
    elif action == 'fill':
        machine.fill()
    elif action == 'take':
        machine.take()
    elif action == 'remaining':
        machine.remain()
    elif action == 'exit':
        break
