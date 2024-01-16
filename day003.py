#prime number
number = int(input("Input number : "))
is_prime=True

if number < 2:
    print(f'{number} is NOT prime number')
else:
    i=2
    for i in range(2,number):
            is_prime = False # remove +
            break


    if is_prime:
        print(f'{number} is prime number')
    else:
        print(f'{number} is NOT prime number')



# subjects = { 'python' : 'kim', 'c++' : 'sung', 'datastructure' : 'kim', ' database': 'kang'}
# print("{0[python]} {0[c++]}".format(subjects))

