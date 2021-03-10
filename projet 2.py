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


dict={}
for i in range(len(tab)-1):
    name = tab[i][0]
    numero_de_circons=tab[i][5]
    print(name,numero_de_circons)
    dict[name]= numero_de_circons


lol =[]

for md in dict.values():
    lol.append(md)

#création d'une fenêtre graphique aux dimensions souhaitées grâce à la méthode plt.figure() de la bibliothèque matplotlib.pyplot as plt
plt.figure(figsize=(10,20))

#création de l'histogramme
plt.hist(lol,bins=5,range=(0,20),align="mid",rwidth=1,color="b",edgecolor="black",label="députés")

#afficher le titre
plt.title("histogramme représentant le numéro de cisconscription des députés")

#légendes
plt.xlabel("nombre de cirsconscription")
plt.ylabel("effectif des députés")

plt.legend()
plt.show()