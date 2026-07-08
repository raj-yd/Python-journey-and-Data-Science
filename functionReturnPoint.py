# def check_even(num):
#     if num % 2 == 0:
#         return True
#     return False
#     print('This is the line never RUNS')

# print(check_even(4))
# print(check_even(7))

#write a function to return all the prime numbers in list type within the range 1 - N. 
#Take input N from the user

def primeNum1toN(n):
    prime=[]
    for number in range(1,n+1):
        flag=1
        for i in range(2,(number//2)+1):
            if number%i==0:
                flag = 0
                break
        if flag == 1:
            prime.append(number)
    return prime
num=int(input("Enter number N : "))
print(primeNum1toN(num))