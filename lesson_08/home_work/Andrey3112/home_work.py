#######1
from collections import Counter, namedtuple, defaultdict, deque

sequence = "2307452340567347890"


def count_it(sequence):
    digit_counts = Counter(map(int, sequence))
    most_common_digits = digit_counts.most_common(3)
    result_dict = dict(most_common_digits)
    return result_dict


print(count_it(sequence))

#######2
Fish = namedtuple('Fish', ['name', 'species', 'tank'])
fish_1 = Fish(name='andrii', species='akula', tank='okean')
fish_2 = Fish(name='sasha', species='som', tank='rechka')
fish_3 = Fish(name='lesha', species='okun', tank='rechka')
print(fish_1._asdict())

#######3
fish_1 = Fish(name='andrii', species='akula', tank='okean')
defaul_fish = Fish(name='andrii', species='akula', tank='okean')
fish_dict = defaultdict(Fish)

#######4
new = deque("hello world")
new.append("!!!")
new.appendleft("!!!!!")
new.pop()
new.popleft()


#######5   и так же под №6 подходит
def dekorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"summa chisel: {result}")
        return result
    return wrapper


@dekorator
def chisla(a, b):
    return a + b


chisla(3, 5)