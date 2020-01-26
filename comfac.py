factors1 = []
factors2 = []
com_factors = []

def find_factors(num,factors):
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def compare_factors(fac1,fac2,cf):
    for i in fac1:
        for a in fac2:
            if i == a:
                cf.append(i)
    return cf

def ask(question):
    while True:
        inp = input(question)
        try:
            inp = int(inp)
            if int(inp) >= 100000: #One hundred thousand
                print ("This is not a valid input, please write a lower value")
            elif int(inp) <= 0:
                print ("This is not a valid input, please write a higher value")
            else:
                break
        except ValueError:
            print ("This is not a valid input, please write an integer")
    return inp

num1 = ask(("What is your first number? "))
num2 = ask(("What is your second number? "))
find_factors(num1,factors1)
find_factors(num2,factors2)
compare_factors(factors1,factors2,com_factors)
commonfactors = ', '.join(str(i) for i in com_factors)
print ('The common factors of ' + str(num1) + ' and ' + str(num2) + ' are ' + commonfactors)