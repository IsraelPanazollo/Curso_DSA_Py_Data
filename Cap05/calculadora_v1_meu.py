# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

Ligado = True

while Ligado:

    print("\nAs operações são: \nSoma (+) \nSubtração (-) \nMultiplicação (*) \nDivisão (/) \nPotenciação (^)\n")

    num1 = float(input("Digite um número: "))
    op = input("Digite a operação desejada: ")
    num2 = float(input("Digite um número: "))

    if op == "+":
        r = num1+num2
        print(num1, "+" ,num2, "=", r)
    elif op == "-":
        r = num1 - num2
        print(num1, "-" ,num2, "=", r)
    elif op == "*":
        r = num1 * num2
        print(num1, "*" ,num2, "=", r)
    elif op == "^":
        r = num1 ** num2 
        print(num1, "^" ,num2, "=", r)
    elif op == "/":
        if num2 == 0:
            print ("Não é possível dividir por zero")
        else:
            r = num1/num2
            print(num1, "/" ,num2, "=", r)
    else:
        print("Operação inválida")
    
    aux = input("Para continuar tecle 0, senão pressione qualquer tecla ")
    
    if aux != "0":
        Ligado = False
