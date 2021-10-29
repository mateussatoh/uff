grades = []

def computeGrades(grades):
  meanGrades = 0
  for grade in grades:
      meanGrades += grade
  meanGrades /=  2
  print(f'media = {meanGrades}')
  return None  

def newEntry():
  grade = float(input())
  if grade > 10 or grade < 0:
    print('nota invalida')
  else:
    grades.append(grade)
  if len(grades) == 2:
    computeGrades(grades)
  else: 
    newEntry()
  return None
    
newEntry()

      


