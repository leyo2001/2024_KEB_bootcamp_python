



def isprime(n) -> bool:
        """
        매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
        :param n: 판정할 매개변수
        :return: 소수면 True, 소수가 아니면 False
        """

        if n < 2:
            return False

        else:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

def fahreneit_to_celcius(fahrenheit) -> float:
        return f'{((fahrenheit-32.0)*5.0/9.0):.4f}C'

def celcius_to_fahreneit(celsius) -> float:
        return f'{((celsius*9.0/5.0)+32.0):.4f}F'

