entriesNumber = int(input())

def getLanguage(languageList):
    prefferedLanguage = languageList[0]
    for language in languageList:
     if(prefferedLanguage != language):
         prefferedLanguage = 'ingles'      
    print(prefferedLanguage)     


for entry in range(entriesNumber):
    friends = int(input())
    languageList = []
    for person in range(friends):
        languageList.append(str(input()))
    getLanguage(languageList)
