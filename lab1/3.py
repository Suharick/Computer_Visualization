from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("1.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

lst = []
count = [0]*256

for x in range(width):
        for y in range(height):
                i = pix[x, y][1]
                lst.append(i)
                count[i] = count[i] + 1 
m = max(count)
k = (height//2)/m

for x in range(256):
        for y in range(height//2):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                if (y >= k*(m - count[x]) and y <= m*k and x<=256):
                    draw.point((x, y), (0, 255, 0))
                                
image.show()
del draw
