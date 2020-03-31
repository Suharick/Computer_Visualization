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
            s = (a + b + c)//3
            if(s >= 189):
                draw.point((x, y), (255, 255, 255))
            elif(s >= 126 and s < 189):
                draw.point((x, y), (170, 170, 170))
            elif(s >= 63 and s < 126):
                draw.point((x, y), (85, 85, 85))
            elif(s < 63):
                draw.point((x, y), (0, 0, 0))            
                                            
image.show()
del draw
 
