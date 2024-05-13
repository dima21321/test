from random import choice


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.auto = None
#     def get_auto(self, brand, year):
#         if self.age >= 18:
#             self.auto = Auto(brand=brand, year=year)
#
# class Auto:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
# h = Human("Oleg", 19)
# h.get_auto(brand="Opel", year=2020)
# print(h.auto.brand)
# print(h.auto.year)






class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 20


    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(auto)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()

        self.job = Job(option_work)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return #зупинка роботи
        self.satiety += 5
        self.home.food -= 5


    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness += self.job.gladness


    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 50
            self.car.fuel = 100
        elif manage == "food":
            print("I bought food")
            self.money -= 20
            self.home.food += 20
        elif manage == "delicacies":
            print("I`m happy!")
            self.money -= 10
            self.gladness += 20
            self.satiety += 2
    def days_indexes(self, day): # -----Day 1------
        day = f"Today the {day} of {self.name}`s life"
        print(f"{day:-^50}")
        indexes_name = f"{self.name}`s indexes"
        print(f"{indexes_name:-^50}")

    def chill(self): #homework
        self.gladness += 10
        self.money -= 5

    def to_repair(self): #homework
        self.money -= 200

    def clean_home(self): #homework
        self.gladness -= 6





class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Auto:
    def __init__(self, auto):
        self.brand = choice(list(auto))
        self.fuel = auto[self.brand]["fuel"]
        self.strength = auto[self.brand]["strength"]
        self.consumption = auto[self.brand]["consumption"]


    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The Car can`t move")
            return False


class Job:
    def __init__(self, option_work):
        self.work = choice(list(option_work))
        self.salary = option_work[self.work]['salary']
        self.gladness = option_work[self.work]['gladness']



option_work = {"Developer C++": {"salary": 50, 'gladness': 10},
               "Developer Python": {"salary": 40, 'gladness': 20},}

auto = {"BMW": {"fuel": 50, "strength": 100, "consumption": 18},
        "OPEL":{"fuel": 30, "strength": 60, "consumption": 12},
        "FORD":{"fuel": 35, "strength": 80, "consumption": 10}}

nick = Human(name="Ivan")


