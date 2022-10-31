from ctypes import pointer
from doctest import master
from textwrap import fill
from tkinter import *
from tkinter import filedialog
from turtle import color
from venv import create


class GrafLik():
    color='red'
    tocka=()

    def __init__(self, color, tocka=[]):
        self.color=color 
        self.tocka=tocka

    def SetColor(self,color):
        self.color=color

    def GetColor(self,color):
        return self.color

    def Draw(self, canvas):
        pass
        



class Linija(GrafLik):
    drugatocka=(2,3)
    def __init__(self, color, tocka, drugatocka):
        self.drugatocka=drugatocka

        super().__init__(color, tocka)
    
    def Draw(self, canvas):
        canvas.create_line(self.tocka[0], self.tocka[1],self.drugatocka[0],self.drugatocka[1],fill=self.color)

        

    
class Pravokutnik(GrafLik):
    visina=1
    sirina=2
    def __init__(self, color, tocka, visina,sirina,):
        self.visina=visina
        self.sirina=sirina
        super().__init__(color, tocka)

    def Draw(self,canvas):
        canvas.create_rectangle(self.tocka[0],self.tocka[1],self.tocka[0]+self.visina,self.tocka[1]+self.sirina,outline=self.color, fill="")



class Poligon(GrafLik):
    def __init__(self, color, tocka):
        super().__init__(color, tocka)
        
    def Draw(self, canvas):
        canvas.create_polygon(self.tocka,outline=self.color, fill="")


class Kruznica(GrafLik):
    radijus=float(3)
    def __init__(self, color, tocka, radijus):
        self.radijus=radijus
        super().__init__(color, tocka)

    def Draw(self,canvas):
        canvas.create_oval(float(self.tocka[0])-self.radijus,float(self.tocka[1])-self.radijus, float(self.tocka[0])+self.radijus,float(self.tocka[1])+self.radijus, outline=self.color, fill="")

    

class Trokut(Linija):
    trecatocka=(10,50)

    def __init__(self, color, tocka, drugatocka,trecatocka):
        self.trecatocka=trecatocka
        super().__init__(color, tocka, drugatocka)
    
    def Draw(self, canvas):
        canvas.create_polygon(self.tocka[0],self.tocka[1], self.drugatocka[0],self.drugatocka[1],self.trecatocka[0],self.trecatocka[1],outline=self.color, fill="")   
        
        
class Elipsa(Kruznica):
    y_radijus=5.2

    def __init__(self, color, tocka, radijus, y_radijus):
        self.y_radijus=y_radijus
        super().__init__(color, tocka, radijus)

    def Draw(self,canvas):
        canvas.create_oval(float(self.tocka[0])-self.radijus,float(self.tocka[1])-self.y_radijus,float(self.tocka[0])+self.radijus,float(self.tocka[1])+self.y_radijus,outline=self.color, fill="")


class Application(Frame): #nasljeđujemo Tkinter.Frame
    def openfile(self):
        file=filedialog.askopenfilename()
        f = open(file, 'r')
        for line in f:
            line=line.rstrip()
            shape=line.split(' ')

            if shape[0]=="Line":
                shape.pop(0)
                boja=shape.pop(0)
                tocka1_x=float(shape[0])
                tocka1_y=float(shape[1])
                tocka1=(tocka1_x,tocka1_y)
                tocka2_x=float(shape[2])
                tocka2_y=float(shape[3])
                tocka2=(tocka2_x,tocka2_y)
                draw_shape=Linija(boja,tocka1,tocka2)
                draw_shape.Draw(self.canvas)

            if shape[0]=="Rectangle":
                shape.pop(0)
                boja=shape.pop(0)
                tocka_x=float(shape[0])
                tocka_y=float(shape[1])
                tocka=(tocka_x,tocka_y)
                visina=float(shape[2])
                sirina=float(shape[3])
                draw_shape=Pravokutnik(boja,tocka,visina,sirina)
                draw_shape.Draw(self.canvas)

            if shape[0]=="Polygon":
                shape.pop(0)
                boja = shape[0]
                shape.pop(0)
                draw_shape = Poligon(boja, shape)
                draw_shape.Draw(self.canvas)

            if shape[0]=="Circle":
                shape.pop(0)
                boja=shape.pop(0)
                center_x=float(shape[0])
                center_y=float(shape[1])
                radijus=float(shape[2])
                centar=(center_x,center_y)
                draw_shape=Kruznica(boja,centar,radijus)
                draw_shape.Draw(self.canvas)
            
            if shape[0]=="Triangle":
                shape.pop(0)
                boja=shape.pop(0)
                x1=shape[0]
                y1=shape[1]
                line_1=(x1,y1)
                x2=shape[2]
                y2=shape[3]
                line_2=(x2,y2)
                x3=shape[4]
                y3=shape[5]
                line_3=(x3,y3)
                draw_shape=Trokut(boja,line_1,line_2,line_3)
                draw_shape.Draw(self.canvas)

            if shape[0]=="Ellipse":
                shape.pop(0)
                boja=shape.pop(0)
                centar_x=float(shape[0])
                centar_y=float(shape[1])
                centar_ell=(centar_x,centar_y)
                x_poluos=float(shape[2])
                y_poluos=float(shape[3])
                draw_shape=Elipsa(boja,centar_ell,x_poluos,y_poluos)
                draw_shape.Draw(self.canvas)

    def CreateWidgets(self):

        self.m = Menu(self.master)
        self.filemenu = Menu(self.m, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.m.add_cascade(label="File", menu=self.filemenu)
        self.master.config(menu=self.m) 

        self.canvas = Canvas(self, bg='#999999', height=600, width=800)
        self.canvas.pack()
        
        
        

    def __init__(self, master = None):
        Frame.__init__(self, master) #inicijaliziramo originalni Frame
        self.pack()
        self.CreateWidgets() #Postavljamo naše kontrole




        
if __name__ == '__main__':          
    root = Tk()
    app = Application(root) #stvaramo našu klasu
    app.mainloop() 