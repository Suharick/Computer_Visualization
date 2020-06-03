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
#1 line

#1 kub
	glColor3f(1, 1, 1)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( 0.05, -0.05, 0.05)
	
	glColor3f(1, 1, 1)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.05, 0.05, -0.05)

	glColor3f(1, 1, 1)
	glVertex3d( -0.05, 0.05, 0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, 0.05)
	
	glColor3f(1, 1, 1)
	glVertex3d( -0.05, 0.05, 0.05)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, -0.05, 0.05)
	glVertex3d( -0.05, -0.05, 0.05)

	glColor3f(1, 1, 1)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, 0.05)
	
	glColor3f(1, 1, 1)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, 0.05)



#2 kub
	glColor3f(1, 0.8, 0.8)
	glVertex3d( -0.05, 0.05, 0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, 0.05)
	
	glColor3f(1, 0.8, 0.8)
	glVertex3d( -0.15, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.15, -0.05, -0.05)

	glColor3f(1, 0.8, 0.8)
	glVertex3d( -0.15, 0.05, 0.05)
	glVertex3d( -0.15, 0.05, -0.05)
	glVertex3d( -0.15, -0.05, -0.05)
	glVertex3d( -0.15, -0.05, 0.05)
	
	glColor3f(1, 0.8, 0.8)
	glVertex3d( -0.15, 0.05, 0.05)
	glVertex3d( -0.05, 0.05, 0.05)
	glVertex3d( -0.05, -0.05, 0.05)
	glVertex3d( -0.15, -0.05, 0.05)
	
	glColor3f(1, 0.8, 0.8)
	glVertex3d( -0.15, 0.05, 0.05)
	glVertex3d( -0.05, 0.05, 0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.15, 0.05, -0.05)
	
	glColor3f(1, 0.8, 0.8)
	glVertex3d( -0.15, -0.05, 0.05)
	glVertex3d( -0.05, -0.05, 0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.15, -0.05, -0.05)



#3 kub
	glColor3f(1, 0.6, 0.6)
	glVertex3d( -0.15, 0.05, 0.05)
	glVertex3d( -0.15, 0.05, -0.05)
	glVertex3d( -0.15, -0.05, -0.05)
	glVertex3d( -0.15, -0.05, 0.05)
	
	glColor3f(1, 0.6, 0.6)
	glVertex3d( -0.25, 0.05, -0.05)
	glVertex3d( -0.15, 0.05, -0.05)
	glVertex3d( -0.15, -0.05, -0.05)
	glVertex3d( -0.25, -0.05, -0.05)

	glColor3f(1, 0.6, 0.6)
	glVertex3d( -0.25, 0.05, 0.05)
	glVertex3d( -0.25, 0.05, -0.05)
	glVertex3d( -0.25, -0.05, -0.05)
	glVertex3d( -0.25, -0.05, 0.05)
	
	glColor3f(1, 0.6, 0.6)
	glVertex3d( -0.25, 0.05, 0.05)
	glVertex3d( -0.15, 0.05, 0.05)
	glVertex3d( -0.15, -0.05, 0.05)
	glVertex3d( -0.25, -0.05, 0.05)
	
	glColor3f(1, 0.6, 0.6)
	glVertex3d( -0.25, 0.05, 0.05)
	glVertex3d( -0.15, 0.05, 0.05)
	glVertex3d( -0.15, 0.05, -0.05)
	glVertex3d( -0.25, 0.05, -0.05)
	
	glColor3f(1, 0.6, 0.6)
	glVertex3d( -0.25, -0.05, 0.05)
	glVertex3d( -0.15, -0.05, 0.05)
	glVertex3d( -0.15, -0.05, -0.05)
	glVertex3d( -0.25, -0.05, -0.05)
	


#4 kub
	glColor3f(1, 0.4, 0.4)
	glVertex3d( -0.25, 0.05, 0.05)
	glVertex3d( -0.25, 0.05, -0.05)
	glVertex3d( -0.25, -0.05, -0.05)
	glVertex3d( -0.25, -0.05, 0.05)
	
	glColor3f(1, 0.4, 0.4)
	glVertex3d( -0.35, 0.05, -0.05)
	glVertex3d( -0.25, 0.05, -0.05)
	glVertex3d( -0.25, -0.05, -0.05)
	glVertex3d( -0.35, -0.05, -0.05)

	glColor3f(1, 0.4, 0.4)
	glVertex3d( -0.35, 0.05, 0.05)
	glVertex3d( -0.35, 0.05, -0.05)
	glVertex3d( -0.35, -0.05, -0.05)
	glVertex3d( -0.35, -0.05, 0.05)
	
	glColor3f(1, 0.4, 0.4)
	glVertex3d( -0.35, 0.05, 0.05)
	glVertex3d( -0.25, 0.05, 0.05)
	glVertex3d( -0.25, -0.05, 0.05)
	glVertex3d( -0.35, -0.05, 0.05)
	
	glColor3f(1, 0.4, 0.4)
	glVertex3d( -0.35, 0.05, 0.05)
	glVertex3d( -0.25, 0.05, 0.05)
	glVertex3d( -0.25, 0.05, -0.05)
	glVertex3d( -0.35, 0.05, -0.05)
	
	glColor3f(1, 0.4, 0.4)
	glVertex3d( -0.35, -0.05, 0.05)
	glVertex3d( -0.25, -0.05, 0.05)
	glVertex3d( -0.25, -0.05, -0.05)
	glVertex3d( -0.35, -0.05, -0.05)



