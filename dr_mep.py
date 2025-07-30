

valor_total = 0
raças = ['pug','pastor-alemão1,','labrador,']
print(raças[0])
print(raças[1])
print('labrador' in raças)

def escolharaça():
    valor_total = 0
    raças = ['pug','pastor-alemão1,','labrador,']
    print(raças[0])
    print(raças[1])
    raça = input('labrador')
    if (raça in raças):
        if (raça == pug ):
            valor_total = valor_total + 70.99
    elif (raça == 'pastor-alemão'):
        valor_total = valor_total + 120.99
    elif (raça == 'labrador'):
        valor_total = valor_total + 110.99
        print(valor_total)
    else:
        print('atendimento indisponivel')
escolharaça()