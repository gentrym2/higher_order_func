age = [3, 21, 16, 32, 57, 9, 44, 68]


def drinking_age(x):
    if x >= 21:
        return "can drink"
    else:
        return "cannot drink"


can_drink = map(drinking_age, age)

for x in can_drink:
    print(x)









