from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image1 = Image.open("1.jpg") #Открываем изображение
draw1 = ImageDraw.Draw(image1) #Создаем инструмент для рисования
width1  = image1.size[0] #Определяем ширину 
height1 = image1.size[1] #Определяем высоту 	
pix1 = image1.load() #Выгружаем значения пикселей

image2 = Image.open("2.jpg") #Открываем изображение
draw2 = ImageDraw.Draw(image2) #Создаем инструмент для рисования
width2  = image2.size[0] #Определяем ширину 
height2 = image2.size[1] #Определяем высоту 	
pix2 = image2.load() #Выгружаем значения пикселей

for x in range(width1*2//3, width1):
        for y in range(height1):
            a1 = pix1[x, y][0]
            b1 = pix1[x, y][1]
            c1 = pix1[x, y][2]
            a2 = pix2[x, y][0]
            b2 = pix2[x, y][1]
            c2 = pix2[x, y][2]
            draw1.point((x, y), (a2, b2 , c2))

for x in range(width1//3, width1*2//3):
        for y in range(height1):
            a1 = pix1[x, y][0]
            b1 = pix1[x, y][1]
            c1 = pix1[x, y][2]
            a2 = pix2[x, y][0]
            b2 = pix2[x, y][1]
            c2 = pix2[x, y][2]
            q = (x - width1//3)/(width1*2//3 - width1//3)
            draw1.point((x, y), (round(a2*q + a1*(1-q)), round(b2*q + b1*(1-q)), round(c2*q + c1*(1-q))))
                              
image1.show()
del draw1
del draw2


