from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("1.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

k = height/width

for x in range(width):
        for y in range(height):
            a = pix[x, y][0]
            b = pix[x, y][1]
            c = pix[x, y][2]
            if(x%40 < 20 and y > height//4 and y < (3*height)//4):
                draw.point((x, y), (40, 255 , 40))
            if((x - width//2)**2 + (y - height//2)**2 <= (height//4)**2):
                draw.point((x, y), (255, 128 , 0))
                                
image.show()
del draw
 
