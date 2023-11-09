def repeat(num_repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_repeats):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat(3)
def greet(name):
    return f'Hello, {name}!'

result = greet('John')
print(result)