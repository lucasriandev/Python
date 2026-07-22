import imageio.v3 as iio

print("Funcionando!")
imagem1 = ['team-pic1.png','team-pic2.png']
img = []

for imagem in imagem1:
    img.append(iio.imread(imagem))

print(len(img))
iio.imwrite('team.gif', img, duration = 500, loop = 0)

