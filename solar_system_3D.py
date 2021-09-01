#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from PIL import Image as Image
import numpy as np


# In[ ]:


ESCAPE = b'\x1b'
window = 0

lookx, looky, lookz = 0, 0, 0

day1, day2, day3, day4, day5, day6, day7, day8 = 0, 0, 0, 0, 0, 0, 0, 0
time1, time2, time3, time4, time5, time6, time7, time8 = 0, 0, 0, 0, 0, 0, 0, 0

day_sp, day_st = 1, 1
time_sp, time_st = 1, 1


# In[ ]:


def InitGL(Width, Height):
    global g_text
    global texture, texture1, texture2, texture3, texture4, texture5
    global texture6, texture6_ring, texture7, texture7_ring, texture8, texture9
    
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glLightfv(GL_LIGHT0, GL_AMBIENT, [1, 1, 1, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 0])
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 5, 3, 0])

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH) # 구로 셰이딩
    glEnable(GL_TEXTURE_2D)
    g_text = gluNewQuadric()
    
    texture = LoadTexture("texture_sun.jpg")
    texture1 = LoadTexture("texture_mercury.jpg")
    texture2 = LoadTexture("texture_venus_surface.jpg")
    texture3 = LoadTexture("ColorMap_Day.jpg")
    texture9 = LoadTexture("texture_moon.jpg")
    texture4 = LoadTexture("texture_mars.jpg")
    texture5 = LoadTexture("texture_jupiter.jpg")
    texture6 = LoadTexture("texture_saturn.jpg")
    texture6_ring = LoadTexture('texture_saturn_ring.png')
    texture7 = LoadTexture("texture_uranus.jpg")
    texture7_ring = LoadTexture('texture_uranus_ring.png')
    texture8 = LoadTexture("texture_neptune.jpg")
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


# In[ ]:


def LoadTexture(filename):
    texName = 0
    pBitmap = Image.open(filename)
    pBitmapData = np.array(list(pBitmap.getdata()), np.int8)

    texName = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texName)
    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGB, pBitmap.size[0], pBitmap.size[1], 0,
        GL_RGB, GL_UNSIGNED_BYTE, pBitmapData
        )

    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    return texName


# In[ ]:


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0, float(Width)/float(Height), 0.1, 65.0)
    glMatrixMode(GL_MODELVIEW)


# In[ ]:


def DrawCircle(radius): # 궤도 그리기
    glColor3ub(255, 255, 255)
    glBegin(GL_LINE_STRIP)
    
    for i in range(360):
        angle = i * np.pi / 180
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        glVertex3f(x, y, 0)
    
    glEnd()


# In[ ]:


def drawMercury(): # 수성 그리기
    DrawCircle(0.5) # 궤도
    glPushMatrix()
    
    glBindTexture(GL_TEXTURE_2D, texture1)
    
    # 공전
    glRotatef(day1, 0.0, 0.0, 1.0)
    glTranslatef(0.5, 0.0, 0.0)
    # 자전
    glRotatef(time1, 0.0, 0.0, 1.0)
    
    gluSphere(g_text, 0.05, 30, 30)
    glPushMatrix()
    glPopMatrix()
    glPopMatrix()


# In[ ]:


def drawVenus(): # 금성 그리기
    DrawCircle(0.7) # 궤도
    glPushMatrix()
    
    glBindTexture(GL_TEXTURE_2D, texture2)
    
    # 공전
    glRotatef(day2, 0.0, 0.0, 1.0)
    glTranslatef(0.7, 0.0, 0.0)
    # 자전
    glRotatef(time2, 0.0, 0.0, 1.0)
    
    gluSphere(g_text, 0.07, 30, 30)
    glPushMatrix()
    glPopMatrix()
    glPopMatrix()


# In[ ]:


def drawEarth(): # 지구 그리기
    DrawCircle(1) # 궤도
    glPushMatrix()
    
    # 공전
    glRotatef(day3, 0.0, 0.0, 1.0)
    glTranslatef(1, 0.0, 0.0)
    # 자전
    glRotatef(time3, 0.0, 0.0, 1.0)
    
    glBindTexture(GL_TEXTURE_2D, texture3)
    gluSphere(g_text, 0.1, 30, 30)
    
    drawMoon()
    glPushMatrix()
    glPopMatrix()
    glPopMatrix()


# In[ ]:


def drawMoon(): # 달 그리기
    DrawCircle(0.17) # 궤도
    glPushMatrix()
    
    glBindTexture(GL_TEXTURE_2D, texture9)
    
    # 공전
    glRotatef (GLfloat(day3), 0.0, 0.0, 1.0)
    glTranslatef (0.17, 0.0, 0.0)
    # 자전
    glRotatef (GLfloat(time3), 0.0, 0.0, 1.0)
    
    gluSphere(g_text, 0.05, 20, 16)
    glPushMatrix()
    glPopMatrix()
    glPopMatrix()


# In[ ]:


def drawMars(): # 화성 그리기
    DrawCircle(1.2) # 궤도
    glPushMatrix()
    
    # 공전
    glRotatef(day4, 0.0, 0.0, 1.0)
    glTranslatef(1.2, 0.0, 0.0)
    # 자전
    glRotatef(time4, 0.0, 0.0, 1.0)
    
    glBindTexture(GL_TEXTURE_2D, texture4)
    gluSphere(g_text, 0.06, 30, 30)
    glPushMatrix()
    glPopMatrix()
    glPopMatrix()


# In[ ]:


