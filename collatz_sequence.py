def collatzSequence(number):
    
    if number == 1 or number <= 0:
        return
    
    if number % 2 == 0:
        new_number = int(number / 2)
        print(new_number)
        
    elif number % 2 > 0:
        new_number = (number * 3) + 1
        print(new_number)
        
    return collatzSequence(new_number)


if __name__ == '__main__':

    try:
        n = int(input('Enter any digit: '))
        collatzSequence(n)
    
    except Exception as e:
        print(e)
        n = int(input('Enter any digit: '))
        collatzSequence(n)

    