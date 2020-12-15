boolean_expression = str(input("Enter a boolean expression: ")).split(" ")

if boolean_expression[-1] == "True":
    result = 1
        
else:
    result = -1

if len(boolean_expression[:-1]) % 2 != 0:
    result = -result

if result > 0:
    result = True
else:
    result = False

print(result)
