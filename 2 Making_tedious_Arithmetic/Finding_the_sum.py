"""
Find the sum of all the numbers from 1 to 100. How about from 1 to 1,000?
See a pattern?
"""

def sum(number):
    running_sum = 0
    for i in range(number+1):
        running_sum +=i
    return print(running_sum)


sum(100)
sum(1000)
