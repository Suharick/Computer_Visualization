from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Процедура инициализации
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.5, 0.5, 1.0) # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
    global filled
    filled = 1

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
    global filled
    if key == b'\x1b':
        sys.exit(0)
    if key == b' ':
        filled = 1 - filled
    glutPostRedisplay()         # Вызываем процедуру перерисовки

# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
    glRotated(0.125,1,1,1)
    global filled
    if filled == 1:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    R1 = 0.5

    glBegin(GL_QUAD_STRIP)
    glColor3d(0, 0, 1)
    for i in range(25):
        glVertex3d(R1*cos(2*pi*i/24) , R1*sin(2*pi*i/24) , 0.05/2)
        glVertex3d(R1*cos(2*pi*i/24) , R1*sin(2*pi*i/24) , -0.05/2)
    glEnd()


    glBegin(GL_QUAD_STRIP)
    glColor3d(0, 0, 1)
    for j in range(1,11):
        for i in range(25):
            glVertex3d((sqrt(abs(R1**2 - (0.05*(j - 1))**2)))*cos(2*pi*i/24), (sqrt(abs(R1**2 - (0.05*(j - 1))**2)))*sin(2*pi*i/24), 0.05/2 + (j-1)*0.05)
            glVertex3d((sqrt(abs(R1**2 - (0.05*j)**2)))*cos(2*pi*i/24), (sqrt(abs(R1**2 - (0.05*j)**2)))*sin(2*pi*i/24), 0.05/2 + j*0.05)
    glEnd()
    

    glBegin(GL_QUAD_STRIP)
    glColor3d(1, 1, 0)
    for j in range(1,9):
        for i in range(25):
            glVertex3d((sqrt(abs(R1**2 - (0.05*(j - 1))**2)))*cos(2*pi*i/24), (sqrt(abs(R1**2 - (0.05*(j - 1))**2)))*sin(2*pi*i/24), -0.035/2 - (j-1)*0.035)
            glVertex3d((sqrt(abs(R1**2 - (0.05*j)**2)))*cos(2*pi*i/24), (sqrt(abs(R1**2 - (0.05*j)**2)))*sin(2*pi*i/24), -0.035/2 - j*0.035)
    glEnd()

    minr = sqrt(R1**2 - (10*((0.5 - 0.05)/11))**2)

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 1, 0.5)
    glVertex3d( 0,  0, -0.9)
    for i in range(25):
	    glVertex3d(minr*cos(2*pi*i/24), minr*sin(2*pi*i/24), -0.9)
    glEnd()

    
    glBegin(GL_QUAD_STRIP)
    glColor3f(0.5, 1, 0.5)
    for i in range(25):
        glVertex3d(minr*cos(2*pi*i/24),minr*sin(2*pi*i/24), -0.9)
        glVertex3d(minr*cos(2*pi*i/24),minr*sin(2*pi*i/24), -7.25*((0.5 - 0.05)/11))
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