#5 kub
	glColor3f(1, 0.2, 0.2)
	glVertex3d( -0.35, 0.05, 0.05)
	glVertex3d( -0.35, 0.05, -0.05)
	glVertex3d( -0.35, -0.05, -0.05)
	glVertex3d( -0.35, -0.05, 0.05)
	
	glColor3f(1, 0.2, 0.2)
	glVertex3d( -0.45, 0.05, -0.05)
	glVertex3d( -0.35, 0.05, -0.05)
	glVertex3d( -0.35, -0.05, -0.05)
	glVertex3d( -0.45, -0.05, -0.05)

	glColor3f(1, 0.2, 0.2)
	glVertex3d( -0.45, 0.05, 0.05)
	glVertex3d( -0.45, 0.05, -0.05)
	glVertex3d( -0.45, -0.05, -0.05)
	glVertex3d( -0.45, -0.05, 0.05)
	
	glColor3f(1, 0.2, 0.2)
	glVertex3d( -0.45, 0.05, 0.05)
	glVertex3d( -0.35, 0.05, 0.05)
	glVertex3d( -0.35, -0.05, 0.05)
	glVertex3d( -0.45, -0.05, 0.05)
	
	glColor3f(1, 0.2, 0.2)
	glVertex3d( -0.45, 0.05, 0.05)
	glVertex3d( -0.35, 0.05, 0.05)
	glVertex3d( -0.35, 0.05, -0.05)
	glVertex3d( -0.45, 0.05, -0.05)

	glColor3f(1, 0.2, 0.2)
	glVertex3d( -0.45, -0.05, 0.05)
	glVertex3d( -0.35, -0.05, 0.05)
	glVertex3d( -0.35, -0.05, -0.05)
	glVertex3d( -0.45, -0.05, -0.05)
	


#6 kub
	glColor3f(1, 0, 0)
	glVertex3d( -0.45, 0.05, 0.05)
	glVertex3d( -0.45, 0.05, -0.05)
	glVertex3d( -0.45, -0.05, -0.05)
	glVertex3d( -0.45, -0.05, 0.05)
	
	glColor3f(1, 0, 0)
	glVertex3d( -0.55, 0.05, -0.05)
	glVertex3d( -0.45, 0.05, -0.05)
	glVertex3d( -0.45, -0.05, -0.05)
	glVertex3d( -0.55, -0.05, -0.05)

	glColor3f(1, 0, 0)
	glVertex3d( -0.55, 0.05, 0.05)
	glVertex3d( -0.55, 0.05, -0.05)
	glVertex3d( -0.55, -0.05, -0.05)
	glVertex3d( -0.55, -0.05, 0.05)
	
	glColor3f(1, 0, 0)
	glVertex3d( -0.55, 0.05, 0.05)
	glVertex3d( -0.45, 0.05, 0.05)
	glVertex3d( -0.45, -0.05, 0.05)
	glVertex3d( -0.55, -0.05, 0.05)
	
	glColor3f(1, 0, 0)
	glVertex3d( -0.55, 0.05, 0.05)
	glVertex3d( -0.45, 0.05, 0.05)
	glVertex3d( -0.45, 0.05, -0.05)
	glVertex3d( -0.55, 0.05, -0.05)

	glColor3f(1, 0, 0)
	glVertex3d( -0.55, -0.05, 0.05)
	glVertex3d( -0.45, -0.05, 0.05)
	glVertex3d( -0.45, -0.05, -0.05)
	glVertex3d( -0.55, -0.05, -0.05)
	


