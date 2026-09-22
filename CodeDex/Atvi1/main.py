# Words as Numbers 🔢
# Codédex

vocab = ['cat', 'dog', 'Tuesday', 'happy', 'sad']

def one_hot(word, vocab):
  vector = [0] * len(vocab)
  vector[vocab.index(word)] = 1
  return vector

def hamming(v1, v2):
  count = 0
  for a, b in zip(v1, v2):
    if a != b:
      count += 1
  return count

cat = one_hot('cat', vocab)
dog = one_hot('dog', vocab)
tuesday = one_hot('Tuesday', vocab)

print(cat)
print(dog)
print(tuesday)

print(hamming(cat, dog))
print(hamming(cat, tuesday))
print(hamming(dog, tuesday))