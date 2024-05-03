#Importation des biblitèques
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from random import choice
from grillevide import grivide
import facile
import moyen
import difficile
import expert
import time

#corps du programme
class Sudoku():
    def __init__(self,window):
        self.window=window
        self.window.title("Sudoku")
        self.lon=900
        self.lar=550
        self.window.geometry("{}x{}+240+80".format(self.lon, self.lar))
        self.affichageFreme()
        self.indice=[0, 1, 2, 3, 4]
        self.reverification=0

        self.temps_debut = None




        self.en_cours = False
    def affichageFreme(self):
        self.freme=Frame(self.window, bg='blue')
        self.freme.place(x=95,y=30,width=self.lon*0.8, height=self.lar*0.8)
        fremeheure=Frame(self.freme,bg='grey')
        fremeheure.place(x=160+self.lon * 0.47,y=30, width=130, height=50)
        self.duree = tk.StringVar()
        self.label = tk.Label(fremeheure, textvariable=self.duree, font=("Helvetica", 20), bg='grey')
        self.label.grid(row=0,column=0)
        Titre= Label(self.freme, text="SUDOKU", font=("ubunto", 12, "bold"), fg="white", bg="#424344")
        Titre.grid(row=1, column=0, pady=10, padx=2)
        grille=grivide

        self.fremeGrill = Frame(self.freme, bg='blue')
        self.fremeGrill.place(x=160, y=30, width=self.lon * 0.47, height=self.lar * 0.8)
        for i in range(0, 9):
            for j in range(0, 9):
                grivide[i][j]=Entry(self.fremeGrill, font=('Times romans', 15, 'bold'), width=3, bd=5,justify='center')
                grivide[i][j].grid(row=i,column=j)
                """if grille[i][j]!="  ":
                    grivide[i][j].insert(END,  grille[i][j])"""
        self.fremeGrille = Frame(self.fremeGrill, bg='green')
        self.fremeGrille.place(x=0, y=330, width=self.lon * 0.449, height=self.lar * 0.09)
        bjouer = Button(self.fremeGrille, text="Jouer", font=('times roman', 15, 'bold'), bg='green', command=self.jouer)
        bjouer.grid(row=0, column=0,pady=4,padx=15)


        bquitter = Button(self.fremeGrille, text="Quitter", font=('times roman', 15, 'bold'), bg='green', command=self.window.quit)
        bquitter.grid(row=0, column=3, columnspan=3,pady=4,padx=15)


    def jouer(self):
        self.fremeGrille = Frame(self.fremeGrill, bg='green')
        self.fremeGrille.place(x=0, y=330, width=self.lon * 0.449, height=self.lar * 0.09)
        bniveau = Button(self.fremeGrille, text="Niveau", font=('times roman', 15, 'bold'), bg='green', command=self.niveau)
        bniveau.grid(row=0, column=0, columnspan=3, pady=4, padx=15)
        bquitter = Button(self.fremeGrille, text="Quitter", font=('times roman', 15, 'bold'), bg='green',command=self.window.quit)
        bquitter.grid(row=0, column=3, columnspan=3, pady=4, padx=15)
    def niveau(self):
        self.fremeGrille = Frame(self.fremeGrill, bg='green')
        self.fremeGrille.place(x=0, y=330, width=self.lon * 0.449, height=self.lar * 0.09)
        bfacile = Button(self.fremeGrille, text="Facile", font=('times roman', 15, 'bold'), bg='green',command=self.facile)
        bfacile.grid(row=0, column=0, columnspan=3, pady=4, padx=10)
        bmoyen = Button(self.fremeGrille, text="Moyen", font=('times roman', 15, 'bold'), bg='green', command=self.moyen)
        bmoyen.grid(row=0, column=4, columnspan=3, pady=4, padx=10)
        bdifficile = Button(self.fremeGrille, text="Difficile", font=('times roman', 15, 'bold'), bg='green', command=self.difficile)
        bdifficile.grid(row=0, column=8, columnspan=3, pady=4, padx=10)
        bexpert = Button(self.fremeGrille, text="Expert", font=('times roman', 15, 'bold'), bg='green', command=self.expert)
        bexpert.grid(row=0, column=12, columnspan=3, pady=4, padx=10)


    def choiNiveau(self):
        self.fremeGrille = Frame(self.fremeGrill, bg='green')
        self.fremeGrille.place(x=0, y=330, width=self.lon * 0.449, height=self.lar * 0.09)
        bdebuter = Button(self.fremeGrille, text="Débuter", font=('times roman', 15, 'bold'), bg='green',command=self.commencer)
        bdebuter.grid(row=0, column=0, pady=4, padx=2)
        bgeneration = Button(self.fremeGrille, text="Génération", font=('times roman', 15, 'bold'), bg='green', command=self.generation)
        bgeneration.grid(row=0, column=1, pady=4, padx=4)

        bChangeNiveau = Button(self.fremeGrille, text="Niveau", font=('times roman', 15, 'bold'), bg='green', command=self.niveau)
        bChangeNiveau.grid(row=0, column=2, pady=4, padx=4)
        bquitter = Button(self.fremeGrille, text="Quitter", font=('times roman', 15, 'bold'), bg='green',command=self.window.quit)
        bquitter.grid(row=0, column=3, columnspan=3, pady=4, padx=4)
    def facile(self):
        self.temps=15
        self.choiNiveau()
        self.gridresolu=facile.gridresolu
        self.gridcharge = facile.gridcharge
        self.generation()


    def moyen(self):
        self.temps = 10
        self.choiNiveau()
        self.gridcharge=moyen.gridcharge
        self.gridresolu = moyen.gridresolu
        self.generation()
    def difficile(self):
       self.temps = 6* 60
       self.choiNiveau()
       self.temps = 7
       self.gridcharge = difficile.gridcharge
       self.gridresolu = difficile.gridresolu
       self.generation()
    def expert(self):
       self.temps = 4
       self.choiNiveau()
       self.gridcharge = expert.gridcharge
       self.gridresolu = expert.gridresolu
       self.generation()

    def generationGrille(self):
        g=choice(self.indice)
        self.grid=self.gridcharge[g]
        self.resolu=self.gridresolu[g]
        return self.grid

    def generation(self):
        self.generationGrille()
        for i in range(0, 9):
            for j in range(0, 9):
                if grivide[i][j].get() != "":
                    grivide[i][j].delete(0,END)
                if self.grid[i][j]!="":
                    grivide[i][j].insert(END,  self.grid[i][j])

    def verification(self):
        for i in range(9):
            for j in range(8):
                for k in range(j, 8):
                    if grivide[i][j].get() != "" and grivide[i][k + 1].get() != "":
                        if grivide[i][j].get() == grivide[i][k + 1].get():
                            messagebox.showerror("Erreur", "une valeur ne doit pas être répétée  sur une même ligne")
                            return False
                    if grivide[j][i].get() != "" and grivide[k + 1][i].get() != "":
                        if grivide[j][i].get() == grivide[k + 1][i].get():
                            messagebox.showerror("Erreur", "une valeur ne doit pas être répétée  dans une même colunne")
                            return False

        for j in range(0,9,3):
            for i in range(0,9,3):
                bloc=[]
                for h in range(j,j+3):
                    for l in range(i,i+3):
                        bloc.append(grivide[h][l].get())
                for a in range(9):
                    if bloc[a] != "" and bloc.count(bloc[a])>1:
                        messagebox.showerror("Erreur", "une valeur ne doit pas être répétée  dans une même région")
                        return False
        return True

    def verifFinal(self):
        for i in range(9):
            for j in range(9):
                if grivide[i][j].get() =="":
                    messagebox.showerror("Erreur", "REMPLIR TOUS LES CHAMPS")
                    return False
                else:
                    if self.verification():
                        messagebox.showinfo("Felicitations", "Félécitation vous avez gagné")


        return True


    def affichageGrille(self):
              pass


    def demarrer(self):
        if not self.en_cours:  # Vérifier si le chronomètre n'est pas déjà en cours
            self.temps_debut = time.time()
            self.en_cours = True
            self.actualiser_chronometre()


    def arreter(self):
        if self.en_cours:  # Vérifier si le chronomètre est en cours
            self.en_cours = False

    def reinitialiser(self):
        self.duree.set("00:00:00")

    def actualiser_chronometre(self):
        if self.en_cours:
            maintenant = time.time()
            duree_en_secondes = int(maintenant - self.temps_debut)
            heures = duree_en_secondes // 3600
            self.minutes = (duree_en_secondes % 3600) // 60
            secondes = (duree_en_secondes % 3600) % 60
            self.duree.set("{:02d}:{:02d}:{:02d}".format(heures, self.minutes, secondes))
            self.reverification+=1
            if self.minutes == self.temps :
                self.verifFinal()
                self.en_cours=False
            if self.reverification == 5:
                self.verification()
                self.reverification=0
            self.window.after(1000, self.actualiser_chronometre)

    def commencer(self):
        self.demarrer()







#Exécution du programme
master=Tk()
app=Sudoku(master)
master.mainloop()