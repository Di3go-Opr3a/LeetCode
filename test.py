roman_number = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s = "DCXXI"
sum = 0
x = 0

while x < len(s):
    if x < (len(s)-1):
        if (s[x] == "I" and (s[x+1] == "V" or s[x+1] == "X")):
            sum += (roman_number[s[x+1]] - roman_number[s[x]])
            x += 2
        elif (s[x] == "X" and (s[x+1] == "L" or  s[x+1] == "C")):
            sum += (roman_number[s[x+1]] - roman_number[s[x]])
            x += 2
        elif (s[x] == "C" and (s[x+1] == "D" or s[x+1] == "M")):
            sum += (roman_number[s[x+1]] - roman_number[s[x]])
            x += 2
        else:
            sum += roman_number[s[x]]
            x += 1
    else:
        sum += roman_number[s[x]]
        x += 1
print(sum)