#7 kub
	glColor3f(0.8, 1, 1)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( 0.05, -0.05, 0.05)
	
	glColor3f(0.8, 1, 1)
	glVertex3d( 0.15, 0.05, -0.05)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( 0.15, -0.05, -0.05)

	glColor3f(0.8, 1, 1)
	glVertex3d( 0.15, 0.05, 0.05)
	glVertex3d( 0.15, 0.05, -0.05)
	glVertex3d( 0.15, -0.05, -0.05)
	glVertex3d( 0.15, -0.05, 0.05)
	
	glColor3f(0.8, 1, 1)
	glVertex3d( 0.15, 0.05, 0.05)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, -0.05, 0.05)
	glVertex3d( 0.15, -0.05, 0.05)
	
	glColor3f(0.8, 1, 1)
	glVertex3d( 0.15, 0.05, 0.05)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( 0.15, 0.05, -0.05)
	
	glColor3f(0.8, 1, 1)
	glVertex3d( 0.15, -0.05, 0.05)
	glVertex3d( 0.05, -0.05, 0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( 0.15, -0.05, -0.05)



#8 kub
	glColor3f(0.6, 1, 1)
	glVertex3d( 0.15, 0.05, 0.05)
	glVertex3d( 0.15, 0.05, -0.05)
	glVertex3d( 0.15, -0.05, -0.05)
	glVertex3d( 0.15, -0.05, 0.05)
	
	glColor3f(0.6, 1, 1)
	glVertex3d( 0.25, 0.05, -0.05)
	glVertex3d( 0.15, 0.05, -0.05)
	glVertex3d( 0.15, -0.05, -0.05)
	glVertex3d( 0.25, -0.05, -0.05)

	glColor3f(0.6, 1, 1)
	glVertex3d( 0.25, 0.05, 0.05)
	glVertex3d( 0.25, 0.05, -0.05)
	glVertex3d( 0.25, -0.05, -0.05)
	glVertex3d( 0.25, -0.05, 0.05)
	
	glColor3f(0.6, 1, 1)
	glVertex3d( 0.25, 0.05, 0.05)
	glVertex3d( 0.15, 0.05, 0.05)
	glVertex3d( 0.15, -0.05, 0.05)
	glVertex3d( 0.25, -0.05, 0.05)
	
	glColor3f(0.6, 1, 1)
	glVertex3d( 0.25, 0.05, 0.05)
	glVertex3d( 0.15, 0.05, 0.05)
	glVertex3d( 0.15, 0.05, -0.05)
	glVertex3d( 0.25, 0.05, -0.05)
	
	glColor3f(0.6, 1, 1)
	glVertex3d( 0.25, -0.05, 0.05)
	glVertex3d( 0.15, -0.05, 0.05)
	glVertex3d( 0.15, -0.05, -0.05)
	glVertex3d( 0.25, -0.05, -0.05)
	


#9 kub
	glColor3f(0.4, 1, 1)
	glVertex3d( 0.25, 0.05, 0.05)
	glVertex3d( 0.25, 0.05, -0.05)
	glVertex3d( 0.25, -0.05, -0.05)
	glVertex3d( 0.25, -0.05, 0.05)
	
	glColor3f(0.4, 1, 1)
	glVertex3d( 0.35, 0.05, -0.05)
	glVertex3d( 0.25, 0.05, -0.05)
	glVertex3d( 0.25, -0.05, -0.05)
	glVertex3d( 0.35, -0.05, -0.05)

	glColor3f(0.4, 1, 1)
	glVertex3d( 0.35, 0.05, 0.05)
	glVertex3d( 0.35, 0.05, -0.05)
	glVertex3d( 0.35, -0.05, -0.05)
	glVertex3d( 0.35, -0.05, 0.05)
	
	glColor3f(0.4, 1, 1)
	glVertex3d( 0.35, 0.05, 0.05)
	glVertex3d( 0.25, 0.05, 0.05)
	glVertex3d( 0.25, -0.05, 0.05)
	glVertex3d( 0.35, -0.05, 0.05)
	
	glColor3f(0.4, 1, 1)
	glVertex3d( 0.35, 0.05, 0.05)
	glVertex3d( 0.25, 0.05, 0.05)
	glVertex3d( 0.25, 0.05, -0.05)
	glVertex3d( 0.35, 0.05, -0.05)
	
	glColor3f(0.4, 1, 1)
	glVertex3d( 0.35, -0.05, 0.05)
	glVertex3d( 0.25, -0.05, 0.05)
	glVertex3d( 0.25, -0.05, -0.05)
	glVertex3d( 0.35, -0.05, -0.05)



#10 kub
	glColor3f(0.2, 1, 1)
	glVertex3d( 0.35, 0.05, 0.05)
	glVertex3d( 0.35, 0.05, -0.05)
	glVertex3d( 0.35, -0.05, -0.05)
	glVertex3d( 0.35, -0.05, 0.05)
	
	glColor3f(0.2, 1, 1)
	glVertex3d( 0.45, 0.05, -0.05)
	glVertex3d( 0.35, 0.05, -0.05)
	glVertex3d( 0.35, -0.05, -0.05)
	glVertex3d( 0.45, -0.05, -0.05)

	glColor3f(0.2, 1, 1)
	glVertex3d( 0.45, 0.05, 0.05)
	glVertex3d( 0.45, 0.05, -0.05)
	glVertex3d( 0.45, -0.05, -0.05)
	glVertex3d( 0.45, -0.05, 0.05)
	
	glColor3f(0.2, 1, 1)
	glVertex3d( 0.45, 0.05, 0.05)
	glVertex3d( 0.35, 0.05, 0.05)
	glVertex3d( 0.35, -0.05, 0.05)
	glVertex3d( 0.45, -0.05, 0.05)
	
	glColor3f(0.2, 1, 1)
	glVertex3d( 0.45, 0.05, 0.05)
	glVertex3d( 0.35, 0.05, 0.05)
	glVertex3d( 0.35, 0.05, -0.05)
	glVertex3d( 0.45, 0.05, -0.05)

	glColor3f(0.2, 1, 1)
	glVertex3d( 0.45, -0.05, 0.05)
	glVertex3d( 0.35, -0.05, 0.05)
	glVertex3d( 0.35, -0.05, -0.05)
	glVertex3d( 0.45, -0.05, -0.05)
	


#11 kub
	glColor3f(0, 1, 1)
	glVertex3d( 0.45, 0.05, 0.05)
	glVertex3d( 0.45, 0.05, -0.05)
	glVertex3d( 0.45, -0.05, -0.05)
	glVertex3d( 0.45, -0.05, 0.05)
	
	glColor3f(0, 1, 1)
	glVertex3d( 0.55, 0.05, -0.05)
	glVertex3d( 0.45, 0.05, -0.05)
	glVertex3d( 0.45, -0.05, -0.05)
	glVertex3d( 0.55, -0.05, -0.05)

	glColor3f(0, 1, 1)
	glVertex3d( 0.55, 0.05, 0.05)
	glVertex3d( 0.55, 0.05, -0.05)
	glVertex3d( 0.55, -0.05, -0.05)
	glVertex3d( 0.55, -0.05, 0.05)
	
	glColor3f(0, 1, 1)
	glVertex3d( 0.55, 0.05, 0.05)
	glVertex3d( 0.45, 0.05, 0.05)
	glVertex3d( 0.45, -0.05, 0.05)
	glVertex3d( 0.55, -0.05, 0.05)
	
	glColor3f(0, 1, 1)
	glVertex3d( 0.55, 0.05, 0.05)
	glVertex3d( 0.45, 0.05, 0.05)
	glVertex3d( 0.45, 0.05, -0.05)
	glVertex3d( 0.55, 0.05, -0.05)

	glColor3f(0, 1, 1)
	glVertex3d( 0.55, -0.05, 0.05)
	glVertex3d( 0.45, -0.05, 0.05)
	glVertex3d( 0.45, -0.05, -0.05)
	glVertex3d( 0.55, -0.05, -0.05)

#2 line
	
#2 kub
	glColor3f(0.8, 1, 0.8)
	glVertex3d( 0.05, 0.15, 0.05)
	glVertex3d( 0.05, 0.15, -0.05)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( 0.05, 0.05, 0.05)
	
	glColor3f(0.8, 1, 0.8)
	glVertex3d( 0.05, 0.15, -0.05)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.15, -0.05)

	glColor3f(0.8, 1, 0.8)
	glVertex3d( -0.05, 0.15, 0.05)
	glVertex3d( -0.05, 0.15, -0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, 0.05)
	
	glColor3f(0.8, 1, 0.8)
	glVertex3d( -0.05, 0.15, 0.05)
	glVertex3d( 0.05, 0.15, 0.05)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( -0.05, 0.05, 0.05)
	
	glColor3f(0.8, 1, 0.8)
	glVertex3d( 0.05, 0.15, 0.05)
	glVertex3d( 0.05, 0.15, -0.05)
	glVertex3d( -0.05, 0.15, -0.05)
	glVertex3d( -0.05, 0.15, 0.05)
	
	glColor3f(0.8, 1, 0.8)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, 0.05)



