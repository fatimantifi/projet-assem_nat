import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

import mysql.connector

con= mysql.connector.connect(host="localhost", user="root", passwd="", database="projet_assembnat")
cursor=con.cursor()

req='select * from liste_deputes'
cursor.execute(req) 
tab=cursor.fetchall()

req2='select * from  liste_mandats'
cursor.execute(req2)
tab2=cursor.fetchall()

con.close()


class mandats:
     def __init__(self):
        self.identifiant_du_depute = ""
        self.prenom_et_nom_du_depute = ""
        self.identifiant_de_lorgane = ""
        self.type_de_lorgane = ""
        self.libelle_de_lorgane = ""
        self.debut_de_la_nomination = ""
        self.fin_de_la_nomination = ""

def days_between(d1, d2):
    ab = datetime.strptime(d1, "%Y-%m-%d")
    cd = datetime.strptime(d2, "%Y-%m-%d")
    ui=abs((cd - ab).days)
    return round(ui/365)


dict={}
for i in range(len(tab2)-1):
    name=tab2[i][1]
    debut=tab2[i][6]
    fin=tab2[i][7]
    if fin!=None:
        mandat=days_between(str(debut),str(fin))
        dict[name]=mandat

# liste contenant la durée ds mandats de tout les députés

duree_mandat_annees =[]

for md in dict.values():
    duree_mandat_annees.append(md)

#création d'une fenêtre graphique aux dimensions souhaitées grâce à la méthode plt.figure() de la bibliothèque matplotlib.pyplot as plt
plt.figure(figsize=(10,20))

#création de l'histogramme
plt.hist(duree_mandat_annees,bins=5,range=(0,5),align="mid",rwidth=1,color="b",edgecolor="black",label="mandat")

#afficher le titre
plt.title("histogramme représentant la durée des mandat des députés de l'Assemblée nationale")

#légendes
plt.xlabel("durée du mandat")
plt.ylabel("effectif des députés")

plt.legend()
plt.show()