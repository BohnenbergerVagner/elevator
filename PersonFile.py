import random


class Person:
    population = 0

    def __init__(self, floors):
        self.animation = None
        Person.population += 1

        self.start_floor = random.randint(0, floors)
        self.target_floor = random.randint(0, floors)
        while self.start_floor == self.target_floor:
            self.target_floor = random.randint(0, floors)
        self.direction = ('up' if self.start_floor < self.target_floor else 'down')

        self.finished = False

    def arrived(self, floor):
        return True if floor == self.target_floor else False