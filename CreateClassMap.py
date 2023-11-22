# coding: utf-8
import sys
import os.path

from time import sleep

import uno
import glob

from com.sun.star.awt import Size, Point
from com.sun.star.beans import PropertyValue

from com.sun.star.drawing.FillStyle import SOLID as SOLID_FILLSTYLE
from com.sun.star.drawing.LineStyle import SOLID as SOLID_LINESTYLE
from com.sun.star.drawing.TextHorizontalAdjust import CENTER as CENTER_TEXTHA
from com.sun.star.drawing.TextVerticalAdjust   import CENTER as CENTER_TEXTVA


from ymydata import lesclasses, basevignettes, bvn

CTX = uno.getComponentContext()
SM = CTX.getServiceManager()

def create_instance(name, with_context=False):
    if with_context:
        instance = SM.createInstanceWithContext(name, CTX)
    else:
        instance = SM.createInstance(name)
    return instance

def createUnoService(serviceName):
  sm = uno.getComponentContext().ServiceManager
  return sm.createInstanceWithContext(serviceName, uno.getComponentContext())

def call_dispatch(doc, url, args=()):
    frame = doc.getCurrentController().getFrame()
    dispatch = create_instance('com.sun.star.frame.DispatchHelper')
    dispatch.executeDispatch(frame, url, '', 0, args)
    return

_VALUES = range(0,256,1)  # 0-255 integer values
def _RGB(red: "# as 0-255", green: int, blue: "one-byte values") -> int:
    """Return a number color value made of red, green, and blue components"""

    if not (red in _VALUES and green in _VALUES and blue in _VALUES):
        raise ValueError
    return (red * 2**16) + (green * 2**8) + (blue * 2**0)

    # note:  ''red'', ''green'' and ''blue'' arguments of RGB function are one byte unsigned integer values.


class ClassClass:
    def __init__(self,classe):
        self.classe=classe
        self.oDoc = XSCRIPTCONTEXT.getDocument()
        self.page1 = self.oDoc.DrawPages.getByIndex(0)


    def doIt(self):
        yoffset=5000+600-150
        yheight=4700-100+10
        tbxheight=600
        if (self.classe[0][0]):
            for e in self.classe[0][0]:
                f=e.vignette
                p=Point(1000+130,yoffset-4400)
                nm=e.prenom
                self.insertImage(f,nm,p,Size (2741, 4550))

        if (self.classe[1][0]):
            for e in self.classe[1][0]:
                f=e.vignette
                p=Point(3000+1000+130,yoffset-4400)
                nm=e.prenom
                self.insertImage(f,nm,p,Size (2741, 4550))

        for ix in range(6):
            for iy in range(6):
                split=0 if (ix<3) else 1
                if (iy==0):
                    if (ix<4):
                        continue
                    if (ix==4):
                        nm="table"+str(ix)+"-"+str(iy)
                        self.drawRect(nm,Point(ix*3000+1000+1000*split,iy*yheight+yoffset),Size(6000,200))
                if ( (ix==0) or (ix==3) ):
                    nm="table"+str(ix)+"-"+str(iy)
                    self.drawRect(nm,Point(ix*3000+1000+1000*split,iy*yheight+yoffset),Size(9000,200))

                if (self.classe[ix][iy]):
                    f=self.classe[ix][iy].vignette
                    nm="img"+str(ix)+"-"+str(iy)
                    p=Point(ix*3000+1000+1000*split+130,iy*yheight+yoffset-4400)
                    self.insertImage(f,nm,p,Size (2741, 4550))

                p=Point(ix*3000+1000+1000*split,iy*yheight+yoffset-tbxheight-200)
                if (self.classe[ix][iy]):
                    txt=self.classe[ix][iy].prenom
                else:
                    txt=str(ix)+" "+str(iy)

                nm="bx"+str(ix)+"-"+str(iy)
                self.drawTextBox(nm,p,Size(3000,tbxheight),txt)


    def drawTextBox(self,n,p,s,t,color=_RGB(240, 240, 255)):
        txtbox = self.oDoc.createInstance("com.sun.star.drawing.TextShape")
        self.page1.add(txtbox)
        txtbox.setName(n)

        txtbox.LineStyle = SOLID_LINESTYLE
        txtbox.LineWidth = 50
        txtbox.LineColor = _RGB(0, 0, 0)
        #txtbox.FillStyle = SOLID_FILLSTYLE
        #txtbox.FillColor = color

        txtbox.setString(t)
        txtbox.TextHorizontalAdjust = CENTER_TEXTHA
        txtbox.TextVerticalAdjust   = CENTER_TEXTVA
        if (len(t)>10):
            txtbox.CharHeight = 10
        elif (len(t)>8):
            txtbox.CharHeight = 12
        elif (len(t)>7):
            txtbox.CharHeight = 14
        elif (len(t)>6):
            txtbox.CharHeight = 15
        else:
            txtbox.CharHeight = 16
        txtbox.CharContoured = True
        txtbox.setPosition(p)
        txtbox.setSize(s)


    def drawRect(self,n,p,s):
        rect = self.oDoc.createInstance("com.sun.star.drawing.RectangleShape")
        self.page1.add(rect)
        rect.setName(n)
        rect.setPosition(p)
        rect.setSize(s)

        rect.LineStyle = SOLID_LINESTYLE
        rect.LineWidth = 10
        rect.LineColor = _RGB(0, 0, 0)
        rect.FillStyle = SOLID_FILLSTYLE
        rect.FillColor = _RGB(200, 200, 255)

    def insertImage(self,f,n,p,s):
        img = self.oDoc.createInstance('com.sun.star.drawing.GraphicObjectShape')
        img.GraphicURL = 'file://' + f
        self.page1.add(img)
        img.setPosition(p)
        img.setSize (s)


