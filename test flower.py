from quantif_image import *

k=int(input("nombre de couleurs="))
im=Image.open("flower.jpg")
w,h=im.size
px=im.load()
px=RecolorierImage(h, w, px, k)
im.show()
