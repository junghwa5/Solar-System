#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math


# In[ ]:


ESCAPE = b'\x1b'
window = 0

day1, day2, day3, day4, day5, day6, day7, day8 = 0, 0, 0, 0, 0, 0, 0, 0
time1, time2, time3, time4, time5, time6, time7, time8 = 0, 0, 0, 0, 0, 0, 0, 0
num = 5

sunRadius = 0.075


# In[ ]:


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


# In[ ]:


def drawSquare(v): # 사각형 그리기
    glBegin(GL_POLYGON)
    glVertex2f(-v, -v)
    glVertex2f(v, -v)
    glVertex2f(v, v)
    glVertex2f(-v, v)
    glEnd()
    glFinish()


# In[ ]:


def drawMercury(): # 수성 그리기
    global day1
    global time1
    
    glPushMatrix()
    # 공전
    glRotatef(day1, 0.0, 0.0, 1.0)
    glTranslatef(0.135, 0.0, 0.0)
    # 자전
    glRotatef(time1, 0.0, 0.0, 1.0)
    glColor3f(210.0/255.0, 155.0/255.0, 90.0/255.0)
    drawSquare(0.017)
    
    glPopMatrix()


# In[ ]:


def drawVenus(): #금성 그리기
    global day2
    global time2
    
    glPushMatrix()
    # 공전
    glRotatef(day2, 0.0, 0.0, 1.0)
    glTranslatef(0.189, 0.0, 0.0)
    # 자전
    glRotatef(time2, 0.0, 0.0, 1.0)
    glColor3f(235.0/255.0, 220.0/255.0, 90.0/255.0)
    drawSquare(0.023)
    
    glPopMatrix()


# In[ ]:


def drawEarth(): # 지구 그리기
    global day3
    global time3
    
    glPushMatrix()
    # 공전
    glRotatef(day3, 0.0, 0.0, 1.0)
    glTranslatef(0.27, 0.0, 0.0)
    # 자전
    glRotatef(time3, 0.0, 0.0, 1.0)
    glColor3f(90.0/255.0, 130.0/255.0, 230.0/255.0)
    drawSquare(0.033)
    
    glPopMatrix()


# In[ ]:


def drawMars(): #화성 그리기
    global day4
    global time4
    
    glPushMatrix()
    # 공전
    glRotatef(day4, 0.0, 0.0, 1.0)
    glTranslatef(0.324, 0.0, 0.0)
    # 자전
    glRotatef(time4, 0.0, 0.0, 1.0)
    glColor3f(180.0/255.0, 90.0/255.0, 35.0/255.0)
    drawSquare(0.019)
    
    glPopMatrix()


# In[ ]:


def drawJupiter(): #목성 그리기
    global day5
    global time5
    
    glPushMatrix()
    # 공전
    glRotatef(day5, 0.0, 0.0, 1.0)
    glTranslatef(0.459, 0.0, 0.0)
    # 자전
    glRotatef(time5, 0.0, 0.0, 1.0)
    glColor3f(255.0/255.0, 180.0/255.0, 140.0/255.0)
    drawSquare(0.06)
    
    glPopMatrix()


# In[ ]:


def drawSaturn(): #토성 그리기
    global day6
    global time6
    
    glPushMatrix()
    # 공전
    glRotatef(day6, 0.0, 0.0, 1.0)
    glTranslatef(0.594, 0.0, 0.0)
    # 자전
    glRotatef(time6, 0.0, 0.0, 1.0)
    glColor3f(180.0/255.0, 145.0/255.0, 50.0/255.0)
    drawSquare(0.055)
    
    glPopMatrix()


# In[ ]:


def drawUranus(): #천왕성 그리기
    global day7
    global time7
    
    glPushMatrix()
    # 공전
    glRotatef(day7, 0.0, 0.0, 1.0)
    glTranslatef(0.702, 0.0, 0.0)
    # 자전
    glRotatef(time7, 0.0, 0.0, 1.0)
    glColor3f(80.0/255.0, 180.0/255.0, 255.0/255.0)
    drawSquare(0.035)
    
    glPopMatrix()


