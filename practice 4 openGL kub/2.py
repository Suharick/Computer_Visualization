from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Процедура инициализации
def init():
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.5, 0.5, 0.5, 1.0) # Серый цвет для первоначальной закраски
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
	if key == b'\x1b':
		sys.exit(0)
	glutPostRedisplay()         # Вызываем процедуру перерисовки

# Процедура рисования
def draw(*args, **kwargs):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
	glRotated(0.125,1,1,1)

	glBegin(GL_QUADS)
#1 kub
	glColor3f(1, 0.5, 0.3)
	glVertex3d( -0.3, 0.7, 0.7)
	glVertex3d( -0.3, 0.7, 0.3)
	glVertex3d( -0.3, 0.3, 0.3)
	glVertex3d( -0.3, 0.3, 0.7)
	
	glColor3f(1, 0.5, 0.3)
	glVertex3d( -0.3, 0.7, 0.3)
	glVertex3d( -0.3, 0.3, 0.3)
	glVertex3d( -0.7, 0.3, 0.3)
	glVertex3d( -0.7, 0.7, 0.3)

	glColor3f(1, 0.5, 0.3)
	glVertex3d( -0.7, 0.7, 0.7)
	glVertex3d( -0.7, 0.7, 0.3)
	glVertex3d( -0.7, 0.3, 0.3)
	glVertex3d( -0.7, 0.3, 0.7)
	
	glColor3f(1, 0.5, 0.3)
	glVertex3d( -0.3, 0.7, 0.7)
	glVertex3d( -0.3, 0.3, 0.7)
	glVertex3d( -0.7, 0.3, 0.7)
	glVertex3d( -0.7, 0.7, 0.7)

	glColor3f(1, 0.5, 0.3)
	glVertex3d( -0.3, 0.7, 0.7)
	glVertex3d( -0.3, 0.7, 0.3)
	glVertex3d( -0.7, 0.7, 0.3)
	glVertex3d( -0.7, 0.7, 0.7)
	
	glColor3f(1, 0.5, 0.3)
	glVertex3d( -0.3, 0.3, 0.7)
	glVertex3d( -0.3, 0.3, 0.3)
	glVertex3d( -0.7, 0.3, 0.3)
	glVertex3d( -0.7, 0.3, 0.7)



#2 kub
	glColor3f(1, 1, 0.5)
	glVertex3d( -0.3, 0.7, -0.7)
	glVertex3d( -0.3, 0.7, -0.3)
	glVertex3d( -0.3, 0.3, -0.3)
	glVertex3d( -0.3, 0.3, -0.7)
	
	glColor3f(1, 1, 0.5)
	glVertex3d( -0.3, 0.7, -0.3)
	glVertex3d( -0.3, 0.3, -0.3)
	glVertex3d( -0.7, 0.3, -0.3)
	glVertex3d( -0.7, 0.7, -0.3)

	glColor3f(1, 1, 0.5)
	glVertex3d( -0.7, 0.7, -0.7)
	glVertex3d( -0.7, 0.7, -0.3)
	glVertex3d( -0.7, 0.3, -0.3)
	glVertex3d( -0.7, 0.3, -0.7)
	
	glColor3f(1, 1, 0.5)
	glVertex3d( -0.3, 0.7, -0.7)
	glVertex3d( -0.3, 0.3, -0.7)
	glVertex3d( -0.7, 0.3, -0.7)
	glVertex3d( -0.7, 0.7, -0.7)

	glColor3f(1, 1, 0.5)
	glVertex3d( -0.3, 0.7, -0.7)
	glVertex3d( -0.3, 0.7, -0.3)
	glVertex3d( -0.7, 0.7, -0.3)
	glVertex3d( -0.7, 0.7, -0.7)
	
	glColor3f(1, 1, 0.5)
	glVertex3d( -0.3, 0.3, -0.7)
	glVertex3d( -0.3, 0.3, -0.3)
	glVertex3d( -0.7, 0.3, -0.3)
	glVertex3d( -0.7, 0.3, -0.7)



#3 kub
	glColor3f(1, 0.5, 1)
	glVertex3d( 0.3, 0.7, 0.7)
	glVertex3d( 0.3, 0.7, 0.3)
	glVertex3d( 0.3, 0.3, 0.3)
	glVertex3d( 0.3, 0.3, 0.7)
	
	glColor3f(1, 0.5, 1)
	glVertex3d( 0.3, 0.7, 0.3)
	glVertex3d( 0.3, 0.3, 0.3)
	glVertex3d( 0.7, 0.3, 0.3)
	glVertex3d( 0.7, 0.7, 0.3)

	glColor3f(1, 0.5, 1)
	glVertex3d( 0.7, 0.7, 0.7)
	glVertex3d( 0.7, 0.7, 0.3)
	glVertex3d( 0.7, 0.3, 0.3)
	glVertex3d( 0.7, 0.3, 0.7)
	
	glColor3f(1, 0.5, 1)
	glVertex3d( 0.3, 0.7, 0.7)
	glVertex3d( 0.3, 0.3, 0.7)
	glVertex3d( 0.7, 0.3, 0.7)
	glVertex3d( 0.7, 0.7, 0.7)

	glColor3f(1, 0.5, 1)
	glVertex3d( 0.3, 0.7, 0.7)
	glVertex3d( 0.3, 0.7, 0.3)
	glVertex3d( 0.7, 0.7, 0.3)
	glVertex3d( 0.7, 0.7, 0.7)
	
	glColor3f(1, 0.5, 1)
	glVertex3d( 0.3, 0.3, 0.7)
	glVertex3d( 0.3, 0.3, 0.3)
	glVertex3d( 0.7, 0.3, 0.3)
	glVertex3d( 0.7, 0.3, 0.7)
	


