#CODEDEX
def predict_price(sq_footage):
    return 101 * sq_footage + 84000

sq_footage = 1000
preco_previsto = predict_price(sq_footage)
print(f"O custo previsto para uma casa com {sq_footage} pés quadrados é: {preco_previsto}")