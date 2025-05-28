def soma():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    resultado = a + b
    print(f"A soma de {a} e {b} é {resultado}")
def media():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    resultado = (a + b + c) / 3
    print(f"A média de {a}, {b} e {c} é {resultado}")
def parouimpar():
    a = int(input("Digite um valor: "))
    if a % 2 == 0:
        print(f"{a} é par")
    else:
        print(f"{a} é ímpar")
def maior():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    if a > b:
        print(f"{a} é maior que {b}")
    elif b > a:
        print(f"{b} é maior que {a}")
    else:
        print(f"{a} e {b} são iguais")
def positivoounegativo():
    a = int(input("Digite um valor: "))
    if a > 0:
        print(f"{a} é positivo")
    elif a < 0:
        print(f"{a} é negativo")
    else:
        print("O valor é zero")
def tabuada():
    a = int(input("Digite um número para ver sua tabuada: "))
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")
def somaintervalo():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    if a > b:
        a, b = b, a
    resultado = sum(range(a, b + 1))
    print(f"A soma dos números entre {a} e {b} é {resultado}")
def contagemregressiva():
    a = int(input("Digite o número para iniciar a contagem regressiva: "))
    for i in range(a, -1, -1):
        print(i)
def pares():
    a = int(input("Digite o número máximo: "))
    print("Números pares até", a, ":")
    for i in range(2, a + 1, 2):
        print(i, end=' ')
def fatorial():
    a = int(input("Digite um número para calcular o fatorial: "))
    resultado = 1
    for i in range(1, a + 1):
        resultado *= i
    print(f"O fatorial de {a} é {resultado}")
def fibonacci():
    a = int(input("Digite o número de termos da sequência de Fibonacci: "))
    fib = [0, 1]
    for i in range(2, a):
        fib.append(fib[i - 1] + fib[i - 2])
    print("Sequência de Fibonacci:", fib[:a])
def verificarprimo():
    a = int(input("Digite um número para verificar se é primo: "))
    if a < 2:
        print(f"{a} não é primo")
        return
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            print(f"{a} não é primo")
            return
    print(f"{a} é primo")
def IMC():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é {imc:.2f}")
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Peso normal")
    elif 25 <= imc < 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")
def mediaponderada():
    a = float(input("Digite a primeira nota: "))
    b = float(input("Digite a segunda nota: "))
    c = float(input("Digite a terceira nota: "))
    media = (a * 2 + b * 3 + c * 5) / 10
    print(f"A média ponderada é {media:.2f}")
def eleicaoporvotacao():
    votos = {}
    while True:
        voto = input("Digite o nome do candidato (ou 'fim' para encerrar): ")
        if voto.lower() == 'fim':
            break
        if voto in votos:
            votos[voto] += 1
        else:
            votos[voto] = 1
    vencedor = max(votos, key=votos.get)
    print(f"O candidato vencedor é {vencedor} com {votos[vencedor]} votos.")
def caixaeletronico():
    valor = int(input("Digite o valor para saque: "))
    notas = [100, 50, 20, 10, 5, 2]
    resultado = {}
    restante = valor

    for nota in notas:
        qtd, restante = divmod(restante, nota)
        if qtd > 0:
            resultado[nota] = qtd

    if restante != 0:
        print("Não é possível sacar esse valor com as notas disponíveis.")
    else:
        print("Notas entregues:")
        for nota in notas:
            if nota in resultado:
                print(f"{resultado[nota]} nota(s) de R$ {nota}")
def palindromo():
    frase = input("Digite uma frase: ").replace(" ", "").lower()
    if frase == frase[::-1]:
        print("A frase é um palíndromo.")
    else:
        print("A frase não é um palíndromo.")
def jogoadivinhacao():
    import random
    numero = random.randint(1, 100)
    chutes = 0
    while True:
        palpite = int(input("Adivinhe o número entre 1 e 100: "))
        chutes += 1
        if palpite < numero:
            print("Muito baixo!")
        elif palpite > numero:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou em {chutes} tentativas.")
            break
def contadorvogais():
    frase = input("Digite uma frase: ").lower()
    vogais = "aeiou"
    contador = {vogal: frase.count(vogal) for vogal in vogais}
    print("Contagem de vogais:")
    for vogal, qtd in contador.items():
        print(f"{vogal}: {qtd}")
def juroscompostos():
    capital = float(input("Digite o capital inicial: "))
    taxa = float(input("Digite a taxa de juros (em %): "))
    tempo = int(input("Digite o tempo (em anos): "))
    montante = capital * (1 + taxa / 100) ** tempo
    juros = montante - capital
    print(f"Montante final: R$ {montante:.2f}")
    print(f"Juros acumulados: R$ {juros:.2f}")