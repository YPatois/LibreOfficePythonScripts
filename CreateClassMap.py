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


def CreateClasseMap():
    print ("--- start ----")

    oDoc = XSCRIPTCONTEXT.getDocument()
    page1 = oDoc.DrawPages.getByIndex(0)

    box = oDoc.createInstance("com.sun.star.drawing.TextShape")
    page1.add(box)
    box.setName("bx1")
    box.setPosition(Point(5000,8000))
    box.setSize(Size(5000,2000))

    box.LineStyle = SOLID_LINESTYLE
    box.LineWidth = 100
    box.LineColor = _RGB(0, 0, 0)
    box.FillStyle = SOLID_FILLSTYLE
    box.FillColor = _RGB(240, 240, 255)

    box.setString("Test")
    box.TextHorizontalAdjust = CENTER_TEXTHA
    box.TextVerticalAdjust   = CENTER_TEXTVA

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
