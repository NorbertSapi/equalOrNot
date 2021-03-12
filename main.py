# This is an exercise to determine if the sum of two integers is equal to the given value.

# numbers = [5, 7, 1, 2, 8, 4, 3]
# for example
# Target Sum: 10 = 7 + 3; 2 + 8
# Target Sum: 19 = No two values sum up to 19


def find_sum_of_two(x, target_number):
    # iterate through list, first number
    for a in x:
        # iterate through list, second number
        for b in x:
            if b == a:
                continue
            if b == (target_number-a):
                print(target_number, " - ", a, " = ", b)
                return True
    return False


print(find_sum_of_two([5, 7, 1, 2, 8, 4, 3], 12))
print(find_sum_of_two([5, 7, 1, 2, 8, 4, 3], 15))
print(find_sum_of_two([5, 2, 8, 7, 6, 1, 9], 16))
print(find_sum_of_two([5, 2, 8, 7, 6, 1, 9], 19))
