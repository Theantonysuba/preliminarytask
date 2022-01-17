

def getSum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

for i in range(10,101):
    sum_of_digits = getSum(i)
    if i%sum_of_digits == 0:
        print(i)

