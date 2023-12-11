"""Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію.
Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи."""


class Vehicle:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def desc(self):
        print(self.color, self.model)

    def wheels(self):
        print(4)
