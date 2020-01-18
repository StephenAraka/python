num1 = 55.01234
num2 = 45.01234

# NORMAL UN-CONCATED STRING
# print('num 1 is', num1, 'and num 2 is', num2)

# USING STRING FORMATTING 
print('num 1 is {} and num 2 is {}'.format(num1, num2))

# PASSING VARIABLE POSITIONS - AS INDEX
print('num 1 is {0} and num 2 is {1}'.format(num1, num2))

# POSITION + FORMATTING - e.g truncating number
print('num 1 is {0:.2f} and num 2 is {1:.2f}'.format(num1, num2))

print('###############')

# USING F-STRINGS
print(f'num 1 is {num1:.4f} and num 2 is {num2:.4}')