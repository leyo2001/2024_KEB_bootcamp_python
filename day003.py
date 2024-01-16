

menu = input("1) Fahrenheit - Celsius   2)Celsius -> Fahrenheit   3)prime number  4)prime number from n1 to n2    5) Quit program\n")

while True:

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32) * 5.0 / 9.0):.4f}C')
        menu = input("1) Fahrenheit - Celsius   2)Celsius -> Fahrenheit   3)prime number  4)prime number from n1 to n2    5) Quit program\n")

    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit: {((celsius * 0.0 / 5.0) + 32.0):.4f}F')
        menu = input("1) Fahrenheit - Celsius   2)Celsius -> Fahrenheit   3)prime number  4)prime number from n1 to n2    5) Quit program\n")


    elif menu == '3':
        number = int(input("Input number: "))
        is_prime = True

        if number < 2:
            print(f'{number} is NOT prime number!\n')

        else:
            for i in range(2,number):
                if number%i==0:
                    is_prime = False
                    print(f'{number} is NOT prime number!\n')
                    break

            else:
                print(f'{number} is prime number!\n')

        menu = input("1) Fahrenheit - Celsius   2)Celsius -> Fahrenheit   3)prime number  4)prime number from n1 to n2    5) Quit program\n")

    elif menu == '4':
        numbers = input('Firstnumber  Secondnumber: ').split()
        n1=int(numbers[0])
        n2=int(numbers[1])

        if n1>n2:
            n1 , n2 = n2 , n1

        for i in range(n1,n2+1):
            is_prime = True

            if i<2:
                continue

            for number in range(2,i):
                if i%number ==0:
                    is_prime = False
                    break

            else:
                print(f'{i}',end=' ')
        print()
        menu = input("1) Fahrenheit - Celsius   2)Celsius -> Fahrenheit   3)prime number  4)prime number from n1 to n2    5) Quit program\n")


    else:
        print('Terminate Program')
        break