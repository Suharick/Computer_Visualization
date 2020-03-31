from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("1.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

k = width+1

for x in range(width):
        for y in range(height):
            a = pix[x, y][0]
            b = pix[x, y][1]
            c = pix[x, y][2]
            draw.point((x, y), (a + (x - width//2)//3, b + (x - width//2)//3, c + (x - width//2)//3))
                                
image.show()
del draw