# In[ ]:


def drawNepturn(): #해왕성 그리기
    global day8
    global time8
    
    glPushMatrix()
    # 공전
    glRotatef(day8, 0.0, 0.0, 1.0)
    glTranslatef(0.783, 0.0, 0.0)
    # 자전
    glRotatef(time8, 0.0, 0.0, 1.0)
    glColor3f(50.0/255.0, 130.0/255.0, 200.0/255.0)
    drawSquare(0.03)
    
    glPopMatrix()


# In[ ]:


def drawScene():
    global sunRadius
    global num
    global day1, day2, day3, day4, day5, day6, day7, day8
    global time1, time2, time3, time4, time5, time6, time7, time8
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity()
    
    # 태양
    glColor3f(255.0/255.0, 199.0/255.0, 0.0/255.0)
    drawSquare(sunRadius)
    
    # 수성
    drawMercury()
    # 금성
    drawVenus()
    # 지구
    drawEarth()
    # 화성
    drawMars()
    # 목성
    drawJupiter()
    # 토성
    drawSaturn()
    # 천왕성
    drawUranus()
    # 해왕성
    drawNepturn()
    
    glEnd
    glFinish()
    glFlush()
    
    
    day1 = (day1 + num*1.5) % 360 #수성의 공전 주기는 지구보다 빠르게 설정
    time1 = (time1 + 3) % 360 # 수성의 자전 주기는 느리게 설정
    
    day2 = (day2 + num*1.3) % 360 #금성의 공전 주기는 지구보다 빠르게 설정
    time2 = (time2 + 5) % 360 # 수성의 자전 주기는 느리게 설정
    
    day3 = (day3 + num) % 360
    time3 = (time3 + 10) % 360
    
    day4 = (day4 + num*0.7) % 360 #화성의 공전 주기는 지구보다 느리게 설정
    time4 = (time4 + 15) % 360 # 화성의 자전 주기는 빠르게 설정
    
    day5 = (day5 + num*0.5) % 360 #목성의 공전 주기는 지구보다 느리게 설정
    time5 = (time5 + 20) % 360 # 목성의 자전 주기는 빠르게 설정
    
    day6 = (day6 + num*0.3) % 360 #토성의 공전 주기는 지구보다 느리게 설정
    time6 = (time6 + 30) % 360 # 토성의 자전 주기는 빠르게 설정
    
    day7 = (day7 + num*0.2) % 360 #천왕성의 공전 주기는 지구보다 느리게 설정
    time7 = (time7 + 40) % 360 # 천왕성의 자전 주기는 빠르게 설정
    
    day8 = (day8 + num*0.1) % 360 #해왕성의 공전 주기는 지구보다 느리게 설정
    time8 = (time8 + 50) % 360 # 해왕성의 자전 주기는 빠르게 설정
    
    
    glutSwapBuffers()


# In[ ]:


def keyPressed(*args):
    global window, num
    print(args[0])
    
    if args[0] == ESCAPE:
        sys.exit()
    if args[0] == b'q': # 공전속도 빨라짐
        num = num + 2
    if args[0] == b'a': # 공전속도 느려짐
        num = num - 2
    if args[0] == b's': # 자전, 공전 멈춤
        glutIdleFunc(None)
    if args[0] == b'w': # 자전, 공전 시작
        glutIdleFunc(drawScene)
        glutPostRedisplay()


# In[ ]:


def main():
    glutInit(sys.argv)
    global window
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(50, 50);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    window = glutCreateWindow("The Solar System")

    glutIdleFunc(drawScene)
    glutDisplayFunc(drawScene)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()


# In[ ]:


print("Hit ESC key to quit")
main()

