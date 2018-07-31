def deco(func):

    def action(a, b, veces):
        for i in range(veces):
            a = a*b
            func(a)

    return action


@deco
def multiply(parametro):
    print("El resultado es {}".format(parametro))


if __name__ == '__main__':
    times = int(input("Veces que debe repetirse la operación: "))
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))

    multiply(num1, num2, times)