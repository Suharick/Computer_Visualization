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
            draw.point((x, y), (255, 255, 255))

def lineP(p1, p2, color):  # рисуем линию из точки p1(x1,y1) в точку p2(x2,y2)
        x1 = p1[0]  # Перекладываем координаты точек в более понятные переменные
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        dX = abs(x2 - x1) # Вычисляем "смещение по X"
        dY = abs(y2 - y1) # Вычисляем "смещение по Y"
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY # "Изменение ошибки"
            y = y1    # текущий Y (начальное значение)
            dirY = sign(y2 - y1) # направление изменения Y
            for x in range(x1, x2 + 1): # перебираем все X от x1 до x2
                    draw.point((x,y),color) # закрашиваем пиксель (x,y)
                    err += dErr             # добавляем "смежение" к "ошибке"
                    if err + err >= dX: # если "ошибка" накопилась
                            y += dirY   # изменяем Y на 1
                            err -= dX   # вычитаем из "ошибки" dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y),color)
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY

def forward(n):
    line([x, y], [], (0, 0, 0))
                                
image.show()
del draw
