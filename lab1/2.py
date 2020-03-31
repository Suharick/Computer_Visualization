from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("1.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                s = (a + b + c)//3
                if (x < (width//3)):
                    draw.point((x, y), (s, s, 0))
                elif (x >= (width//3) and x < 2*(width//3)):
                    draw.point((x, y), (s, 0, 0))
                elif (x >= 2*(width//3)):
                    draw.point((x, y), (0, s, 0))
                
image.show()
del draw
