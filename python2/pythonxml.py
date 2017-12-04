from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("/home/pythonml/zadania/python2/plik.xml")
collection = DOMTree.documentElement

przyciski = collection.getElementsByTagName("Button")


for przycisk in przyciski:
    print("*****Button*****")
    print("Text: %s" % przycisk.getAttribute("android:text"))
    print("ID: %s" % przycisk.getAttribute("android:id"))
    print("Layout width: %s" % przycisk.getAttribute("android:layout_width"))


przyciski[1].setAttribute("android:text","Nowe połączenie")


for przycisk in przyciski:

    print("*****Button*****")
    print("Text: %s" % przycisk.getAttribute("android:text"))
    print("ID: %s" % przycisk.getAttribute("android:id"))
    print("Layout width: %s" % przycisk.getAttribute("android:layout_width"))
