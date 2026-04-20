list = input("Enter your numbers:")
numbers = []
for number in list.split(','):
    numbers = [int(number)]
    for even_num in numbers:
        if even_num % 2 == 0:
            print(even_num)
