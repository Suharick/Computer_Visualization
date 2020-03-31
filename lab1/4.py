from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("1.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

 
countr = [0]*256

for x in range(width):
        for y in range(height):
                i = pix[x, y][1]
                countr[i] = countr[i] + 1 
mr = max(countr)
kr = (height//2)/mr

for x in range(256):
        for y in range(height//2):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                if (y >= kr*(mr - countr[x]) and y <= mr*kr and x<=256):
                    draw.point((x, y), (0, 255, 0))

countg = [0]*256

for x in range(width):
        for y in range(height):
                j = pix[x, y][0]
                countg[j] = countg[j] + 1 
mg = max(countg)
kg = (height//2)/mg
p = 0
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                if (y >= kg*(mg - countg[x]) and y <= mg*kg):

#                if (y >= kg*(mg - countg[p]) and y <= mg*kg and x >= (width//2)):
                    draw.point((x, y), (255, 0, 0))
                    p = p + 1

image.show()
del draw
