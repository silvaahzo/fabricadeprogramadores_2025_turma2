estoque = {   
    "versys 650": [432, 52.990],
    "bmw s1000": [234, 58.990],
    "Hyundai HB20 Sense 1.0": [351, 59.990],
    "Chevrolet Onix Joy 1.0": [345, 60.000],
    "Voltswagen Gol 1.0": [523, 63.000],
    "vstron 700": [234, 67.000],
    "Peugeot 208 Like 1.0": [543, 75.885],
    "Fiat Cronos 1.3": [235, 76.798],
    "Fiat Strada Endurance": [346, 94.203],
    "Hyundai HB20S Sense": [123, 97.336],
    "Voltswagen Saveiro CS": [533, 99.990],
    "Fiat Strada Freedom": [234, 103.990],
    "Peugeot 2008 Allure": [234, 103.490],
    "Chevrolet Tracker Turbo": [565, 109.990],
    "Nissan Versa Sense": [324, 119.990],
    "Toyota Yaris Hatch XL": [342, 92.990],
    "bmw 1200": [231, 96.990],
    "Cg 160": [234, 112.990],
    "Voltswagen Polo": [231, 72.990],
    "bmw gs310": [231, 82.990],
    
}

total = 0
print("=== Registro de Vendas ===")

while True:
    produto = input("Digite o nome do carro (ou 'fim' para encerrar): ").lower()
    
    if produto == "fim":
        break
    
    if produto not in estoque:
        print("Produto não encontrado no estoque.")
        continue
    
    try:
        quantidade = int(input("Digite a quantidade vendida: "))
    except ValueError:
        print("Quantidade inválida. Tente novamente.")
        continue
    
    if quantidade > estoque[produto][0]:
        print(f"Estoque insuficiente! Disponível: {estoque[produto][0]}")
        continue
    
    preco = estoque[produto][1]
    custo = preco * quantidade
    estoque[produto][0] -= quantidade
    total += custo
    
    print(f"Venda registrada: {produto} - {quantidade} x R$ {preco:.2f} = R$ {custo:.2f}\n")

print(f"\nCusto total das vendas: R$ {total:.2f}\n")

print("=== Estoque Atualizado ===")
for nome, dados in estoque.items():
    print(f"Descrição: {nome}")
    print(f"Quantidade: {dados[0]}")
    print(f"Preço: R$ {dados[1]:.2f}\n")
