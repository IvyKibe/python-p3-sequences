#!/usr/bin/env python3

def print_fibonacci(length):

    added_list=[]
    a,b =0,1
    for i in range(length):
        added_list.append(a)
        a,b =b,a+b

    print(added_list)
    
print_fibonacci(10)    
    