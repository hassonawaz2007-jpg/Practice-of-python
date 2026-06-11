from functools import reduce
l= [111 , 64 , 53 ,635 ,65 ,74 ,45 ,55]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))