#4 kub
	glColor3f(0.5, 1, 0.5)
	glVertex3d( 0.3, 0.7, -0.7)
	glVertex3d( 0.3, 0.7, -0.3)
	glVertex3d( 0.3, 0.3, -0.3)
	glVertex3d( 0.3, 0.3, -0.7)
	
	glColor3f(0.5, 1, 0.5)
	glVertex3d( 0.3, 0.7, -0.3)
	glVertex3d( 0.3, 0.3, -0.3)
	glVertex3d( 0.7, 0.3, -0.3)
	glVertex3d( 0.7, 0.7, -0.3)

	glColor3f(0.5, 1, 0.5)
	glVertex3d( 0.7, 0.7, -0.7)
	glVertex3d( 0.7, 0.7, -0.3)
	glVertex3d( 0.7, 0.3, -0.3)
	glVertex3d( 0.7, 0.3, -0.7)
	
	glColor3f(0.5, 1, 0.5)
	glVertex3d( 0.3, 0.7, -0.7)
	glVertex3d( 0.3, 0.3, -0.7)
	glVertex3d( 0.7, 0.3, -0.7)
	glVertex3d( 0.7, 0.7, -0.7)

	glColor3f(0.5, 1, 0.5)
	glVertex3d( 0.3, 0.7, -0.7)
	glVertex3d( 0.3, 0.7, -0.3)
	glVertex3d( 0.7, 0.7, -0.3)
	glVertex3d( 0.7, 0.7, -0.7)
	
	glColor3f(0.5, 1, 0.5)
	glVertex3d( 0.3, 0.3, -0.7)
	glVertex3d( 0.3, 0.3, -0.3)
	glVertex3d( 0.7, 0.3, -0.3)
	glVertex3d( 0.7, 0.3, -0.7)



#5 kub
	glColor3f(0.5, 1, 1)
	glVertex3d( 0.3, -0.7, -0.7)
	glVertex3d( 0.3, -0.7, -0.3)
	glVertex3d( 0.3, -0.3, -0.3)
	glVertex3d( 0.3, -0.3, -0.7)
	
	glColor3f(0.5, 1, 1)
	glVertex3d( 0.3, -0.7, -0.3)
	glVertex3d( 0.3, -0.3, -0.3)
	glVertex3d( 0.7, -0.3, -0.3)
	glVertex3d( 0.7, -0.7, -0.3)

	glColor3f(0.5, 1, 1)
	glVertex3d( 0.7, -0.7, -0.7)
	glVertex3d( 0.7, -0.7, -0.3)
	glVertex3d( 0.7, -0.3, -0.3)
	glVertex3d( 0.7, -0.3, -0.7)
	
	glColor3f(0.5, 1, 1)
	glVertex3d( 0.3, -0.7, -0.7)
	glVertex3d( 0.3, -0.3, -0.7)
	glVertex3d( 0.7, -0.3, -0.7)
	glVertex3d( 0.7, -0.7, -0.7)

	glColor3f(0.5, 1, 1)
	glVertex3d( 0.3, -0.7, -0.7)
	glVertex3d( 0.3, -0.7, -0.3)
	glVertex3d( 0.7, -0.7, -0.3)
	glVertex3d( 0.7, -0.7, -0.7)
	
	glColor3f(0.5, 1, 1)
	glVertex3d( 0.3, -0.3, -0.7)
	glVertex3d( 0.3, -0.3, -0.3)
	glVertex3d( 0.7, -0.3, -0.3)
	glVertex3d( 0.7, -0.3, -0.7)
	


