# loop from 1 to 100
# multiple of 3 print "Fizz"
# multiple of 5 print "buzz"
# multiple of 3 and 5 print "Fizz Buzz"

for i in range (1,101):
    if i%3==0 and i%5==0:
        print(f'fizz and buzz {i}')
    elif i%3==0:
        print(f'fizz {i}')
    elif i%5==0:
        print(f'buzz {i}')
