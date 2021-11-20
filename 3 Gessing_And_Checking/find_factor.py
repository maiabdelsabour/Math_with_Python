"""EXERCISE 3­1: FINDING THE FACTOR
The factors()function could come in handy for finding the greatest common
factor (GCF) of two numbers. Write a function that will return the GCF of two
numbers,> gcf(150,138)=6"""

def factors(number):
    factorList = []
    for i in range(1,number+1):
        if number%i == 0:
            factorList.append(i)
    return factorList


def GCF(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        firstNumber,secondNumber = secondNumber,firstNumber
    for i in range (firstNumber, 0, -1):
        if firstNumber%i == 0 and secondNumber%i == 0:
            return i


print(GCF(150,138))
print(factors(150))
print(factors(138))



