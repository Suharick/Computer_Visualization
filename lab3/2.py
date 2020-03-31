from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("1.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

for x in range(width-2):
        for y in range(height-2):
            a = pix[x, y][0]
            b = pix[x, y][1]
            c = pix[x, y][2]
            
            if(a >= 115):
                a = 255
            else:
                a = 0

            if(b >= 115):
                b = 255
            else:
                b = 0
                
            if(c >= 115):
                c = 255
            else:
                c = 0
            
            draw.point((x, y), (a, b, c))
            

                                            
image.show()
del draw
 
