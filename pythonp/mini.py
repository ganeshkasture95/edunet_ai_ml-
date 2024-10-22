# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Factorial 

def fact(n):
    if n<0:
        print("Invalid Input")
    
    elif n==0:
        return 1
    
    for i in range(1,n):
        factorial = n * i
    return factorial

print(fact(3))

# Area of circle 

def CArea(red):
    return 3.14*(red**2)

print(CArea(4))