#6 kub
	glColor3f(1, 1, 1)
	glVertex3d( 0.3, -0.7, 0.7)
	glVertex3d( 0.3, -0.7, 0.3)
	glVertex3d( 0.3, -0.3, 0.3)
	glVertex3d( 0.3, -0.3, 0.7)
	
	glColor3f(1, 1, 1)
	glVertex3d( 0.3, -0.7, 0.3)
	glVertex3d( 0.3, -0.3, 0.3)
	glVertex3d( 0.7, -0.3, 0.3)
	glVertex3d( 0.7, -0.7, 0.3)

	glColor3f(1, 1, 1)
	glVertex3d( 0.7, -0.7, 0.7)
	glVertex3d( 0.7, -0.7, 0.3)
	glVertex3d( 0.7, -0.3, 0.3)
	glVertex3d( 0.7, -0.3, 0.7)
	
	glColor3f(1, 1, 1)
	glVertex3d( 0.3, -0.7, 0.7)
	glVertex3d( 0.3, -0.3, 0.7)
	glVertex3d( 0.7, -0.3, 0.7)
	glVertex3d( 0.7, -0.7, 0.7)

	glColor3f(1, 1, 1)
	glVertex3d( 0.3, -0.7, 0.7)
	glVertex3d( 0.3, -0.7, 0.3)
	glVertex3d( 0.7, -0.7, 0.3)
	glVertex3d( 0.7, -0.7, 0.7)
	
	glColor3f(1, 1, 1)
	glVertex3d( 0.3, -0.3, 0.7)
	glVertex3d( 0.3, -0.3, 0.3)
	glVertex3d( 0.7, -0.3, 0.3)
	glVertex3d( 0.7, -0.3, 0.7)
	


#7 kub
	glColor3f(0.5, 0.5, 1)
	glVertex3d( -0.3, -0.7, 0.7)
	glVertex3d( -0.3, -0.7, 0.3)
	glVertex3d( -0.3, -0.3, 0.3)
	glVertex3d( -0.3, -0.3, 0.7)
	
	glColor3f(0.5, 0.5, 1)
	glVertex3d( -0.3, -0.7, 0.3)
	glVertex3d( -0.3, -0.3, 0.3)
	glVertex3d( -0.7, -0.3, 0.3)
	glVertex3d( -0.7, -0.7, 0.3)

	glColor3f(0.5, 0.5, 1)
	glVertex3d( -0.7, -0.7, 0.7)
	glVertex3d( -0.7, -0.7, 0.3)
	glVertex3d( -0.7, -0.3, 0.3)
	glVertex3d( -0.7, -0.3, 0.7)
	
	glColor3f(0.5, 0.5, 1)
	glVertex3d( -0.3, -0.7, 0.7)
	glVertex3d( -0.3, -0.3, 0.7)
	glVertex3d( -0.7, -0.3, 0.7)
	glVertex3d( -0.7, -0.7, 0.7)

	glColor3f(0.5, 0.5, 1)
	glVertex3d( -0.3, -0.7, 0.7)
	glVertex3d( -0.3, -0.7, 0.3)
	glVertex3d( -0.7, -0.7, 0.3)
	glVertex3d( -0.7, -0.7, 0.7)
	
	glColor3f(0.5, 0.5, 1)
	glVertex3d( -0.3, -0.3, 0.7)
	glVertex3d( -0.3, -0.3, 0.3)
	glVertex3d( -0.7, -0.3, 0.3)
	glVertex3d( -0.7, -0.3, 0.7)



#8 kub
	glColor3f(1, 0.5, 0.5)
	glVertex3d( -0.3, -0.7, -0.7)
	glVertex3d( -0.3, -0.7, -0.3)
	glVertex3d( -0.3, -0.3, -0.3)
	glVertex3d( -0.3, -0.3, -0.7)
	
	glColor3f(1, 0.5, 0.5)
	glVertex3d( -0.3, -0.7, -0.3)
	glVertex3d( -0.3, -0.3, -0.3)
	glVertex3d( -0.7, -0.3, -0.3)
	glVertex3d( -0.7, -0.7, -0.3)

	glColor3f(1, 0.5, 0.5)
	glVertex3d( -0.7, -0.7, -0.7)
	glVertex3d( -0.7, -0.7, -0.3)
	glVertex3d( -0.7, -0.3, -0.3)
	glVertex3d( -0.7, -0.3, -0.7)
	
	glColor3f(1, 0.5, 0.5)
	glVertex3d( -0.3, -0.7, -0.7)
	glVertex3d( -0.3, -0.3, -0.7)
	glVertex3d( -0.7, -0.3, -0.7)
	glVertex3d( -0.7, -0.7, -0.7)

	glColor3f(1, 0.5, 0.5)
	glVertex3d( -0.3, -0.7, -0.7)
	glVertex3d( -0.3, -0.7, -0.3)
	glVertex3d( -0.7, -0.7, -0.3)
	glVertex3d( -0.7, -0.7, -0.7)
	
	glColor3f(1, 0.5, 0.5)
	glVertex3d( -0.3, -0.3, -0.7)
	glVertex3d( -0.3, -0.3, -0.3)
	glVertex3d( -0.7, -0.3, -0.3)
	glVertex3d( -0.7, -0.3, -0.7)

	

	glEnd()

	glutSwapBuffers()           # Меняем буферы
	glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
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
