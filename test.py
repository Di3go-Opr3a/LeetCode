matrix = [["I", "V", "X", "L", "C", "D", "M"], [1, 5, 10, 50, 100, 500, 1000]]
s = "DCXXI"
sum = 0
x = 0

while x < len(s):
    symbol = s[x]
    if x < (len(s)-1):
        symbol2 = s[x+1]
        if (symbol == "I" and symbol2 == "V") or (symbol == "I" and symbol2 == "X"):
            sum += (matrix[1][matrix[0].index(symbol2)] - matrix[1][matrix[0].index(symbol)])
            x += 2
        elif (symbol == "X" and symbol2 == "L") or (symbol == "X" and symbol2 == "C"):
            sum += (matrix[1][matrix[0].index(symbol2)] - matrix[1][matrix[0].index(symbol)])
            x += 2
        elif (symbol == "C" and symbol2 == "D") or (symbol == "C" and symbol2 == "M"):
            sum += (matrix[1][matrix[0].index(symbol2)] - matrix[1][matrix[0].index(symbol)])
            x += 2
        else:
            sum += matrix[1][matrix[0].index(symbol)]
            x += 1
    else:
        sum += matrix[1][matrix[0].index(symbol)]
        x += 1
print(sum)