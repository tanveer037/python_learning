def yes_or_no():
    values = ['yes','no']
    while True:
        for value in values:
            yield value

gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
