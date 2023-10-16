'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.
'''
def persistence(num):
    count = 0
    
    while num >= 10:
        product = 1
        
        while num > 0:
            product *= num % 10
            num //= 10
        
        num = product
        count += 1
    
    return count

print(persistence(39))  #Output: 3
print(persistence(999))  #Output: 4
print(persistence(4))  #Output: 0





