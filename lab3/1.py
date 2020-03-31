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
            
            a1 = pix[x+1, y][0]
            b1 = pix[x+1, y][1]
            c1 = pix[x+1, y][2]
            
            s = (a+b+c)//3
            s1 = (a1+b1+c1)//3
            draw.point((x, y), (128 + 2*(s - s1), 128 + 2*(s - s1),128 + 2*(s - s1)))
                                                        
image.show()
del draw
 
