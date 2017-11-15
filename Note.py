class note:
    def __init__(self,x,y,z):
        self.x =x
        self.y = y
        self.z = z
      
   
def getNotes(String):
    if(String == 'C'):
        C = note(33.5,-4.5,3.5)
        return C
    if(String == 'd'):
        d = note(33, -1,3.1)
        return d
    if(String == 'e'):
        e = note(33,2.5,3)
        return e
    if(String == 'f'):
        f = note(32.5, 6,3)
        return f
    if(String =='g'):
        g = note(32,9.5,3)
        return g
    if(String =='a'): 
        a = note(31.4,11.5,3.5)
        return a
    if(String=='b'):
        b = note(30.5,15,4)
        return b
    if(String =='c'):   
        c = note(30,18,4.6)
        return c