fileName = input()
minMaxEfficiency = input().split()
minMaxHours = input().split()

def registration(line, minMaxEfficiency, minMaxHours):
    with open(f"{line}.txt", "r") as file:
        efficiency = 0
        totalHours = 0
        validHours = 0
        course = file.readline().strip("\n")
        name = file.readline().strip("\n")
        data = file.readline().strip("\n").split("#")
        while data != [""]:
            hours = int(data[-2:][0])
            grades = float(data[-2:][1])
            if grades >= 6:
                validHours += hours
            efficiency += hours * grades
            totalHours += hours
            data = file.readline().strip("\n").split("#")
    efficiencyCoef = efficiency / totalHours
    file.close()
    if int(minMaxHours[0]) < validHours < int(minMaxHours[1]) and float(
        minMaxEfficiency[0]
    ) < efficiencyCoef < float(minMaxEfficiency[1]):
        print(
            f"Nome:{name} \nCurso:{course} \nCarga Horária Efetiva: {validHours} \nCoeficiente de Rendimento: {efficiencyCoef:.2f}\n"
        )
    return None


with open(f"{fileName}.txt", "r") as file:
    line = file.readline()
    while line != "":
        studentData = registration(line.strip("\n"), minMaxEfficiency, minMaxHours)
        line = file.readline()
file.close()
