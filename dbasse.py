import sqlite3
# creation de la base de donnees 
conn = sqlite3.connect('projetDB.db')

 # creation de la table depense
  
cur = conn.cursor()
 
habillement = int(input("donner la depense de l'habillement"))
loyer = int(input("donner la depense de votre loyer"))
manger = int(input("donner la depense de votre nouriture"))
transport = int(input("donner la depense du transport " ))
req="CREATE TABLE depense(id integer primary key, habillement numeric, loyer numeric, manger numeric, transport numeric)"
req = "insert into depense(habillement, loyer, manger, transport) values (?,?,?,?)"

# execution de la requete

cur.execute(req,(habillement, loyer, manger, transport))
conn.commit()

# calcul du depense total

total_depense = habillement+loyer+manger+transport
if total_depense > 300000:
  print("vous avez trop depensez ce !!!")
else:
 print("votre depense est a la normale")
 
# sauvegarder les modifications  a la base de donnees 
conn.commit()

# # creation de la table revenu

salaire = int(input("donner votre salaire "))
business = int(input("quels sont vos revenus en business "))
pension=int(input("quel est la somme de votre pension ? "))
allocation=int(input("quel est la somme de votre allocation social? "))
req2 ="CREATE TABLE revenu(id integer primary key, salaire numeric, business numeric, pension numeric, allocation numeric)"
req2 ="insert into revenu(salaire, business, pension, allocation)  Values (?,?,?,?)"

# execution de la requete

cur.execute(req2,(salaire,business,pension,allocation))
conn.commit()

# calcul du revenu

total_revenu = salaire+business+pension+allocation

print("somme de vos revenue est: " +str(total_revenu)+ "fcfa")

# #la condition sur le revenu
if total_revenu > total_depense:
 print("vous pouvez augmenter vos depenses pour plus de revenus !!!")
else:
 print("vous reduisez vos depenses vous avez trop depenser !!!") 
conn.commit()

# calcul l'ecart
if total_depense < total_revenu:
    ecart = total_revenu-total_depense
    print("l'ecart entre les depenses etrevenus est :"+str(ecart)+"fcfa")
elif total_revenu < total_depense:
    ecart = total_depense-total_revenu
    print("l'ecart entre les depenses est :"+str(ecart)+"fcfa")
else:
    print("pas d'ecart entre les depenses et les revenues")

# print("l'ecart entre vos depense et revenus est estimee a :" + str(ecart) + "fcfa")

conn.commit()

#fermer la connection
conn.close()