from collections import deque
my_deque = deque()
my_deque.appendleft(1)
my_deque.append(2)
print(my_deque)

item_from_start = my_deque.popleft()
item_from_end = my_deque.pop()
print(item_from_start)
print(item_from_end)
print(my_deque)