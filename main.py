# 1

print("welcome to today's session".title())

num=10
print("I love marvel characters {} times more than DC".format(num))


def times_two(num1):
    result = num1 * 2
    return result

for number in range(3): # 0,1,2
    calc_res = times_two(number)
    print(calc_res)

# 2

carrots = int(input('How many carrots do you have?'))
rabbits = 6

if rabbits > carrots:
    print('There are not enough carrots')
elif rabbits < carrots:
    print('There are too many carrots')
else:
    print('You have the right number of carrots')
