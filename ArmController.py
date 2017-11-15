import math
from time import sleep
import serial
import Note
import numpy

Basicx = 30
Basicy = 0
Basicz = 8


def hitNote(note):
    moveToCoordinates(note.x, note.y, note.z)

    
def makeMelody(notes,times = None):
    s = 'melody '
    if(times.all() == None) :
        for i in range(length(notes)):
            times.append(500)
    for i in range(notes.size):
        angles = moveToCoordinates(notes[i].x, notes[i].y, notes[i].z)
        s += '%i %i %i %i;'%(angles[0],angles[1],angles[2],times[i])
    return s   
def moveToCoordinates(x,y,z):#inverse kinematics formulas
        if(x==0):#special case when x is 0
            if(y>0):
                ang = math.pi/2
            elif(y<0):
                ang = -math.pi/2
            else:ang=0
        else:
            ang = math.atan(y/x)
        if(x>=0):
            angle1 = ang
        else:
            angle1 = ang-math.pi
        k = math.sqrt(math.pow(x, 2)+math.pow(y,2))
        if(k>=0):
            if(k==0):k+=0.01
            tAngle = math.atan((z-LM1)/(k))
        else:
            tAngle = math.pi+math.atan((z-LM1)/(k))
        l = math.sqrt(math.pow(z-LM1,2)+math.pow(k,2))
        if(l>LM2+LM3 or l<math.fabs(LM2-LM3)):
            print("ERROR, impossible to reach position ")
            return False
        a = math.acos((LM2**2+l**2-LM3**2)/(2*LM2*l))
        b = math.acos((math.pow(LM2,2)+math.pow(LM3,2)-math.pow(l,2))/(2*LM2*LM3))
        angle2 = math.pi/2 - (tAngle+a)
        angle3 = math.pi - b
        angle1 = math.degrees(angle1)
        angle2 = math.degrees(angle2)
        angle3 = math.degrees(angle3)
        if(angle1>90 or angle2>90 or angle3>90 or angle1 <-90 or angle2< -90 or angle3<-90):
            print('EROOR, Impossible reach position, max angle is 90')
            return False

        return numpy.array([angle1,angle2,angle2])


LM1 = 10.515
LM2 = 10.43
LM3 = 26.55
ser = serial.Serial('COM18', 9600)
f = Note.getNotes('f')
d = Note.getNotes('d')
e = Note.getNotes('e')
C = Note.getNotes('C')
g = Note.getNotes('g')
a = Note.getNotes('a')

notes = numpy.array([C,C,g,g,a,a,g,f,f,e,e,d,d,C])
delays = numpy.array([500,500,500,500,500,500,1000,500,500,500,500,500,500,500])

ser.write(makeMelody(notes,delays))






# 
# moveToCoordinates(10, 10, 10)