#3 kub
	glColor3f(0.6, 1, 0.6)
	glVertex3d( 0.05, 0.25, 0.05)
	glVertex3d( 0.05, 0.25, -0.05)
	glVertex3d( 0.05, 0.15, -0.05)
	glVertex3d( 0.05, 0.15, 0.05)
	
	glColor3f(0.6, 1, 0.6)
	glVertex3d( 0.05, 0.25, -0.05)
	glVertex3d( 0.05, 0.15, -0.05)
	glVertex3d( -0.05, 0.15, -0.05)
	glVertex3d( -0.05, 0.25, -0.05)

	glColor3f(0.6, 1, 0.6)
	glVertex3d( -0.05, 0.25, 0.05)
	glVertex3d( -0.05, 0.25, -0.05)
	glVertex3d( -0.05, 0.15, -0.05)
	glVertex3d( -0.05, 0.15, 0.05)
	
	glColor3f(0.6, 1, 0.6)
	glVertex3d( -0.05, 0.25, 0.05)
	glVertex3d( 0.05, 0.25, 0.05)
	glVertex3d( 0.05, 0.15, 0.05)
	glVertex3d( -0.05, 0.15, 0.05)
	
	glColor3f(0.6, 1, 0.6)
	glVertex3d( 0.05, 0.25, 0.05)
	glVertex3d( 0.05, 0.25, -0.05)
	glVertex3d( -0.05, 0.25, -0.05)
	glVertex3d( -0.05, 0.25, 0.05)
	
	glColor3f(0.6, 1, 0.6)
	glVertex3d( 0.05, 0.15, 0.05)
	glVertex3d( 0.05, 0.15, -0.05)
	glVertex3d( -0.05, 0.15, -0.05)
	glVertex3d( -0.05, 0.15, 0.05)
	

#4 kub
	glColor3f(0.4, 1, 0.4)
	glVertex3d( 0.05, 0.35, 0.05)
	glVertex3d( 0.05, 0.35, -0.05)
	glVertex3d( 0.05, 0.25, -0.05)
	glVertex3d( 0.05, 0.25, 0.05)
	
	glColor3f(0.4, 1, 0.4)
	glVertex3d( 0.05, 0.35, -0.05)
	glVertex3d( 0.05, 0.25, -0.05)
	glVertex3d( -0.05, 0.25, -0.05)
	glVertex3d( -0.05, 0.35, -0.05)

	glColor3f(0.4, 1, 0.4)
	glVertex3d( -0.05, 0.35, 0.05)
	glVertex3d( -0.05, 0.35, -0.05)
	glVertex3d( -0.05, 0.25, -0.05)
	glVertex3d( -0.05, 0.25, 0.05)
	
	glColor3f(0.4, 1, 0.4)
	glVertex3d( -0.05, 0.35, 0.05)
	glVertex3d( 0.05, 0.35, 0.05)
	glVertex3d( 0.05, 0.25, 0.05)
	glVertex3d( -0.05, 0.25, 0.05)
	
	glColor3f(0.4, 1, 0.4)
	glVertex3d( 0.05, 0.35, 0.05)
	glVertex3d( 0.05, 0.35, -0.05)
	glVertex3d( -0.05, 0.35, -0.05)
	glVertex3d( -0.05, 0.35, 0.05)
	
	glColor3f(0.4, 1, 0.4)
	glVertex3d( 0.05, 0.25, 0.05)
	glVertex3d( 0.05, 0.25, -0.05)
	glVertex3d( -0.05, 0.25, -0.05)
	glVertex3d( -0.05, 0.25, 0.05)



#5 kub
	glColor3f(0.2, 1, 0.2)
	glVertex3d( 0.05, 0.45, 0.05)
	glVertex3d( 0.05, 0.45, -0.05)
	glVertex3d( 0.05, 0.35, -0.05)
	glVertex3d( 0.05, 0.35, 0.05)
	
	glColor3f(0.2, 1, 0.2)
	glVertex3d( 0.05, 0.45, -0.05)
	glVertex3d( 0.05, 0.35, -0.05)
	glVertex3d( -0.05, 0.35, -0.05)
	glVertex3d( -0.05, 0.45, -0.05)

	glColor3f(0.2, 1, 0.2)
	glVertex3d( -0.05, 0.45, 0.05)
	glVertex3d( -0.05, 0.45, -0.05)
	glVertex3d( -0.05, 0.35, -0.05)
	glVertex3d( -0.05, 0.35, 0.05)
	
	glColor3f(0.2, 1, 0.2)
	glVertex3d( -0.05, 0.45, 0.05)
	glVertex3d( 0.05, 0.45, 0.05)
	glVertex3d( 0.05, 0.35, 0.05)
	glVertex3d( -0.05, 0.35, 0.05)
	
	glColor3f(0.2, 1, 0.2)
	glVertex3d( 0.05, 0.45, 0.05)
	glVertex3d( 0.05, 0.45, -0.05)
	glVertex3d( -0.05, 0.45, -0.05)
	glVertex3d( -0.05, 0.45, 0.05)
	
	glColor3f(0.2, 1, 0.2)
	glVertex3d( 0.05, 0.35, 0.05)
	glVertex3d( 0.05, 0.35, -0.05)
	glVertex3d( -0.05, 0.35, -0.05)
	glVertex3d( -0.05, 0.35, 0.05)
	


#6 kub
	glColor3f(0, 1, 0)
	glVertex3d( 0.05, 0.55, 0.05)
	glVertex3d( 0.05, 0.55, -0.05)
	glVertex3d( 0.05, 0.45, -0.05)
	glVertex3d( 0.05, 0.45, 0.05)
	
	glColor3f(0, 1, 0)
	glVertex3d( 0.05, 0.55, -0.05)
	glVertex3d( 0.05, 0.45, -0.05)
	glVertex3d( -0.05, 0.45, -0.05)
	glVertex3d( -0.05, 0.55, -0.05)

	glColor3f(0, 1, 0)
	glVertex3d( -0.05, 0.55, 0.05)
	glVertex3d( -0.05, 0.55, -0.05)
	glVertex3d( -0.05, 0.45, -0.05)
	glVertex3d( -0.05, 0.45, 0.05)
	
	glColor3f(0, 1, 0)
	glVertex3d( -0.05, 0.55, 0.05)
	glVertex3d( 0.05, 0.55, 0.05)
	glVertex3d( 0.05, 0.45, 0.05)
	glVertex3d( -0.05, 0.45, 0.05)
	
	glColor3f(0, 1, 0)
	glVertex3d( 0.05, 0.55, 0.05)
	glVertex3d( 0.05, 0.55, -0.05)
	glVertex3d( -0.05, 0.55, -0.05)
	glVertex3d( -0.05, 0.55, 0.05)
	
	glColor3f(0, 1, 0)
	glVertex3d( 0.05, 0.45, 0.05)
	glVertex3d( 0.05, 0.45, -0.05)
	glVertex3d( -0.05, 0.45, -0.05)
	glVertex3d( -0.05, 0.45, 0.05)
	


