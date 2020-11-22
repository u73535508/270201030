number = int(input("Enter a number with at least two digits:"))
first_digit = number % 10
second_digit = ( number // 10 )%10

print(first_digit + second_digit)