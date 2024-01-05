import random
# randint(a,b) returns a random integer between a and b (both inclusive).
random_integer = random.randint(1,20)
print(random_integer)

# random.random()-> returns the next random floating point number between (0.0 to 1.0).
randoms = random.random()
print(randoms)

# random.uniform(a, b) -> Returns a random floating point
random_uniform = random.uniform(10,15)
print(random_uniform)

# random.expovariate(lambda) -> Returns a number corresponding to an exponential distribution.
print('Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))
