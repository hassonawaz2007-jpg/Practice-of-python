'''def sum(n):
    if(n==0):
        return 0   #finding sum of the given number
    return n+sum(n-1)

n=4
print("sum of first",n,"number is",sum(n))'''


'''def factorial(n):
    if(n==0 or n==1):
        return 1        # finding factoeial of the givrn number
    return n*factorial(n-1)

n=6
print("the factorial of",n,"is",factorial(n))'''


'''def count(n):
    if(n<10):
        return 1
    return 1+count(n//10)   #for counting didgits in the given num
n=123456
print("digits in",n,"is",count(n))'''



'''def num(n):
    if(n==0):
        return 0
    return(n%10)+num(n//10)  #for the sum of all digits

n = 123
print("Sum of digits of", n, "is:", num(n))'''


'''def num(n):
    if(n==0):
        return   #point numbers from n down to 1
    
    print(n, end="")
    num(n - 1)
    
n=5
num(n)'''


