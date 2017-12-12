import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import statistics



#this is sofrt fuoier trnasfrom
def short(X):
    #length of the signal
    n = len(X)
    print n
    # window
    # the window, so basically which part of the orginal signal will be processed by fourier transfrom
    win  = n/10
    print win
    #hop size
    #how much do we move, so if you see this the windows will overlap, which is one of the basis of sft
    hop = win/2
    print hop
    spectrumArray = [0]*n
    fourierArray = [0] * n
    Jup = []
    print Jup
    j = 0

# again magic, so for each of the window you perform normal fourier, but here instead of doing i+1, you use hop, to skip some
    for  i in range(0,n,hop):
        newA = X[i:i+win]
        zero = [0] * win
        conca = newA + zero

        aaa = fu(conca)
        #lo = np.abs(aaa * np.conj(aaa))
        autopower = np.abs(aaa * np.conj(aaa))
        #Jup = Jup + autopower
        #print autopower
        fourierArray[i] = aaa
        spectrumArray[i] = autopower
        #Jup = Jup + aaa
        #print  lo
        #print Jup

        #Jup = Jup + aaa
        Jup = Jup + aaa
    print spectrumArray
    print fourierArray
    return Jup



#this is fourier transform
def fu(X):
    #length of the matrix/signal
    n = len(X)
    #array thhat has length of the signall; solution will be stored here
    dupsko = [0] * n
# for each of the number in the signal, you perfom the equation, which you can find on wikipedia
    for i in range(0,n):
        dupa = [0] * n
        for k in range(0,n):
            a = np.exp(-2j * np.pi * k * i / n)*X[k]
           # print a, k
            dupa[k] = dupa[k]+a

        #print sum(dupa), 'sum'
        dupsko[i] = sum(dupa)
    #print dupsko
    return dupsko
#some example of the signal
X = [1,2,3,4,5,6,7,8,9,10,12,12,32,1,2,3,4,1,43,3,2,5,454,3,643,2,43,43,432,5,5,3,34,2,23,35,4,64,5,23,32,3,5,235,42,43,4,536,43,45,2,43,2,32,532,532,]
fupa = short(X)
"""

def half(X):
    aa = np.median(X)
    n= len(X)
    Y = []
    for i in range(0,n):
        print X[i]
        if X[i] < aa and X[i] > 0:
            Y.append(X[i])
            #np.insert(Y,X[i])
    return Y
"""

dupa = short(X)
print len(X)
print len(fupa)
plt.plot(dupa)
plt.show()

'''''''''
#SPECTRUM SHOULD BE DONE SEPERETELY FOR EACH SEGMENT/WINDOW
autopower = np.abs(fupa * np.conj(fupa))
print autopower


autopower = 20*np.log10(autopower)          # scale to db
autopower = np.clip(autopower, -40, 200)
img = plt.imshow(autopower, origin='lower', cmap='jet', interpolation='nearest', aspect='auto')
plt.show()
'''''