class UnEleve:
    def __init__(self,e,cid):
        self.prenom=e[0]
        self.nom=e[1]
        self.ide=e[2]
        self.loc=e[3]
        self.cid=cid
        self.vignette=os.path.join(basevignettes,
                                   "vignette_"+self.cid,
                                   "vig_"+bvn+"_"+self.cid+"-"+str(self.ide)+".jpg")

    def __str__(self):
        return self.prenom+" "+self.nom+" "+str(self.loc)


class UneClasse:
    def __init__(self,c):
        self.cid=str(c[0])+"_"+str(c[1])
        self.eleves=[]
        for e in c[2]:
            self.eleves.append(UnEleve(e,self.cid))

    def getFullArray(self):
        ea=[]
        for ix in range(6):
            c=[]
            for iy in range (6):
                c.append(None)
            ea.append(c)
        ea[0][0]=[]
        ea[1][0]=[]
        for e in  self.eleves:
            if ((e.loc[0] == 0) and (e.loc[1] == 0)):
                    ea[0][0].append(e)
                    print("Not placed: "+str(e))
            else:
                if(not ea[e.loc[0]][e.loc[1]]):
                    ea[e.loc[0]][e.loc[1]]=e
                else:
                    print("Overlay: "+str(e)+" with "+str(ea[e.loc[0]][e.loc[1]]))
                    e.prenom=e.prenom+str(e.loc)
                    ea[1][0].append(e)
        return ea


    def __str__(self):
        s=self.cid+"\n"
        for e in self.eleves:
            s+=str(e)+"\n"
        return s

class LesClasses:
    def __init__(self,lc):
        self.lesclasses={}
        self.classesCid=[]
        for c in lc:
            uc=UneClasse(c)
            self.lesclasses[uc.cid]=uc
            self.classesCid.append(uc.cid)

    def getClasse(self,cid):
        return self.lesclasses[cid]

    def __str__(self):
        s=""
        for cid in self.classesCid:
            s+=str(self.lesclasses[cid])
            s+=" ----- "
        return s


def CreateClasseMap():
    print ("--- start ----")
    #print (sys.version)
    #print(sys.path)
    #print(lesclasses)

    lc=LesClasses(lesclasses)
    #print(lc)

    cc=ClassClass(lc.getClasse("4_5").getFullArray())
    cc.doIt()

    print("--- stop ----")
    return None