#7 kub
	glColor3f(1, 0.8, 1)
	glVertex3d( 0.05, -0.15, 0.05)
	glVertex3d( 0.05, -0.15, -0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( 0.05, -0.05, 0.05)
	
	glColor3f(1, 0.8, 1)
	glVertex3d( 0.05, -0.15, -0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.15, -0.05)

	glColor3f(1, 0.8, 1)
	glVertex3d( -0.05, -0.15, 0.05)
	glVertex3d( -0.05, -0.15, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, 0.05)
	
	glColor3f(1, 0.8, 1)
	glVertex3d( -0.05, -0.15, 0.05)
	glVertex3d( 0.05, -0.15, 0.05)
	glVertex3d( 0.05, -0.05, 0.05)
	glVertex3d( -0.05, -0.05, 0.05)
	
	glColor3f(1, 0.8, 1)
	glVertex3d( 0.05, -0.15, 0.05)
	glVertex3d( 0.05, -0.15, -0.05)
	glVertex3d( -0.05, -0.15, -0.05)
	glVertex3d( -0.05, -0.15, 0.05)
	
	glColor3f(1, 0.8, 1)
	glVertex3d( 0.05, -0.05, 0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, 0.05)



#8 kub
	glColor3f(1, 0.6, 1)
	glVertex3d( 0.05, -0.25, 0.05)
	glVertex3d( 0.05, -0.25, -0.05)
	glVertex3d( 0.05, -0.15, -0.05)
	glVertex3d( 0.05, -0.15, 0.05)
	
	glColor3f(1, 0.6, 1)
	glVertex3d( 0.05, -0.25, -0.05)
	glVertex3d( 0.05, -0.15, -0.05)
	glVertex3d( -0.05, -0.15, -0.05)
	glVertex3d( -0.05, -0.25, -0.05)

	glColor3f(1, 0.6, 1)
	glVertex3d( -0.05, -0.25, 0.05)
	glVertex3d( -0.05, -0.25, -0.05)
	glVertex3d( -0.05, -0.15, -0.05)
	glVertex3d( -0.05, -0.15, 0.05)
	
	glColor3f(1, 0.6, 1)
	glVertex3d( -0.05, -0.25, 0.05)
	glVertex3d( 0.05, -0.25, 0.05)
	glVertex3d( 0.05, -0.15, 0.05)
	glVertex3d( -0.05, -0.15, 0.05)
	
	glColor3f(1, 0.6, 1)
	glVertex3d( 0.05, -0.25, 0.05)
	glVertex3d( 0.05, -0.25, -0.05)
	glVertex3d( -0.05, -0.25, -0.05)
	glVertex3d( -0.05, -0.25, 0.05)
	
	glColor3f(1, 0.6, 1)
	glVertex3d( 0.05, -0.15, 0.05)
	glVertex3d( 0.05, -0.15, -0.05)
	glVertex3d( -0.05, -0.15, -0.05)
	glVertex3d( -0.05, -0.15, 0.05)
	

#9 kub
	glColor3f(1, 0.4, 1)
	glVertex3d( 0.05, -0.35, 0.05)
	glVertex3d( 0.05, -0.35, -0.05)
	glVertex3d( 0.05, -0.25, -0.05)
	glVertex3d( 0.05, -0.25, 0.05)
	
	glColor3f(1, 0.4, 1)
	glVertex3d( 0.05, -0.35, -0.05)
	glVertex3d( 0.05, -0.25, -0.05)
	glVertex3d( -0.05, -0.25, -0.05)
	glVertex3d( -0.05, -0.35, -0.05)

	glColor3f(1, 0.4, 1)
	glVertex3d( -0.05, -0.35, 0.05)
	glVertex3d( -0.05, -0.35, -0.05)
	glVertex3d( -0.05, -0.25, -0.05)
	glVertex3d( -0.05, -0.25, 0.05)
	
	glColor3f(1, 0.4, 1)
	glVertex3d( -0.05, -0.35, 0.05)
	glVertex3d( 0.05, -0.35, 0.05)
	glVertex3d( 0.05, -0.25, 0.05)
	glVertex3d( -0.05, -0.25, 0.05)
	
	glColor3f(1, 0.4, 1)
	glVertex3d( 0.05, -0.35, 0.05)
	glVertex3d( 0.05, -0.35, -0.05)
	glVertex3d( -0.05, -0.35, -0.05)
	glVertex3d( -0.05, -0.35, 0.05)
	
	glColor3f(1, 0.4, 1)
	glVertex3d( 0.05, -0.25, 0.05)
	glVertex3d( 0.05, -0.25, -0.05)
	glVertex3d( -0.05, -0.25, -0.05)
	glVertex3d( -0.05, -0.25, 0.05)



#10 kub
	glColor3f(1, 0.2, 1)
	glVertex3d( 0.05, -0.45, 0.05)
	glVertex3d( 0.05, -0.45, -0.05)
	glVertex3d( 0.05, -0.35, -0.05)
	glVertex3d( 0.05, -0.35, 0.05)
	
	glColor3f(1, 0.2, 1)
	glVertex3d( 0.05, -0.45, -0.05)
	glVertex3d( 0.05, -0.35, -0.05)
	glVertex3d( -0.05, -0.35, -0.05)
	glVertex3d( -0.05, -0.45, -0.05)

	glColor3f(1, 0.2, 1)
	glVertex3d( -0.05, -0.45, 0.05)
	glVertex3d( -0.05, -0.45, -0.05)
	glVertex3d( -0.05, -0.35, -0.05)
	glVertex3d( -0.05, -0.35, 0.05)
	
	glColor3f(1, 0.2, 1)
	glVertex3d( -0.05, -0.45, 0.05)
	glVertex3d( 0.05, -0.45, 0.05)
	glVertex3d( 0.05, -0.35, 0.05)
	glVertex3d( -0.05, -0.35, 0.05)
	
	glColor3f(1, 0.2, 1)
	glVertex3d( 0.05, -0.45, 0.05)
	glVertex3d( 0.05, -0.45, -0.05)
	glVertex3d( -0.05, -0.45, -0.05)
	glVertex3d( -0.05, -0.45, 0.05)
	
	glColor3f(1, 0.2, 1)
	glVertex3d( 0.05, -0.35, 0.05)
	glVertex3d( 0.05, -0.35, -0.05)
	glVertex3d( -0.05, -0.35, -0.05)
	glVertex3d( -0.05, -0.35, 0.05)
	


#11 kub
	glColor3f(1, 0, 1)
	glVertex3d( 0.05, -0.55, 0.05)
	glVertex3d( 0.05, -0.55, -0.05)
	glVertex3d( 0.05, -0.45, -0.05)
	glVertex3d( 0.05, -0.45, 0.05)
	
	glColor3f(1, 0, 1)
	glVertex3d( 0.05, -0.55, -0.05)
	glVertex3d( 0.05, -0.45, -0.05)
	glVertex3d( -0.05, -0.45, -0.05)
	glVertex3d( -0.05, -0.55, -0.05)

	glColor3f(1, 0, 1)
	glVertex3d( -0.05, -0.55, 0.05)
	glVertex3d( -0.05, -0.55, -0.05)
	glVertex3d( -0.05, -0.45, -0.05)
	glVertex3d( -0.05, -0.45, 0.05)
	
	glColor3f(1, 0, 1)
	glVertex3d( -0.05, -0.55, 0.05)
	glVertex3d( 0.05, -0.55, 0.05)
	glVertex3d( 0.05, -0.45, 0.05)
	glVertex3d( -0.05, -0.45, 0.05)
	
	glColor3f(1, 0, 1)
	glVertex3d( 0.05, -0.55, 0.05)
	glVertex3d( 0.05, -0.55, -0.05)
	glVertex3d( -0.05, -0.55, -0.05)
	glVertex3d( -0.05, -0.55, 0.05)
	
	glColor3f(1, 0, 1)
	glVertex3d( 0.05, -0.45, 0.05)
	glVertex3d( 0.05, -0.45, -0.05)
	glVertex3d( -0.05, -0.45, -0.05)
	glVertex3d( -0.05, -0.45, 0.05)

#3 line

#2 kub
	glColor3f(0.8, 0.8, 1)
	glVertex3d( 0.05, 0.05, 0.15)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, -0.05, 0.05)
	glVertex3d( 0.05, -0.05, 0.15)
	
	glColor3f(0.8, 0.8, 1)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( 0.05, -0.05, 0.05)
	glVertex3d( -0.05, -0.05, 0.05)
	glVertex3d( -0.05, 0.05, 0.05)

	glColor3f(0.8, 0.8, 1)
	glVertex3d( -0.05, 0.05, 0.15)
	glVertex3d( -0.05, 0.05, 0.05)
	glVertex3d( -0.05, -0.05, 0.05)
	glVertex3d( -0.05, -0.05, 0.15)
	
	glColor3f(0.8, 0.8, 1)
	glVertex3d( -0.05, 0.05, 0.15)
	glVertex3d( 0.05, 0.05, 0.15)
	glVertex3d( 0.05, -0.05, 0.15)
	glVertex3d( -0.05, -0.05, 0.15)
	
	glColor3f(0.8, 0.8, 1)
	glVertex3d( 0.05, 0.05, 0.15)
	glVertex3d( 0.05, 0.05, 0.05)
	glVertex3d( -0.05, 0.05, 0.05)
	glVertex3d( -0.05, 0.05, 0.15)
	
	glColor3f(0.8, 0.8, 1)
	glVertex3d( 0.05, -0.05, 0.15)
	glVertex3d( 0.05, -0.05, 0.05)
	glVertex3d( -0.05, -0.05, 0.05)
	glVertex3d( -0.05, -0.05, 0.15)



