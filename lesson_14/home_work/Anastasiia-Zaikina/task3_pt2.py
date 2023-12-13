from task3 import Animal


class Cow(Animal):
    def print_animal_sound(self):
        print('Muu')

if __name__ == '__main__':
    cow = Cow()
