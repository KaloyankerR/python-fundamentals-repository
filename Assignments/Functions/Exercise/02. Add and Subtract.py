def add_and_subtract(num1, num2, num3):
    def subtract(num_sum):
        subtract_num = num_sum - num3
        return subtract_num

    def sum_numbers():
        the_sum = num1 + num2
        sum_num = subtract(the_sum)
        return sum_num

    result = sum_numbers()
    return result


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(add_and_subtract(number_1, number_2, number_3))
