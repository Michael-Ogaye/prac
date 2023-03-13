def sumStrings(a, b):
    # Pad the shorter string with zeros to make the lengths equal
    diff = len(a) - len(b)
    if diff > 0:
        b = '0' * diff + b
    else:
        a = '0' * (-diff) + a
    
    # Perform the addition digit by digit
    carry = 0
    result = []
    for i in range(len(a)-1, -1, -1):
        digit_sum = int(a[i]) + int(b[i]) + carry
        carry = digit_sum // 10
        digit = digit_sum % 10
        result.append(str(digit))
    
    # Add any remaining carry to the most significant digit
    if carry > 0:
        result.append(str(carry))
    
    # Reverse the result and remove leading zeros
    result.reverse()
    while len(result) > 1 and result[0] == '0':
        result.pop(0)
    
    # If the result is empty, return '0' instead of an empty string
    if not result:
        return '0'
    
    # Convert the result to a string and return it
    return ''.join(result)
    
    
    
    
    
    
    
    
    def sum_strings(x, y):
    l, res, carry = max(len(x), len(y)), "", 0
    x, y = x.zfill(l), y.zfill(l)
    for i in range(l-1, -1, -1):
        carry, d = divmod(int(x[i]) + int(y[i]) + carry, 10)
        res += str(d)
    return ("1" * carry + res[::-1]).lstrip("0") or "0"
    
    
    
    from gmpy2 import mpz

def sum_strings(x, y):
    return str(mpz(x or '0') + mpz(y or '0'))
    
    
    
    

