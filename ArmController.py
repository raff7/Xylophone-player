import math
from time import sleep
import serial
from Note import *
import numpy

Basicx = 30
Basicy = 0
Basicz = 8


def hitNote(note):
    s = moveToCoordinates(note.x, note.y, note.z)
    ns = 'angles:%i %i %i'%(s[0],s[1],s[2])
    ns = ns.encode()
    ser.write(ns)

    
def makeMelody(notes,times = numpy.array([500]*100)):
    s = 'melody:'
    for i in range(notes.size):
        angles = moveToCoordinates(notes[i].x, notes[i].y, notes[i].z)
        s += '%i,%i,%i,%i;'%(angles[0],angles[1],angles[2],times[i])
    return s.encode() 
def moveToCoordinates(x,y,z):#inverse kinematics formulas
        if(x==0):#special case when x is 0
            if(y>0):
                angle1 = math.pi/2
            elif(y<0):
                angle1 = -math.pi/2
            else:angle1=0
        else:
            angle1 = math.atan(y/x)
        k = math.sqrt(math.pow(x, 2)+math.pow(y,2))
        if(k==0):k+=0.01
        tAngle = math.atan((z-LM1)/(k))
        l = math.sqrt(math.pow(z-LM1,2)+math.pow(k,2))
        if(l>LM2+LM3 or l<math.fabs(LM2-LM3)):
            print("ERROR, impossible to reach position ")
            return False
        a = math.acos((LM2**2+l**2-LM3**2)/(2*LM2*l))
        b = math.acos((math.pow(LM2,2)+math.pow(LM3,2)-math.pow(l,2))/(2*LM2*LM3))
        angle2 = math.pi/2 - (tAngle+a)
        angle3 = math.pi - b
        if(x<0):
            angle2 = -angle2
            angle3 = -angle3
        angle1 = math.degrees(angle1)
        angle2 = math.degrees(angle2)
        angle3 = math.degrees(angle3)
        if(angle1>90 or angle2>90 or angle3>90 or angle1 <-90 or angle2< -90 or angle3<-90):
            print('EROOR, Impossible reach position, max angle is 90')
            return False
#         c = 'angles:%i %i %i'%(angle1,angle2,angle3)
#         c = c.encode()
#         ser.write(c)
        return numpy.array([angle1,angle2,angle3])


LM1 = 10.515
LM2 = 10.43
LM3 = 26.55
ser = serial.Serial('COM18', 9600)
# f = note(34, -3,3)
# d = note(33,-10,3.5)
# e = note(33.5,-6,3)
# C = note(32.5,-13,3.5)
# g = note(33.5,0,2.5)
# a = note(33,4,3)
# b = note(30.5,15,4.7)
# c = note(31.5,18,0)
# notes = numpy.array([C,C,g,g,a,a,g,f,f,e,e,d,d,C])
# delays = numpy.array([500,500,500,500,500,500,500,1000,500,500,500,500,500,500,500])
f = note(29,15,11)
d = note(30,8.5,11)
e= note(30,12,11)
C = note(31, 5,10)
g = note(27,18.5,11.5)
a = note(28,19,18)
b = note(26,22.7,10)
c = note(25,25,11)
#g bells
notes = numpy.array([e,e,e ,e,e,e ,e,g,C,d,e,f,f,f,f,f,e,e,e,e,d,d,e,d,g])
delays = numpy.array([250,250,250,600,250,250,500,250,250,250,250,1200,250,250,600,100,250,250,600,100,250,250,250,250,600])
#supemario
# notes = numpy.array([e,e,e ,e,e,e ,e,g,C,d,e])
# delays = numpy.array([250,250,250,600,250,250,500,250,250,250,250,250])

ser.write(makeMelody(notes,delays))





