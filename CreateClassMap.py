# coding: utf-8
from time import sleep

import uno
import glob

from com.sun.star.awt import Size, Point
from com.sun.star.beans import PropertyValue

from com.sun.star.drawing.FillStyle import SOLID as SOLID_FILLSTYLE
from com.sun.star.drawing.LineStyle import SOLID as SOLID_LINESTYLE
from com.sun.star.drawing.TextHorizontalAdjust import CENTER as CENTER_TEXTHA
from com.sun.star.drawing.TextVerticalAdjust   import CENTER as CENTER_TEXTVA

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
    def __init__(self):
        self.oDoc = XSCRIPTCONTEXT.getDocument()
        self.page1 = self.oDoc.DrawPages.getByIndex(0)


    def doIt(self):
        for ix in range(6):
            for iy in range(6):
                split=0 if (ix<3) else 1
                yoffset=5500
                if (iy==0):
                    if (ix<4):
                        continue
                    if (ix==4):
                        nm="table"+str(ix)+"-"+str(iy)
                        self.drawRect(nm,Point(ix*3000+1000+1000*split,iy*4500+yoffset),Size(6000,200))
                if ( (ix==0) or (ix==3) ):
                    nm="table"+str(ix)+"-"+str(iy)
                    self.drawRect(nm,Point(ix*3000+1000+1000*split,iy*4500+yoffset),Size(9000,200))
                p=Point(ix*3000+1000+1000*split,iy*4500+yoffset-1000)
                txt=str(ix)+" "+str(iy)
                nm="bx"+str(ix)+"-"+str(iy)
                self.drawTextBox(nm,p,Size(3000,700),txt)

    def drawTextBox(self,n,p,s,t,color=_RGB(240, 240, 255)):
        txtbox = self.oDoc.createInstance("com.sun.star.drawing.TextShape")
        self.page1.add(txtbox)
        txtbox.setName(n)
        txtbox.setPosition(p)
        txtbox.setSize(s)

        txtbox.LineStyle = SOLID_LINESTYLE
        txtbox.LineWidth = 50
        txtbox.LineColor = _RGB(0, 0, 0)
        txtbox.FillStyle = SOLID_FILLSTYLE
        txtbox.FillColor = color

        txtbox.setString(t)
        txtbox.TextHorizontalAdjust = CENTER_TEXTHA
        txtbox.TextVerticalAdjust   = CENTER_TEXTVA
        txtbox.CharHeight = 18


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






def CreateClasseMap():
    print ("--- start ----")

    cc=ClassClass()
    cc.doIt()

    print("--- stop ----")
    return None

    #oTBox = ThisComponent.createInstance("com.sun.star.drawing.TextShape")
    #oPos = oTBox.Position
    #oPos.X = 2500
    #oPos.Y = 2500
    #oTBox.Position = oPos
    #oSize = oTBox.Size
    #oSize.Width = 7000
    #oSize.Height = 1500
    #oTBox.Size = oSize
    #oDP = ThisComponent.DrawPages.getByName("page1")
    #oDP.add(oTBox)
    #oTBox.String = "The string"

def InsertAll():
    print ("--- start ----")
    file_list = glob.glob('/home/ypatois/unison/work/enseignement/college_nelson_mandela/trombinoscope/vignette_4_3/*.jpg')
    for f in file_list:
        InsertOne(f)
    print("--- stop ----")
    return None


def InsertOne(f):
    oDoc = XSCRIPTCONTEXT.getDocument()
    #call_dispatch(oDoc,".uno:Deselect")
    Page1 = oDoc.DrawPages.getByIndex(0)
    img = oDoc.createInstance('com.sun.star.drawing.GraphicObjectShape')
    img.GraphicURL = 'file://' + f
    position = Point(1000,1000)
    img.setPosition(position)
    size = Size (2500, 4150)
    img.setSize (size)
    Page1.add(img)
    img.setSize (size)
    img.setPosition(position)
    #w = img.actualSize.Width
    #h = img.actualSize.Height
    #ui.Print (img.GraphicURL)
    #text.insertTextContent(cursor, img, False)
    #cursor.gotoEnd(False)
    #pv=PropertyValue()
    #pv.Name="toto"
    #pv.Value=0
    #dispatcher = createUnoService("com.sun.star.frame.DispatchHelper")
    #dispatcher.executeDispatch(oDoc, ".uno:Deselect","",0,pv)
    #call_dispatch(oDoc,".uno:Deselect")
    print(f)
    #thiscomponent.currentcontroller.frame.layoutmanager.HideCurrentUI = True
    #thiscomponent.currentcontroller.frame.layoutmanager.HideCurrentUI = False
    #sleep(1)
