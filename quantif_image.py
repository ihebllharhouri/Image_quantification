from PIL import Image
from random import randint
from math import sqrt


def fréquence_couleur(w,h,px):
    liste=[]
    for i in range(h):
        for j in range(w):
            liste.append(px[i,j])
    freq = {} # stockage de la fréquence de chaque couleur
    counting = [freq.update({x: liste.count(x)}) for x in liste]
    return freq
    

        
def ChoixPalette(k):
    l=[]  #initialisation
    while len(l) <k:
        c=(randint(0, 256),randint(0, 256),randint(0, 256))  # une couleur aléatoire
        if c not in l: # on vérifie que la couleur n'existe pas déjà dans la palette
            l.append(c)
    return l

def distance(c1, c2):
    return sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)

def distance_redmean(c1,c2):
    r_barre=1/2*(c1[0]+c2[0])
    return sqrt((2+r_barre/256)*((c1[0]-c2[0])**2)+4*((c1[1]-c2[1])**2)+(2+(255-r_barre)/256)*((c1[2]-c2[2])**2))



 
def RecolorierImage(h,w,px,k):
    l=AmeliorationPalette(w, h, px, k) # Palette choisie aléatoirement
    for i in range(h): #On parcourt l'image en hauteur
        for j in range(w): #On parcourt l'image en largeur
            liste=k*[0]  #Initialisation d'une liste de distances
            for p in range(k):
                liste[p]=distance(px[i,j],l[p]) #distance euclidienne entre les couleurs
                min=liste[0]  #min:distance minimale
            ind=0  #ind:indice de la dist minimale dans le tableau
            for d in range(1,len(liste)):
                if liste[d] <min:
                    ind=d
                    min=liste[d]
            px[i,j]=l[ind]
    return px
    


def MesureErreur(h,w,px,px1):
   s=0 #compteur
   for i in range(h):
       for j in range(w):
           s+=distance(px[i,j],px1[i,j])
   return s/(w*h)  #erreur


def AmeliorationPalette(w,h,px,k):
    aire=w*h
    liste=[]   #liste vide
    for i in range(h):
        for j in range(w):
            liste.append(px[i,j])
            
              #liste contient toutes les couleurs de l'image
    liste.sort(key=lambda x: distance((0,0,0),x)) # tri de la liste par ordre croissant des normes de couleurs
    liste2=[]  #liste vide
    for i in range(k):
        ind=((2*i+1)*h*w)//(2*k)  # indice du point milieu de chaque interval
        liste2.append(liste[ind]) # on ajoute à la liste la couleur du milieu de l'interval
    return liste2

def histogramme_couleurs(w,h,px):
    freq=fréquence_couleur(w, h, px)
    l=[]
    for x, y in freq.items():
        l.append([x,y])
    l.sort(key=lambda x:x[1])
    liste=[l[len(l)][0],l[len(l)-1][0],l[len(l)-2][0],l[len(l)-3][0]] # les 4 couleurs les plus fréquents
    for i in range(h):
        for j in range(w):
            liste1=4*[0]  #Initialisation d'une liste de distances
            for p in range(4):
                liste1[p]=distance(px[i,j],liste[p]) #distance euclidienne entre les couleurs
                min=liste1[0]  #min:distance minimale
            ind=0  #ind:indice de la dist minimale dans le tableau
            for d in range(1,len(liste1)):
                if liste1[d] <min:
                    ind=d
                    min=liste1[d]
            px[i,j]=liste[ind]
    return px
    
        

  

      

if __name__ == "__main__":

    k=int(input("nombre de couleurs="))
    #im=Image.open("copper_image_a.jpg")
    im=Image.open("Mon projet.jpg")
    w,h=im.size
    px=im.load()
    #im2=im.quantize(k)
    #im2.show()  #image généré à partir de k couleurs par la méthode quantize
    im.show()

    
        
