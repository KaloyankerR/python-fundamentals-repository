def pos_or_neg(num_1, num_2, num_3):
    neg_count = 0
    zero_condition = num_1 == 0 or num2 == 0 or num3 == 0

    if zero_condition:
        return 'zero'

    condition1 = num_1 <= 0
    condition2 = num_2 <= 0
    condition3 = num_3 <= 0

    if condition1:
        neg_count += 1
    if condition2:
        neg_count += 1
    if condition3:
        neg_count += 1

    if neg_count == 0:
        return 'positive'
    elif neg_count == 1:
        return 'negative'
    elif neg_count == 2:
        return 'positive'
    elif neg_count == 3:
        return 'negative'


num1 = float(input())
num2 = float(input())
num3 = float(input())
res = pos_or_neg(num1, num2, num3)
print(res)
