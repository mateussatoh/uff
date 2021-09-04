entriesNumber = int(input())

password = ''
passwordList = []

for entry in range(entriesNumber):
   passphrase = input().split()
   for word in passphrase:
      password += word[0]
   passwordList.append(password)
   password = ''

for password in passwordList:
   print(password)
