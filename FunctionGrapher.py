def equationFormatter(equation):
    equationArray = list(equation)
    cleanEquationArray = []

    for i in range(len(equationArray)):
        if (equationArray[i] == "^"):
            cleanEquationArray.append("**")
            continue
        if (equationArray[i] == "y" or equationArray[i] == "Y" or equationArray[i] == " " or equationArray[i] == "="):
            continue
        cleanEquationArray.append(equationArray[i])

    equationArray = cleanEquationArray

    equation = "".join(equationArray)
    return equation


def subX(equation, xValue):
    equation = list(equation)
    subString = "(" + str(xValue) + ")"

    for i in range(len(equation)):
        if (equation[i] == "X" or equation[i] == "x"):
            if (i + 1 < len(equation)):
                if (validateMultiplication(equation[i+1])):
                    subString = subString + "*"
            if (i - 1 >= 0):
                if (validateMultiplication(equation[i-1])):
                    subString = "*" + subString
            equation[i] = subString   
    equation = "".join(equation)
    return equation


def validateMultiplication(element):
    if (element.isnumeric() or element == "-"):
        return True
    else:
        return False



def cartesianPlanePrinter(TOV):
    plane = []
    for x in range(-51, 51):
        temp = []
        for y in range(-51, 51):
            temp.append("   ")
        plane.append(temp)

    for i in range(len(plane)):
        for j in range(len(plane[i])):
            if (j == 51):
                plane[i][j] = " | "

    xAxisCount = -50
    for i in range(len(plane[50])):
        plane[50][i] = "---"
        if (i != 0):
            if (len(str(xAxisCount)) == 1):
                plane[101][i] = " " + str(xAxisCount) + " "
            elif (len(str(xAxisCount)) == 2):
                plane[101][i] = str(xAxisCount) + " "
            elif (len(str(xAxisCount)) == 3):
                plane[101][i] = str(xAxisCount)
            xAxisCount += 1

    yAxisCount = -50
    for i in range(101):
        for j in range(len(plane[i])):
            if (j == 0):
                if (len(str(yAxisCount)) == 1):
                    plane[i][j] = " " + str(yAxisCount) + " "
                elif (len(str(yAxisCount)) == 2):
                    plane[i][j] = str(yAxisCount) + " "
                elif (len(str(yAxisCount)) == 3):
                    plane[i][j] = str(yAxisCount)
        yAxisCount += 1


    x_position = -50
    for y in range(1, 102):
        y_position = 50
        for x in range(0, 101):
            for value in TOV:
                try:
                    if (value[0] == x_position and value[1] == y_position):
                        plane[x][y] = " # "
                except:
                    pass
            y_position -= 1
        x_position += 1
    for i in plane:
        print("".join(i))
        #print(i)

def main():
    while True:
        equation = input("Enter equation of the line: ")
        equation = equationFormatter(equation)
        TOV = []
        for i in range(-50, 51):
            try:
                TOV.append([i, round(eval(subX(equation, i)))])
            except:
                TOV.append("")
        cartesianPlanePrinter(TOV)

if __name__ == "__main__":
    main()