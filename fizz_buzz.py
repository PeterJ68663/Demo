def fizzbuzz(number):
    if number % 3 == 0:
        return "fuzz"
    if number % 5 == 0:
        return "bizz"
    else:
        return number
    
print("ARBOx is awesome!")
print(fizzbuzz(3))
print(fizzbuzz(5))

