import re

words= {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10"
}






def function (text):
    pattern = r'(1|2|3|4|5|6|7|8|9|0|one|two|three|four|five|six|seven|eight|nine|zero)'
    retValue=0
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    for i, item in enumerate(matches):
        if item in words:
            matches[i] = words[item]
    print(matches , matches[0]+matches [len(matches ) -1])

    if len(matches) ==0 :
        return 0
    elif len(matches) == 1 :
        return int(matches[0])
    else :
        return int(matches[0]+matches [len(matches ) -1])

with open('example.txt', 'r') as file:
    # Iterate through the file line by line
    sum =0
    for line in file:
        print(line.strip())
        sum += function(line)
       
    print(sum) 

