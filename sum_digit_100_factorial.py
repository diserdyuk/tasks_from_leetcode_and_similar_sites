
''' Find the sum of the digits in the number 100! (i.e. 100 factorial)
{Correct answer: 648} '''



num = int(input('enter nums: '))    # 100

prod = 1
for i in range(num):    # num -> 100, [0,1,2,3,4,5 ... 99]
    prod = prod * (i+1)

sum = 0
for i in str(prod):
    sum = sum + int(i)

print(sum)    # 648




