#!/usr/bin/python3

def same_number_with_zero_to_nine(name):
    for n in range(10):
        for i in range(1, 11):
            all_zero = ''
            for j in range(i):
                all_zero += str(n)
            print(name + all_zero)

def zero_to_ten_number_with_zero_to_nine(name):
    for i in range(1, 12):
        all_zero = ''
        for j in range(i):
            all_zero += str(j)
        print(name + all_zero)

def one_to_ten_number_with_zero_to_nine(name):
    for i in range(2, 12):
        all_zero = ''
        for j in range(1, i):
            all_zero += str(j)
        print(name + all_zero)


# same_number_with_zero_to_nine('Test')
# zero_to_ten_number_with_zero_to_nine('Test')
# one_to_ten_number_with_zero_to_nine('Test')