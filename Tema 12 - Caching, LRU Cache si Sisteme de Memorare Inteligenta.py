# Exercitiul 1
# Cache LRU pentru conversie temperatura

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):

        if key not in self.cache:
            return None

        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(5)


def celsius_to_fahrenheit(temp):

    rezultat = cache.get(temp)

    if rezultat is not None:
        print("Rezultat din cache")
        return rezultat

    rezultat = temp * 9/5 + 32

    cache.put(temp, rezultat)

    return rezultat


print(celsius_to_fahrenheit(20))
print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit(20))



# Exercitiul 2
# Cache decorator pentru factorial

cache_factorial = {}

def cache_decorator(func):

    def wrapper(n):

        if n in cache_factorial:
            return cache_factorial[n]

        rezultat = func(n)

        cache_factorial[n] = rezultat

        return rezultat

    return wrapper


@cache_decorator
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)


print("Factorial 5:", factorial(5))
print("Factorial 5 din cache:", factorial(5))



# Exercitiul 3
# Sistem simplu de caching pentru API

cache_api = {}

def get_data_api(endpoint):

    if endpoint in cache_api:
        print("Date din cache")
        return cache_api[endpoint]

    print("Simulare request API...")

    data = {
        "user": "Ana",
        "age": 30,
        "city": "Timisoara"
    }

    cache_api[endpoint] = data

    return data


print(get_data_api("/user"))
print(get_data_api("/user"))


