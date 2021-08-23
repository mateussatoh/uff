entriesNumber = int(input())

def caesarCipherDecoder(message, shift):
    messageCharList = [ord(char)-shift for char in message]
    messageString = ""
    for asciiNumber in messageCharList:
        if(asciiNumber < 65):
            messageString += chr(91-(65-asciiNumber))
        else:
            messageString += chr(asciiNumber)
    print(messageString)
    

for entry in range(entriesNumber):
    message = str(input())
    shift = int(input())
    caesarCipherDecoder(message, shift)
