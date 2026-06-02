s = "III"

roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
number = []
answer = 0

for char in s:
    number.append(roman_dict[char])
                
for num in range(len(number)-1):
    if number[num] < number[num+1]:
        answer += number[num+1] - number[num]
    else:
        answer += number[num]
answer += number[-1]
print(answer)