"""
x = 5 
x = x + 2
length = 12
print(x + length)
"""

"""
name_list = ['Abe','Bob','Chloe','Daphne']
for i, name in enumerate(name_list):
    print(name,"has index", i)
"""


def average(a,b):
    return print((a+b)/2)

average(10,20)


def mySum(number):
    running_sum = 0
    for i in range(1,number+1):
         running_sum += i
    return print(running_sum)
    
mySum(10)

def mySum2(number):
    running_sum = 0
    for i in range(number+1):
        running_sum +=i**2 +1
    return print(running_sum)
mySum2(20)



def sum(numbers):
    running_sum = 0
    for i in numbers:
        running_sum +=i
    return running_sum
print(sum([1, 2, 3, 4, 5]))


def average3(numberList):
    return print(sum(numberList)/len(numberList))
average3([8,11,15])