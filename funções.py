'''variavel1 = "texto1"
variavel2 = " texto2"
variavel3 = '""'
"""texto 3 de 1 
texto 3 de 2
texto 3 de 3"""
print(variavel1)
print(variavel3)
print(variavel2)
print("\tOI!\nEu me chamo \"(Rafael)\"!!!")
def dizer_ola(nome_usuario = "mundo"):
    print("Olá ", nome_usuario)             

dizer_ola("Guilherme")
dizer_ola()
    
dizer_ola("cachorro")
dizer_ola(188+777)

nome = int(input("insira um numero: "))
saudaçao = nome - 2
print(saudaçao)

numero = 3
def apresentar_numero():
    global numero
    print(numero)
    numero = 2
    print(numero)

apresentar_numero()
print(numero)

def quadrado(area):
    resultado = area ** 2 
    return resultado
print(quadrado(4))

def salario(reajuste):
    reajuste = reajuste * 0.15
    return reajuste
print(salario(1500))

def conversor(celsius):
    fahrenheit = (9*celsius+160)/5
    return fahrenheit
print(conversor(100))

def valores (x,y):
    z=x
    x=y
    y=z
    return ("o valoe de x é: ", x)
            ("e o valor de y é:", y")
print(valores(2, 3))

 triangulo(base, altura):
    return base * altura / 2 
print(triangulo(5,3))
'''
def volume(comprimento, largura, altura):
    return()
