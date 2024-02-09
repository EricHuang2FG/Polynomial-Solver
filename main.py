import math

def getDegree():
    while True:
        try:
            print("Degree: ", end = "")
            degree = int(input())
            return degree
        except Exception:
            print("Must be an integer")
            continue

def getPolynomial():
    loop = True
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    degree = getDegree()
    coefficients = []
    for i in range(degree, -1, -1):
        while True:
            try:
                print(f"Enter the coefficient of the degree {i}: ", end = "")
                coefficient = int(input())
                break
            except Exception:
                print("Must be an integer")
                continue
        coefficients.append(coefficient)
    for prime in primeList:
        loop = True
        while loop:
            for coefficient in coefficients:
                if coefficient % prime != 0:
                    loop = False
                    break
            else:
                coefficients = [int(i / prime) for i in coefficients]
    return coefficients

def getFactors(num):
    num = abs(num)
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    factors.sort()
    return factors

def possibleZeros(leadingCo, constant):
    possibleZeros = []
    factLeadingCo = getFactors(leadingCo)
    factConstant = getFactors(constant)
    for m in factLeadingCo:
        for n in factConstant:
            possibleZeros.append(n / m)
            possibleZeros.append(-n / m)
    return possibleZeros

def f(x, coefficients):
    return sum(value * x ** (len(coefficients) - 1 - index) for index, value in enumerate(coefficients))

def solvePolynomial():
    solutions = []
    coefficients = getPolynomial()
    degree = len(coefficients) - 1
    while coefficients[-1] == 0:
        coefficients.pop()
        if 0 not in solutions: solutions.append(0)
    testCases = possibleZeros(coefficients[0], coefficients[len(coefficients) - 1])
    testCases = list(set(testCases))
    for case in testCases:
        if f(case, coefficients) == 0.0: solutions.append(case)
        if len(solutions) == degree: return solutions
    return solutions

def printSolutions():
    solutions = list(set(solvePolynomial()))
    result = "The real, rational solutions are: "
    if len(solutions) != 0:
        solutions.sort()
        for solution in solutions:
            result += str(solution) + ", "
        result = result[:len(result) - 2]
    else:
        result += "None"
    print(result)

def main():
    printSolutions()

if __name__ == "__main__":
    main()