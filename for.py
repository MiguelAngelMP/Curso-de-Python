for i in range(5):
    print(i)

for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i ** 2)


for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 22:
        break

r = 'ferrocarril'

for letter in r:
    print(letter)
