def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a= [1,23,3656,34578,68,34,76789,98,55,45]

f=list(filter(divisible5,a))
print(f)