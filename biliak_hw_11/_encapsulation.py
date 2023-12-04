# Створити клас з 2 змінними (_a and __a), Створити об'єкт класу та показати ' \
# доступ до цих змінних. (Очікувано отримаємо помилку при доступі до __а)


class Alphabet:

    _a = 1
    __a = 2

alphabet = Alphabet()
print(alphabet._a)
print(alphabet.__a) # AttributeError: 'Alphabet' object has no attribute '__a'.
                    # Did you mean: '_a'?

