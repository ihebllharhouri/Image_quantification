from quantif_image import *

k=int(input("nombre de couleurs="))
im=Image.open("euler.jpg")
w,h=im.size
px=im.load()
px=RecolorierImage(h, w, px, k)
im.show()
