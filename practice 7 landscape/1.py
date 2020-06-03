from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image, ImageDraw

# Процедура инициализации
def init():
	glEnable(GL_DEPTH_TEST)
	glClearColor(1.0, 1.0, 1.0, 1.0)  # Белый цвет для первоначальной закраски
	glMatrixMode(GL_PROJECTION)  # Выбираем матрицу проекций
	glLoadIdentity()  # Сбрасываем все предыдущие трансформации
	gluPerspective(90, window_width / window_height, 0.1, 250)  # Задаем перспективу
	global anglex, angley, anglez, zoom, filled
	anglex = 0
	angley = 0
	anglez = 0
	zoom = 1.0
	filled = 0


# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
	global anglex, angley, anglez, zoom, filled
	if key == b'\x1b':
		sys.exit(0)
	if key == b'w':
		anglex += 5
	if key == b's':
		anglex -= 5
	if key == b'q':
		angley += 5
	if key == b'e':
		angley -= 5
	if key == b'a':
		anglez += 5
	if key == b'd':
		anglez -= 5
	if key == b'-':
		zoom /= 1.1
	if key == b'=':
		zoom *= 1.1
	if key == b' ':
		filled = 1 - filled
	glutPostRedisplay()  # Вызываем процедуру перерисовки


# Процедура рисования
def draw(*args, **kwargs):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очищаем экран и заливаем текущим цветом фона
	#glMatrixMode(GL_MODELVIEW)  # Выбираем модельно-видовую матрицу
	glLoadIdentity()  # Сбрасываем все предыдущие трансформации
	gluLookAt(0, 0, -1,  # Положение камеры
		0, 0, 0,  # Точка, на которую смотрит камера
		0, 1, 0)  # Направление "верх" камеры
	global anglex, angley, anglez, filled, h, width,height
	glRotated(anglex, 1, 0, 0)
	glRotated(angley, 0, 1, 0)
	glRotated(anglez, 0, 0, 1)
	glRotated(-105, 1, 0, 0)

	if filled == 1:
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	else:
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

	glScaled(zoom, zoom, zoom)

	glPushMatrix()
	glRotate(180, 0, 0, -1)
	glTranslate(-1, -1, -0.5)
	glScaled(0.03, 0.03, 0.03)
	for i in range(1, height , 2):
		for j in range(1, width , 2):
			glBegin(GL_TRIANGLE_FAN)
			glColor3f(1, 1, 0.5)
			glVertex3d(i, j, h[i][j]/7)
			glVertex3d(i + 1, j, h[i + 1][j]/7)
			glVertex3d(i + 1, j + 1, h[i + 1][j + 1]/7)
			glVertex3d(i, j + 1, h[i][j + 1]/7)
			glVertex3d(i - 1, j + 1, h[i - 1][j + 1]/7)
			glVertex3d(i - 1, j, h[i - 1][j]/7)
			glVertex3d(i - 1, j - 1, h[i - 1][j - 1]/7)
			glVertex3d(i, j - 1, h[i][j - 1]/7)
			glVertex3d(i + 1, j - 1, h[i + 1][j - 1]/7)
			glVertex3d(i + 1, j, h[i + 1][j]/7)
			glEnd()
	glPopMatrix()

	glutSwapBuffers()  # Меняем буферы
	glutPostRedisplay()  # Вызываем процедуру перерисовки



if __name__ == '__main__':
	window_width = 800
	window_height = 600

	image = Image.open("map.jpg")
	global width, height, h
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	h = []

	for x in range(width):
		h1 = []
		for y in range(height):
			a = pix[x, y]
			h1.append(a)
		h.append(h1)

	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(window_width, window_height)
	glutInitWindowPosition(50, 50)
	glutInit(sys.argv)
	glutCreateWindow(b"OpenGL Second Program!")
	# Определяем процедуру, отвечающую за рисование
	glutDisplayFunc(draw)
	# Определяем процедуру, отвечающую за обработку обычных клавиш
	glutKeyboardFunc(keyboardkeys)
	# Вызываем нашу функцию инициализации
	init()
	glutMainLoop()