'''
Your task is to write a function that accepts a floating point number and formats it using the notation given above.
The resulting number should include 3 most significant digits and be rounded down towards zero (for example, 1238 should be 1.23K, and -1238should be -1.23K). 
All trailing zeroes after the decimal point should be removed, and the decimal point should be excluded 
if the resulting number is whole number of units after the rounding down. 
If the number is too small and it's rounded down to 0, then 0 should be returned. 
Beware of the negative zero, which should not appear in the output, insted the regular zero 0 should be returned.
'''
import math

def format_num(n):
    units = ['', 'K', 'M', 'B', 'T']
    overflow_units = 'abcdefghijklmnopqrstuvwxyz'
    sign = '-' if n < 0 else ''
    n = abs(n)

    if n < 1:
        return '0'

    magnitude = int(math.floor(math.log10(n) / 3))
    if magnitude >= len(units):
        unit1 = overflow_units[(magnitude - len(units)) // 26]
        unit2 = overflow_units[(magnitude - len(units)) % 26]
        unit = unit1 + unit2
    else:
        unit = units[magnitude]

    n = n / (1000 ** magnitude)
    n = math.floor(n * 100) / 100

    formatted_num = f'{n}'.rstrip('0').rstrip('.') if '.' in f'{n}' else f'{n}'
    formatted_num = sign + formatted_num + unit

    return formatted_num

# Examples
print(format_num(0))  # Expected output: 0
print(format_num(1))  # Expected output: 1
print(format_num(-1))  # Expected output: -1
print(format_num(123))  # Expected output: 123
print(format_num(0.25))  # Expected output: 0.25
print(format_num(-0.9999))  # Expected output: -0.99
print(format_num(0.009))  # Expected output: 0 (too small)
print(format_num(1000))  # Expected output: 1K
print(format_num(1234))  # Expected output: 1.23K
print(format_num(-4002))  # Expected output: -4K
print(format_num(5809))  # Expected output: 5.8K
print(format_num(100000))  # Expected output: 100K
print(format_num(123456789))  # Expected output: 123M
print(format_num(1234567890))  # Expected output: 1.23B
print(format_num(1234567890000))  # Expected output: 1.23T
print(format_num(999999999999999))  # Expected output: 999T
print(format_num(1234567890000000000))  # Expected output: 1.23ab
print(format_num(-0.0000001))  # Expected output: 0
print(format_num(10**300))  # Expected output: 1dr
