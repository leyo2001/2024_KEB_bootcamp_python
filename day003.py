#prime number
number = int(input("Input number : "))
is_prime=True
i=2
while i<number:
    if number%i==0:
        is_prime = False # remove +
        break
    # print(i, end=' ')
    i+=1

if is_prime:
    print(f'{number} is prime number')
else:
    print(f'{number} is NOT prime number')



# subjects = { 'python' : 'kim', 'c++' : 'sung', 'datastructure' : 'kim', ' database': 'kang'}
# print("{0[python]} {0[c++]}".format(subjects))

