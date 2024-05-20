def calculadora(num1, num2, operacao):
    operacoes = {
        1: num1 + num2,
        2: num1 - num2,
        3: num1 * num2,
        4: num1 / num2 if num2 != 0 else "Erro: Divisão por zero!"
    }
    return operacoes.get(operacao, 0)

# Exemplo de uso:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)
