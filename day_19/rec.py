#!/usr/bin/python3
import math


with open('input.txt', 'r') as file:
    content = file.read().strip()
    
    result = [item.strip() for item in content.split(',')]

with open('liste.txt', 'r') as file:
    lines = [line.strip() for line in file]

hashmap = {line: 0 for line in lines}





def function (input, arr, hashMap):
    ret = False

    if len(input) ==0:
        return True
    
    if input in hashMap :
        return hashMap[input]
    
    for i in arr:
        if input.startswith(i):
            ret= function (input[len(i):], arr , hashMap) or ret

    hashMap[input] = ret
    return ret

    

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
    tata = {}
    cpt =0 
    for key in hashmap:
        
        val = function (key , result, tata)
        print(val)
        if val :
            cpt += 1
        
    
    print(cpt )

