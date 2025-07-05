def fizzbuzz(number):
    if number % 3 == 0:
        return "fuzz"
    if number % 5 == 0:
        return "bizz"
    else:
        return number
    
    
print(fizzbuzz(3))
print(fizzbuzz(5))

