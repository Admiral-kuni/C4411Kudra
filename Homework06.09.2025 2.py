import random

class Dog:
    def __init__(self, name):
        self.name = name
        self.happiness = 0
        self.satiety = 25
        self.alive = True

    def to_go_out(self):
        print("Time to go out")
        self.happiness += 0.12
        self.satiety -= 4

    def to_sleep(self):
        print("Time to sleep")
        self.happiness += 0.14

    def to_eat(self):
        print("Time to eat!")
        self.satiety += 5
        self.happiness -= 0.2

    def is_alive(self):
        if self.happiness <= -0.5:
            print("Depression...")
            self.alive = False
        elif self.satiety <= 0:
            print("Died from hunger")
            self.alive = False

        elif self.happiness > 5:
            print("happy life of a pet")
            self.alive = False

    def end_of_day(self):
        print(f"Satiety = {self.satiety}")
        print(f"Happiness = {round(self.happiness, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" +self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_go_out()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_eat()
        self.end_of_day()
        self.is_alive()

nick = Dog(name="Russel")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
