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
    while cpt < len(listOfItems):
        item = listOfItems[cpt]
        if len(target) ==0:
            #print(temp , "is OK")
            return 1
        if target.startswith(item):
            target = target[len(item) :]
            cpt =-1
            print(item, end= ',')
        cpt +=1
    return 0

def is_substring_in_array(substring, array_of_strings):
    for string in array_of_strings:
        if substring in string:
            return True
    return False


def checkIfExists_part_2(target , listOfItems , foundPatterns):
    final = ''
    restart = False
    i=0
    j=0
    
    while i < len(listOfItems):
        if len (target) ==0 :
            return final
        while j <len(listOfItems):
            item = listOfItems [j]
            if target.startswith(item) :
                checkValue = final + ','+item if final != '' else item
                if is_substring_in_array(checkValue, foundPatterns) == False :
                    target = target[len(item) :]
                    final += item + ','
                    j = -1
            j+=1
        i+=1
        j=0
    return ''


def perm (s):
    first = s[0]
    s=s[1:]
    s=s + [first]
    return s



def countOccurences (target , listOfItems):
    patterns = []
    temp_target = listOfItems
    temp_val = ''
    for i in range (len(listOfItems)):

        temp_val =checkIfExists_part_2(target , temp_target , patterns)
        print(temp_val)
        if temp_val not in patterns and temp_val != '':
            patterns.append(temp_val)
        temp_target = perm(temp_target)
    
    return len(patterns)




if __name__ == "__main__":
    # for key in hashmap:
    #     x= len(result)
    #     for i in range( 0 ,x):
    #         result = perm(result)
    #         returnVal = checkIfExists(key , result , hashmap[key] )
    #         hashmap[key] = returnVal
    #     result= perm(result)

    # count = sum(1 for value in hashmap.values() if value == 1)

    # # Print the count
    # print(f"Number of entries with value 1: {count}")


    for key in hashmap:
        val = countOccurences (key , result)
        print(val)

