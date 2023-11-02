#Ex_2
from collections import namedtuple
Fish = namedtuple('Fish', ['name', 'species', 'tank'])
fish_1 = Fish(name='Shark', species='Predator', tank='Ocean')
fish_2 = Fish(name='Tuna', species='Predator', tank='Ocean')
fish_3 = Fish(name='Carp', species='Omnivorous', tank='Rievers or lakes')


selected_fish = fish_1
fish_dict = selected_fish._asdict()
print(fish_dict)

#Ex_3

from collections import defaultdict, namedtuple
Fish = namedtuple('Fish', ['name', 'species', 'tank'])
fish_defaultdict = defaultdict(Fish)
fish_defaultdict['Shark'] = Fish('Shark', 'Predator', 'Ocean')
fish_defaultdict['Tuna'] = Fish('Tuna', 'Predator', 'Ocean')
fish_defaultdict['Carp'] = Fish('Carp', 'Omnivorous', 'Rievers or lakes')

Shark = fish_defaultdict['Shark']
Tuna = fish_defaultdict['Tuna']
Carp = fish_defaultdict['Carp']

print(Shark)
print(Tuna)
print(Carp)