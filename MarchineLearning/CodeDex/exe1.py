def predict_price(sq_footage, age):
    """
    Calcula o preço de uma casa aplicando a fórmula de um modelo de regressão linear múltipla.
    """
    
    # O cálculo combina três fatores extraídos do modelo treinado:
    # 1. (101 * sq_footage): Adiciona valor com base no tamanho da casa (coeficiente positivo).
    # 2. - (1000 * age): Reduz o valor com base na idade da casa (taxa de depreciação).
    # 3. + 84000: O valor base de partida da casa (intercepto).
    preco = (101 * sq_footage) - (1000 * age) + 84000
    
    return preco

# Executando a função com dados reais:
# Simulando uma casa de 1000 pés quadrados e 10 anos de idade.
custo_previsto = predict_price(1000, 10)

# O resultado esperado é 175000 (101.000 de área - 10.000 de idade + 84.000 de base)
print(f"O custo previsto da casa é: {custo_previsto}")