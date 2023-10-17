from collections import namedtuple, OrderedDict, Counter, deque, defaultdict

# namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])
point = Point(1, 2, 3)
print(point)
print(point.x, point.y, point.z, sep=' ,')
point1 = Point(y=4, x=1, z=3)
print(point1)
# Value cannot be set after instance creation
# point.x = 4
print(point)

# Ordered dictionary
print()
print("_" * 50)
print()
a_dict = {}
a_dict['a'] = 1
a_dict['c'] = 3
a_dict['b'] = 2

print(a_dict)
a_dict['d'] = 4
print(a_dict)
a_dict.popitem()
print(a_dict)


o_dict = OrderedDict({'a': 1, 'c': 3, 'b': 2})
print(o_dict)
o_dict.move_to_end('c')
print(o_dict)
o_dict['d'] = 4
print(o_dict)
o_dict.move_to_end('d', last=False)
print(o_dict)
o_dict.popitem()
print(o_dict)
o_dict.popitem(False)
print(o_dict)


# Counter
print()
print("_" * 50)
print()

c = Counter('collections'[::-1])
print(c)
print(f"The word 'cheese' contains e letter {c['e']} times")
print(c.most_common(2))

# deque
print()
print("_" * 50)
print()

d = deque('abcdefg')
print(d)
print("popped element", d.pop())
print(d)
print("popped left element", d.popleft())
print(d)
d.append('g')
print(d)
d.appendleft('a')
print(d)

d.rotate(-3)
print(d)

# defaultdict
print()
print("_" * 50)
print()


i_dict = {'a': 1, 'b': 2, 'c': 3}

print(i_dict.get('d'))
print(i_dict.get('d', 'default'))

defaulted = defaultdict(float)

print(defaulted['one'])
defaulted['one'] = 1
defaulted['two'] = 2
defaulted['four'] = '4'
print(defaulted)
print('one', defaulted['one'])
print('three', defaulted['three'])


