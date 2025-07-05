def fizzbuzz(number):
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    else:
        return number
    
    
print(fizzbuzz(3))
print(fizzbuzz(5))