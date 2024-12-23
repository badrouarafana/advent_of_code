#!/usr/bin/python3
import math


with open('input.txt', 'r') as file:
    content = file.read().strip()
    
    result = [item.strip() for item in content.split(',')]

with open('liste.txt', 'r') as file:
    lines = [line.strip() for line in file]

hashmap = {line: 0 for line in lines}


def count_arrangements(input, arr, hashMap):

    ret = 0
    if len(input) ==0:
        return 1
    
    if input in hashMap :
        return hashMap[input]
    
    for i in arr:
        if input.startswith(i):
            ret+= count_arrangements (input[len(i):], arr , hashMap) 

    hashMap[input] = ret
    return ret




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
    cpt =0 
    hm ={}
    for key in hashmap:
        
        val = count_arrangements (key , result, hm)
        cpt += val
        
    
    print(cpt )

