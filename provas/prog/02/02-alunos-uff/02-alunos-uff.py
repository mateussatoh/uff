fileName = input()
minMaxEfficiency = input().split()
minMaxHours = input().split()
def registration(line):
  with open(f'{line}.txt', "r") as file:
    lines = file.readlines()
    efficiency = 0
    totalHours = 0
    validHours = 0
    for index, line in enumerate(lines):
      if index > 1:
        data = line.strip("\n").split('#')
        hours = int(data[-2:][0])
        grades = float(data[-2:][1])
        if(grades >= 6):
          validHours += hours
        efficiency += hours * grades
        totalHours += hours
      elif(index == 1):
        name = line.strip('\n')
      else:
        course = line.strip('\n')
  efficiencyCoef = efficiency / totalHours
  file.close()
  return [name, course, validHours, efficiencyCoef]
with open(f'{fileName}.txt', "r") as file:
  lines = file.readlines()
  for line in lines:
    studentData = registration(line.strip("\n"))
    if(int(minMaxHours[0]) < studentData[2] < int(minMaxHours[1]) and float(minMaxEfficiency[0]) < studentData[3] < float(minMaxEfficiency[1])):
        print(f'Nome:{studentData[0]} \nCurso:{studentData[1]} \nCarga Horária Efetiva: {studentData[2]} \nCoeficiente de Rendimento: {studentData[3]:.2f}\n')
file.close()