#3 kub
	glColor3f(0.6, 0.6, 1)
	glVertex3d( 0.05, 0.05, 0.25)
	glVertex3d( 0.05, 0.05, 0.15)
	glVertex3d( 0.05, -0.05, 0.15)
	glVertex3d( 0.05, -0.05, 0.25)
	
	glColor3f(0.6, 0.6, 1)
	glVertex3d( 0.05, 0.05, 0.15)
	glVertex3d( 0.05, -0.05, 0.15)
	glVertex3d( -0.05, -0.05, 0.15)
	glVertex3d( -0.05, 0.05, 0.15)

	glColor3f(0.6, 0.6, 1)
	glVertex3d( -0.05, 0.05, 0.25)
	glVertex3d( -0.05, 0.05, 0.15)
	glVertex3d( -0.05, -0.05, 0.15)
	glVertex3d( -0.05, -0.05, 0.25)
	
	glColor3f(0.6, 0.6, 1)
	glVertex3d( -0.05, 0.05, 0.25)
	glVertex3d( 0.05, 0.05, 0.25)
	glVertex3d( 0.05, -0.05, 0.25)
	glVertex3d( -0.05, -0.05, 0.25)
	
	glColor3f(0.6, 0.6, 1)
	glVertex3d( 0.05, 0.05, 0.25)
	glVertex3d( 0.05, 0.05, 0.15)
	glVertex3d( -0.05, 0.05, 0.15)
	glVertex3d( -0.05, 0.05, 0.25)
	
	glColor3f(0.6, 0.6, 1)
	glVertex3d( 0.05, -0.05, 0.25)
	glVertex3d( 0.05, -0.05, 0.15)
	glVertex3d( -0.05, -0.05, 0.15)
	glVertex3d( -0.05, -0.05, 0.25)
	

