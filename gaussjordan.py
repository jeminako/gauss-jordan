# Date:        20.02.2020
# Author:      Jemina Kotkajuuri
# Description: A fun Gauss-Jordan Elimination experiment
#TODO: Yleistä ref ja rref samaksi aliohjelmaksi. Parantele tulostusten ulkonäköä.


#Ask the user for a matrix
def getMatrix():
    mat = []
    print("Number of rows?")
    while True:
        num = input()
        if (num.isdigit()):
            rNumber = int(num)
            break
        else:
            print("Bad input! Give number of rows")
    print("Number of columns?")
    while True:
        num = input()
        if (num.isdigit()):
            cNumber = int(num)
            break
        else:
            print("Bad input! Give number of columns")
    formMatrix(rNumber, cNumber, mat)
    printMatrix(mat)
    return mat


#Form the matrix from the user info
def formMatrix(rNumber, cNumber, m):
    for x in range(rNumber):
        print('give row {0}, separate numbers with spaces, eg. 1 2 3:'.format(x+1))
        while True:
            userRow = input()
            if (len(userRow.split()) == cNumber ):
                break
            else:
                print("There should be {0} numbers on your row".format(cNumber))
        row = [float(i) for i in userRow.split()] 
        m.append(row)


#Printer for matrices
def printMatrix(m):
    print()
    for x in m:
        print(x)
    print()


# Orders rows according to Gauss-Jordan algorithm
def orderRows(m, columns):
    for i in range(columns, len(m)):
        if (m[i][columns] != 0):
            m.insert(columns, m.pop(i))
            break


def ref(m):
    rows = 0
    columns = 0

    while (rows < len(m)-1):
        orderRows(m, columns)

        if (m[rows].count(0) == len(m[0])):
            rows += 1
            columns += 1
            continue

        #Multiply the leading row so that the leading number equals 1
        modifiedRow = []
        modifiedRow = [entry / m[rows][columns] if m[rows][columns] != 0 else modifiedRow.append(0) for entry in m[rows]]
        m[rows] = modifiedRow
        leading = m[rows][columns]

        for x in range(rows + 1, len(m)):
            multiplier = m[x][columns] / leading
            multipliedRow = []

            # Multiply the leading row so you can substract it from rows below
            for i in range(len(m[rows])):
                multipliedRow.append(m[rows][i] * float(multiplier))
            
            # Substract the leading row
            for j in range(len(m[x])):
                m[x][j] = m[x][j] - multipliedRow[j]
        printMatrix(m)
        rows += 1
        columns += 1


def rref(m):
    rows = len(m)-1
    columns = len(m[0])-1

    while (rows > 0):
        if (m[rows].count(0) == len(m[0])):
            rows -= 1
            columns -= 1
            continue
        #Multiply the leading row so that the leading number equals 1
        modifiedRow = []
        modifiedRow = [entry / m[rows][columns] if m[rows][columns] != 0 else modifiedRow.append(0) for entry in m[rows]]
        m[rows] = modifiedRow
        leading = m[rows][columns]

        for x in range(rows - 1, -1, -1):
            if (leading == 0):
                break
            multiplier = m[x][columns] / leading
            multipliedRow = []

            # Multiply the leading row so you can substract it from rows below
            for i in range(len(m[rows])):
                multipliedRow.append(m[rows][i] * float(multiplier))
            
            # Substract the leading row
            for j in range(len(m[x])):
                m[x][j] = m[x][j] - multipliedRow[j]
        printMatrix(m)
        rows -= 1
        columns -= 1


def end():
    print("Try another matrix? (y/n)")
    answer = input()
    if (answer == 'y'):
        main()
    elif (answer == 'n'):
        exit()
    end()


def main():
    m = getMatrix()
    ref(m)
    rref(m)
    printMatrix(m)
    end()


main()