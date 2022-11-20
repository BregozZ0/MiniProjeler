while True:

    num1 = int(input("Birinci sayi giriniz : "))
    num2 = int(input("İkinci sayiyi giriniz : "))
    opt = input("'+ - * /'  : ")


    def calculator(x, y, operator):

        if operator == "+ - * /":
            print("Sadece + - * / ")

        if type(x) != int and type(x) != float and type(y) != int and type(y) != float:
            print("Lütfen sadece rakam giriniz")

        if operator == "+":
            print(f"{x} {operator} {y} = {x + y}")

        if operator == "-":
            print(f"{x} {operator} {y} = {x - y}")

        if operator == "/":
            print(f"{x} {operator} {y} = {x / y}")

        if operator == "*":
            print(f"{x} {operator} {y} = {x * y}")


    calculator(num1, num2, opt)
