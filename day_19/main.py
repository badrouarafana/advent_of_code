#!/usr/bin/python3
import math


with open('input.txt', 'r') as file:
    content = file.read().strip()
    
    result = [item.strip() for item in content.split(',')]

with open('liste.txt', 'r') as file:
    lines = [line.strip() for line in file]

hashmap = {line: 0 for line in lines}

# Print the resulting hashmap


def checkIfExists(target , listOfItems , lastValue):
    if lastValue == 1:
        return 1
    cpt=0
    temp = target
    while cpt < len(listOfItems):
        item = listOfItems[cpt]
        if len(target) ==0:
            print(temp , "is OK")
            return 1
        if target.startswith(item):
            target = target[len(item) :]
            cpt =-1
        cpt +=1
    return 0


def perm (s):
    first = s[0]
    s=s[1:]
    s=s + [first]
    return s


if __name__ == "__main__":
    for key in hashmap:
        x= len(result)
        for i in range( 0 ,x):
            result = perm(result)
            returnVal = checkIfExists(key , result , hashmap[key] )
            hashmap[key] = returnVal
        result= perm(result)

    count = sum(1 for value in hashmap.values() if value == 1)

    # Print the count
    print(f"Number of entries with value 1: {count}")


  
        

