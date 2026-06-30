def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    elif number == 1:
        return 1
    
    sum = 1
    current_square = 2
    while current_square <= number:
        sum *= 2
        current_square += 1
    
    return sum
    
    


def total():
    sum = 1
    square = 1
    while square < 65:
        sum *= 2
        square += 1
    return sum-1 # why does sum have to be subtracted? I have no clue, but it wouldn't pass tests otherwise
