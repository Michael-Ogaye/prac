def next_bigger(num):
    # Convert the number to a list of digits
    digits = list(str(num))

    # Find the first digit from the right that is smaller than the digit to its right
    for i in range(len(digits)-2, -1, -1):
        if digits[i] < digits[i+1]:
            # Find the smallest digit to the right of the current digit that is greater than it
            for j in range(len(digits)-1, i, -1):
                if digits[j] > digits[i]:
                    # Swap the current digit with the smallest greater digit to its right
                    digits[i], digits[j] = digits[j], digits[i]
                    # Reverse the digits to the right of the current digit
                    digits[i+1:] = digits[i+1:][::-1]
                    # Convert the list of digits back to a number and return it
                    return int(''.join(digits))

    # If no such digit is found, the number cannot be rearranged
    return None

