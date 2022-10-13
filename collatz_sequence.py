def collatzSequence(number):
    # Return a collatz sequence

    if number == 1:
        return
        
    elif number <= 0:
        return
    
    if number % 2 == 0:
        new_number = int(number / 2)
        print(new_number)
        
    elif number % 2 > 0:
        new_number = (number * 3) + 1
        print(new_number)
        
    return collatzSequence(new_number)


n = int(input('Enter any digit: '))

collatzSequence(n)