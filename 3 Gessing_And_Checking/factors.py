def factors(number):
    factorList = []
    for i in range(1,number+1):
        if number%i == 0:
            factorList.append(i)
    return factorList

print(factors(120))


