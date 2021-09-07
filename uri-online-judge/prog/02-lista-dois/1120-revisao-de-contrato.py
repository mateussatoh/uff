def removeGlitchNumber():
    glitchNumber, totalValue = map(str,input().split())
    if (glitchNumber != "0" or totalValue != "0"):
        newString = ""
        totalValueList = list(totalValue)
        for number in totalValueList:
            if(number != glitchNumber):
              newString += number
        if newString == '':
            newString = '0'
        print(int(newString))
        removeGlitchNumber()

removeGlitchNumber()





    
    
