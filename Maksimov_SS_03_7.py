''' 	
A bouncy number is a positive integer whose digits neither increase nor decrease. 
For example, 1235 is an increasing number, 5321 is a decreasing number, and 2351 is a bouncy number. 
By definition, all numbers under 100 are non-bouncy, and 101 is the first bouncy number.

Determining if a number is bouncy is easy, but counting all bouncy numbers with N digits can be challenging for large values of N. 
To complete this kata, you must write a function that takes a number N and return the count of bouncy numbers with N digits. 
For example, a "4 digit" number includes zero-padded, smaller numbers, such as 0001, 0002, up to 9999.

For clarification, the bouncy numbers between 100 and 125 are: 101, 102, 103, 104, 105, 106, 107, 108, 109, 120, and 121.
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def count_bouncy_numbers(N):
    def count_increasing_or_decreasing(is_increasing):
        total = 0
        start = 0 if is_increasing else 1
        for i in range(start, 10):
            total += combination(9 + N - i - 1, N - 1)
        return total

    total_numbers = 10**N
    increasing_numbers = count_increasing_or_decreasing(True)
    decreasing_numbers = count_increasing_or_decreasing(False)
    both_types = 10

    bouncy_numbers = total_numbers - (increasing_numbers + decreasing_numbers - both_types)

    return bouncy_numbers

print(count_bouncy_numbers(2)) # Expected output: 0 (as numbers under 100 are non-bouncy)
print(count_bouncy_numbers(3)) # Example: count of bouncy numbers with 3 digits
print(count_bouncy_numbers(4)) # Example: count of bouncy numbers with 4 digits