#4 kub
	glColor3f(0.4, 0.4, 1)
	glVertex3d( 0.05, 0.05, 0.35)
	glVertex3d( 0.05, 0.05, 0.25)
	glVertex3d( 0.05, -0.05, 0.25)
	glVertex3d( 0.05, -0.05, 0.35)
	
	glColor3f(0.4, 0.4, 1)
	glVertex3d( 0.05, 0.05, 0.25)
	glVertex3d( 0.05, -0.05, 0.25)
	glVertex3d( -0.05, -0.05, 0.25)
	glVertex3d( -0.05, 0.05, 0.25)

	glColor3f(0.4, 0.4, 1)
	glVertex3d( -0.05, 0.05, 0.35)
	glVertex3d( -0.05, 0.05, 0.25)
	glVertex3d( -0.05, -0.05, 0.25)
	glVertex3d( -0.05, -0.05, 0.35)
	
	glColor3f(0.4, 0.4, 1)
	glVertex3d( -0.05, 0.05, 0.35)
	glVertex3d( 0.05, 0.05, 0.35)
	glVertex3d( 0.05, -0.05, 0.35)
	glVertex3d( -0.05, -0.05, 0.35)
	
	glColor3f(0.4, 0.4, 1)
	glVertex3d( 0.05, 0.05, 0.35)
	glVertex3d( 0.05, 0.05, 0.25)
	glVertex3d( -0.05, 0.05, 0.25)
	glVertex3d( -0.05, 0.05, 0.35)
	
	glColor3f(0.4, 0.4, 1)
	glVertex3d( 0.05, -0.05, 0.35)
	glVertex3d( 0.05, -0.05, 0.25)
	glVertex3d( -0.05, -0.05, 0.25)
	glVertex3d( -0.05, -0.05, 0.35)



#5 kub
	glColor3f(0.2, 0.2, 1)
	glVertex3d( 0.05, 0.05, 0.45)
	glVertex3d( 0.05, 0.05, 0.35)
	glVertex3d( 0.05, -0.05, 0.35)
	glVertex3d( 0.05, -0.05, 0.45)
	
	glColor3f(0.2, 0.2, 1)
	glVertex3d( 0.05, 0.05, 0.35)
	glVertex3d( 0.05, -0.05, 0.35)
	glVertex3d( -0.05, -0.05, 0.35)
	glVertex3d( -0.05, 0.05, 0.35)

	glColor3f(0.2, 0.2, 1)
	glVertex3d( -0.05, 0.05, 0.45)
	glVertex3d( -0.05, 0.05, 0.35)
	glVertex3d( -0.05, -0.05, 0.35)
	glVertex3d( -0.05, -0.05, 0.45)
	
	glColor3f(0.2, 0.2, 1)
	glVertex3d( -0.05, 0.05, 0.45)
	glVertex3d( 0.05, 0.05, 0.45)
	glVertex3d( 0.05, -0.05, 0.45)
	glVertex3d( -0.05, -0.05, 0.45)
	
	glColor3f(0.2, 0.2, 1)
	glVertex3d( 0.05, 0.05, 0.45)
	glVertex3d( 0.05, 0.05, 0.35)
	glVertex3d( -0.05, 0.05, 0.35)
	glVertex3d( -0.05, 0.05, 0.45)
	
	glColor3f(0.2, 0.2, 1)
	glVertex3d( 0.05, -0.05, 0.45)
	glVertex3d( 0.05, -0.05, 0.35)
	glVertex3d( -0.05, -0.05, 0.35)
	glVertex3d( -0.05, -0.05, 0.45)
	


#6 kub
	glColor3f(0, 0, 1)
	glVertex3d( 0.05, 0.05, 0.55)
	glVertex3d( 0.05, 0.05, 0.45)
	glVertex3d( 0.05, -0.05, 0.45)
	glVertex3d( 0.05, -0.05, 0.55)
	
	glColor3f(0, 0, 1)
	glVertex3d( 0.05, 0.05, 0.45)
	glVertex3d( 0.05, -0.05, 0.45)
	glVertex3d( -0.05, -0.05, 0.45)
	glVertex3d( -0.05, 0.05, 0.45)

	glColor3f(0, 0, 1)
	glVertex3d( -0.05, 0.05, 0.55)
	glVertex3d( -0.05, 0.05, 0.45)
	glVertex3d( -0.05, -0.05, 0.45)
	glVertex3d( -0.05, -0.05, 0.55)
	
	glColor3f(0, 0, 1)
	glVertex3d( -0.05, 0.05, 0.55)
	glVertex3d( 0.05, 0.05, 0.55)
	glVertex3d( 0.05, -0.05, 0.55)
	glVertex3d( -0.05, -0.05, 0.55)
	
	glColor3f(0, 0, 1)
	glVertex3d( 0.05, 0.05, 0.55)
	glVertex3d( 0.05, 0.05, 0.45)
	glVertex3d( -0.05, 0.05, 0.45)
	glVertex3d( -0.05, 0.05, 0.55)
	
	glColor3f(0, 0, 1)
	glVertex3d( 0.05, -0.05, 0.55)
	glVertex3d( 0.05, -0.05, 0.45)
	glVertex3d( -0.05, -0.05, 0.45)
	glVertex3d( -0.05, -0.05, 0.55)
	


#7 kub
	glColor3f(1, 1, 0.8)
	glVertex3d( 0.05, 0.05, -0.15)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( 0.05, -0.05, -0.15)
	
	glColor3f(1, 1, 0.8)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.05, 0.05, -0.05)

	glColor3f(1, 1, 0.8)
	glVertex3d( -0.05, 0.05, -0.15)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.15)
	
	glColor3f(1, 1, 0.8)
	glVertex3d( -0.05, 0.05, -0.15)
	glVertex3d( 0.05, 0.05, -0.15)
	glVertex3d( 0.05, -0.05, -0.15)
	glVertex3d( -0.05, -0.05, -0.15)
	
	glColor3f(1, 1, 0.8)
	glVertex3d( 0.05, 0.05, -0.15)
	glVertex3d( 0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, -0.05)
	glVertex3d( -0.05, 0.05, -0.15)
	
	glColor3f(1, 1, 0.8)
	glVertex3d( 0.05, -0.05, -0.15)
	glVertex3d( 0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.05)
	glVertex3d( -0.05, -0.05, -0.15)



