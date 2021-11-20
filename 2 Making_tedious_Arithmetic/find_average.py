"""
Find the average of the numbers in the list below:
d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42,
15, 96, 11, 70, 83, 97, 75]
"""
def sum(numbers):
    running_sum = 0
    for i in numbers:
        running_sum +=i
    return running_sum


def average(numberList):
    return print(sum(numberList)/len(numberList))

d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42,
15, 96, 11, 70, 83, 97, 75]
average(d)