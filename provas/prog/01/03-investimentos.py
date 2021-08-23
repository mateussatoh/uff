totalOptions = []
totalPeriods = []

def greaterInterest(periodA, periodB, totalOptions):
    monthA, monthB = (int(periodA) - 1), int(periodB) 
    betterOption = '' 
    biggerInterest = 0
    for option in totalOptions:
        meanInterest = 0.0
        name = option[0]
        rates = option[1]
        periodOptions = rates[monthA:monthB]
        for interest in periodOptions:
            meanInterest += float(interest)
        meanInterest = meanInterest/((monthB - monthA))
        if(meanInterest > biggerInterest):
            biggerInterest = meanInterest 
            betterOption = name
    print(f'Entre os meses {monthA + 1} e {monthB}, a melhor aplicação foi: {betterOption}')
    print(f'Com maior percentual mesal médio no período de: {round(biggerInterest,3)} \n')
    return None

    
def compute(totalOptions, totalPeriods):
    for period in totalPeriods:
        greaterInterest(period[0], period[1], totalOptions)
    return None

def addPeriod(totalPeriods):
    line = input()
    if line != "Fim dos Períodos":
        period = line.split(" ")
        totalPeriods.append(period)
        addPeriod(totalPeriods)
    else:
        compute(totalOptions, totalPeriods)
    return None


def addOption(totalOptions):
    line = input()
    if line != "Fim das Opções":
        investimentName = line.split('#')[0]
        investimentInterest = line.split('#')[1].split(" ")
        investiment = [investimentName, investimentInterest]
        totalOptions.append(investiment)
        addOption(totalOptions)
    else:
        addPeriod(totalPeriods)
    return None
    
addOption(totalOptions)
