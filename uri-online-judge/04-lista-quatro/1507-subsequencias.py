def isSubsequence(string, subsequence):
    matches = 0
    index = 0
    for char in string:
        if char == subsequence[index]:
            matches += 1
            index += 1
            if matches == len(subsequence):
                return True  
    return False
    
for i in range(int(input())):
  line = input()
  for j in range(int(input())):
    sub = input()
    if isSubsequence(line, sub):
      print('Yes')
    else:
      print('No')            
