name = input()
baseSalary = float(input())
totalSales = float(input())

def totalSalary(baseSalary, totalSales):
    return baseSalary + (totalSales * 0.15)

print("TOTAL = R$ %.2f" % (totalSalary(baseSalary, totalSales)) ) 