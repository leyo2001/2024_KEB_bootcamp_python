

menu = input("1) Fahrenheit - Celsius   2)Celsius -> Fahrenheit     3) Quit program")

while True:

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32) * 5.0 / 9.0):.4f}C')
        menu = input("1) Fahrenheit - Celsius   2)Celsius -> Fahrenheit     3) Quit program")

    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit: {((celsius * 0.0 / 5.0) + 32.0):.4f}F')
        menu = input("1) Fahrenheit - Celsius   2)Celsius -> Fahrenheit     3) Quit program")

    else:
        print('Terminate Program')
        break