#8 kub
	glColor3f(1, 1, 0.6)
	glVertex3d( 0.05, 0.05, -0.25)
	glVertex3d( 0.05, 0.05, -0.15)
	glVertex3d( 0.05, -0.05, -0.15)
	glVertex3d( 0.05, -0.05, -0.25)
	
	glColor3f(1, 1, 0.6)
	glVertex3d( 0.05, 0.05, -0.15)
	glVertex3d( 0.05, -0.05, -0.15)
	glVertex3d( -0.05, -0.05, -0.15)
	glVertex3d( -0.05, 0.05, -0.15)

	glColor3f(1, 1, 0.6)
	glVertex3d( -0.05, 0.05, -0.25)
	glVertex3d( -0.05, 0.05, -0.15)
	glVertex3d( -0.05, -0.05, -0.15)
	glVertex3d( -0.05, -0.05, -0.25)
	
	glColor3f(1, 1, 0.6)
	glVertex3d( -0.05, 0.05, -0.25)
	glVertex3d( 0.05, 0.05, -0.25)
	glVertex3d( 0.05, -0.05, -0.25)
	glVertex3d( -0.05, -0.05, -0.25)
	
	glColor3f(1, 1, 0.6)
	glVertex3d( 0.05, 0.05, -0.25)
	glVertex3d( 0.05, 0.05, -0.15)
	glVertex3d( -0.05, 0.05, -0.15)
	glVertex3d( -0.05, 0.05, -0.25)
	
	glColor3f(1, 1, 0.6)
	glVertex3d( 0.05, -0.05, -0.25)
	glVertex3d( 0.05, -0.05, -0.15)
	glVertex3d( -0.05, -0.05, -0.15)
	glVertex3d( -0.05, -0.05, -0.25)
	

#9 kub
	glColor3f(1, 1, 0.4)
	glVertex3d( 0.05, 0.05, -0.35)
	glVertex3d( 0.05, 0.05, -0.25)
	glVertex3d( 0.05, -0.05, -0.25)
	glVertex3d( 0.05, -0.05, -0.35)
	
	glColor3f(1, 1, 0.4)
	glVertex3d( 0.05, 0.05, -0.25)
	glVertex3d( 0.05, -0.05, -0.25)
	glVertex3d( -0.05, -0.05, -0.25)
	glVertex3d( -0.05, 0.05, -0.25)

	glColor3f(1, 1, 0.4)
	glVertex3d( -0.05, 0.05, -0.35)
	glVertex3d( -0.05, 0.05, -0.25)
	glVertex3d( -0.05, -0.05, -0.25)
	glVertex3d( -0.05, -0.05, -0.35)
	
	glColor3f(1, 1, 0.4)
	glVertex3d( -0.05, 0.05, -0.35)
	glVertex3d( 0.05, 0.05, -0.35)
	glVertex3d( 0.05, -0.05, -0.35)
	glVertex3d( -0.05, -0.05, -0.35)
	
	glColor3f(1, 1, 0.4)
	glVertex3d( 0.05, 0.05, -0.35)
	glVertex3d( 0.05, 0.05, -0.25)
	glVertex3d( -0.05, 0.05, -0.25)
	glVertex3d( -0.05, 0.05, -0.35)
	
	glColor3f(1, 1, 0.4)
	glVertex3d( 0.05, -0.05, -0.35)
	glVertex3d( 0.05, -0.05, -0.25)
	glVertex3d( -0.05, -0.05, -0.25)
	glVertex3d( -0.05, -0.05, -0.35)



#10 kub
	glColor3f(1, 1, 0.2)
	glVertex3d( 0.05, 0.05, -0.45)
	glVertex3d( 0.05, 0.05, -0.35)
	glVertex3d( 0.05, -0.05, -0.35)
	glVertex3d( 0.05, -0.05, -0.45)
	
	glColor3f(1, 1, 0.2)
	glVertex3d( 0.05, 0.05, -0.35)
	glVertex3d( 0.05, -0.05, -0.35)
	glVertex3d( -0.05, -0.05, -0.35)
	glVertex3d( -0.05, 0.05, -0.35)

	glColor3f(1, 1, 0.2)
	glVertex3d( -0.05, 0.05, -0.45)
	glVertex3d( -0.05, 0.05, -0.35)
	glVertex3d( -0.05, -0.05, -0.35)
	glVertex3d( -0.05, -0.05, -0.45)
	
	glColor3f(1, 1, 0.2)
	glVertex3d( -0.05, 0.05, -0.45)
	glVertex3d( 0.05, 0.05, -0.45)
	glVertex3d( 0.05, -0.05, -0.45)
	glVertex3d( -0.05, -0.05, -0.45)
	
	glColor3f(1, 1, 0.2)
	glVertex3d( 0.05, 0.05, -0.45)
	glVertex3d( 0.05, 0.05, -0.35)
	glVertex3d( -0.05, 0.05, -0.35)
	glVertex3d( -0.05, 0.05, -0.45)
	
	glColor3f(1, 1, 0.2)
	glVertex3d( 0.05, -0.05, -0.45)
	glVertex3d( 0.05, -0.05, -0.35)
	glVertex3d( -0.05, -0.05, -0.35)
	glVertex3d( -0.05, -0.05, -0.45)
	


#11 kub
	glColor3f(1, 1, 0)
	glVertex3d( 0.05, 0.05, -0.55)
	glVertex3d( 0.05, 0.05, -0.45)
	glVertex3d( 0.05, -0.05, -0.45)
	glVertex3d( 0.05, -0.05, -0.55)
	
	glColor3f(1, 1, 0)
	glVertex3d( 0.05, 0.05, -0.45)
	glVertex3d( 0.05, -0.05, -0.45)
	glVertex3d( -0.05, -0.05, -0.45)
	glVertex3d( -0.05, 0.05, -0.45)

	glColor3f(1, 1, 0)
	glVertex3d( -0.05, 0.05, -0.55)
	glVertex3d( -0.05, 0.05, -0.45)
	glVertex3d( -0.05, -0.05, -0.45)
	glVertex3d( -0.05, -0.05, -0.55)
	
	glColor3f(1, 1, 0)
	glVertex3d( -0.05, 0.05, -0.55)
	glVertex3d( 0.05, 0.05, -0.55)
	glVertex3d( 0.05, -0.05, -0.55)
	glVertex3d( -0.05, -0.05, -0.55)
	
	glColor3f(1, 1, 0)
	glVertex3d( 0.05, 0.05, -0.55)
	glVertex3d( 0.05, 0.05, -0.45)
	glVertex3d( -0.05, 0.05, -0.45)
	glVertex3d( -0.05, 0.05, -0.55)
	
	glColor3f(1, 1, 0)
	glVertex3d( 0.05, -0.05, -0.55)
	glVertex3d( 0.05, -0.05, -0.45)
	glVertex3d( -0.05, -0.05, -0.45)
	glVertex3d( -0.05, -0.05, -0.55)
	

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
