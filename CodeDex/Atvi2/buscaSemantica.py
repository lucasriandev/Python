documents = [
  'the cat sat on the warm mat',
  'the dog chased a stick in the yard',
  'I love pizza and pasta for dinner',
  # ...
]

def build_vocab(texts):
  vocab = []                      # 1. Cria uma lista vazia para guardar o dicionário
  for text in texts:              # 2. Pega uma frase por vez da nossa lista de textos
    for word in text.split():     # 3. Corta a frase nos espaços (split) e pega uma palavra por vez
      if word not in vocab:       # 4. Checa: essa palavra já está no nosso dicionário?
        vocab.append(word)        # 5. Se não estiver, adiciona ela na lista
  return vocab                    # 6. Devolve o dicionário pronto, sem nenhuma palavra repetida

resultado = build_vocab(documents)
print(resultado)