def drawJupiter(): # 목성 그리기
    DrawCircle(1.7) # 궤도
    glPushMatrix()
    
    # 공전
    glRotatef(day5, 0.0, 0.0, 1.0)
    glTranslatef(1.7, 0.0, 0.0)
    # 자전
    glRotatef(time5, 0.0, 0.0, 1.0)
    
    glBindTexture(GL_TEXTURE_2D, texture5)
    gluSphere(g_text, 0.2, 30, 30)
    glPushMatrix()
    glPopMatrix()
    glPopMatrix()


# In[ ]:


def drawSaturn(): # 토성 그리기
    DrawCircle(2.2) # 궤도
    glPushMatrix()
    
    # 공전
    glRotatef(day6, 0.0, 0.0, 1.0)
    glTranslatef(2.2, 0.0, 0.0)
    # 자전
    glRotatef(time6, 0.0, 0.0, 1.0)
    
    glBindTexture(GL_TEXTURE_2D, texture6)
    gluSphere(g_text, 0.18, 30, 30)
    
    glRotatef(0.2, 1.0, 0.0, 0.0)
    glBindTexture(GL_TEXTURE_2D, texture6_ring)
    drawSaturnRing()
    glPushMatrix()
    glPopMatrix()
    glPopMatrix()


# In[ ]:


def drawSaturnRing(): # 토성 고리
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    
    for i in range(360):
        p=float(i * 3.14 / 180)
        glVertex3f(np.sin(p) * 0.22, np.cos(p) * 0.22, 0.0)
        
    glEnd()


# In[ ]:


def drawUranus(): # 천왕성 그리기
    DrawCircle(2.6) # 궤도
    glPushMatrix()
    
    # 공전
    glRotatef(day7, 0.0, 0.0, 1.0)
    glTranslatef(2.6, 0.0, 0.0)
    # 자전
    glRotatef(time7, 0.0, 0.0, 1.0)
    
    glBindTexture(GL_TEXTURE_2D, texture7)
    gluSphere(g_text, 0.11, 30, 30)
    drawUranusRing()
    glPushMatrix()
    glPopMatrix()
    glPopMatrix()


# In[ ]:


def drawUranusRing(): # 천왕성 고리
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    
    for i in range(360):
        p=float(i * 3.14 / 180)
        glVertex3f(np.sin(p) * 0.15, np.cos(p) * 0.15, 0.0)
        
    glEnd()


# In[ ]:


def drawNepturn(): # 해왕성 그리기
    DrawCircle(2.9) # 궤도
    glPushMatrix()
    
    # 공전
    glRotatef(day8, 0.0, 0.0, 1.0)
    glTranslatef(2.9, 0.0, 0.0)
    # 자전
    glRotatef(time8, 0.0, 0.0, 1.0)
    glBindTexture(GL_TEXTURE_2D, texture8)
    
    gluSphere(g_text, 0.1, 30, 30)
    glPushMatrix()
    glPopMatrix()
    glPopMatrix()


# In[ ]:


def revolutionCycle():
    global day1, day2, day3, day4, day5, day6, day7, day8
    global time1, time2, time3, time4, time5, time6, time7, time8
    global day_sp, day_st, time_sp, time_st
    
    # 수성
    day1 = day_st * (day1 + day_sp + 6) % 360
    time1 = time_st * (time1 + time_sp + 8) % 360
    # 금성
    day2 = day_st * (day2 + day_sp + 7) % 360 
    time2 = time_st * (time2 + time_sp + 7) % 360 
    # 지구
    day3 = day_st * (day3 + day_sp + 4) % 360 
    time3 = time_st * (time3 + time_sp + 4) % 360 
    # 화성
    day4 = day_st * (day4 + day_sp + 1.5) % 360 
    time4 = time_st * (time4 + time_sp + 2.5) % 360 
    # 목성
    day5 = day_st * (day5 + day_sp + 2) % 360 
    time5 = time_st * (time5 + time_sp + 6) % 360
    # 토성
    day6 = day_st * (day6 + day_sp + 1) % 360
    time6 = time_st * (time6 + time_sp + 2.5) % 360
    # 천왕성
    day7 = day_st * (day7 + day_sp + 0.8) % 360 
    time7 = time_st * (time7 + time_sp + 6) % 360
    # 해왕성
    day8 = day_st * (day8 + day_sp + 0.5) % 360
    time8 = time_st * (time8 + time_sp + 2) % 360

    glutPostRedisplay()


# In[ ]:


def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    
    glLoadIdentity()
    gluLookAt(0.0, 0.0, lookz + 5.0, lookx, looky, 0.0, 0.0, 1.0, 0.0)

    # 태양
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, [.4, .4, .4, 0]) # 자체발광
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    gluSphere(g_text, 0.3, 300, 300)
    glPushMatrix()

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

    glPopMatrix()

    revolutionCycle()
    glFlush()
    glutSwapBuffers()


# In[ ]:


def keyPressed(*args):
    global window
    global day_sp, time_sp
    global lookx, looky, lookz
    
    if args[0] == ESCAPE:
        sys.exit()
    if args[0] == b'q': # 공전속도 10% 빨라짐
        day_sp = day_sp * 1.1
        time_sp = 1
    if args[0] == b'e': # 공전속도 10% 느려짐
        day_sp = day_sp * 0.9
        time_sp = 1
    if args[0] == b'w': # 카메라 zoom in
        lookz -= 0.05
    if args[0] == b's': # 카메라 zoom out
        lookz += 0.05
    if args[0] == b'a': # 카메라 좌측으로 이동
        lookx += 0.05
        looky = 0
    if args[0] == b'd': # 카메라 우측으로 이동
        lookx -= 0.05
        looky = 0


# In[ ]:


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 100)
    
    window = glutCreateWindow("The Solar System")
    
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(800, 800)
    glutMainLoop()


# In[ ]:


print("Hit ESC key to quit")
main()

