import random

def compare_random_numbers():
    num1 = random.randint(1, 100)  # Generate random number between 1 and 100
    num2 = random.randint(1, 100)
    
    if num1 > num2:
        result = f"{num1} is greater than {num2}."
    elif num1 < num2:
        result = f"{num1} is less than {num2}."
    else:
        result = f"{num1} is equal to {num2}."
        
    return result

result5 = compare_random_numbers()
print(result5)