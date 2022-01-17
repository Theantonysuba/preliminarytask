def getSum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

for i in range(101):
    sum_of_digits = getSum(i)
    if i == sum_of_digits * sum_of_digits:
        print(i)

