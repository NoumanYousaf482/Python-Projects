my_num = int(input('Enter a number: '))

power = len(str(my_num))

num = 0
i = my_num

while i > 0:
    reminder = i%10
    num += reminder**power
    i = i //10

if num == my_num:
    print(f'{my_num} is Armstrong')
else:
    print(f'{my_num} is not Armstrong number')