import sqlite3

# # Creation de la base de donnees de budgetDB

conn = sqlite3.connect('budgetDB.db')
cur = conn.cursor()

# # Creation de la table depense 

def table_depense():
    cur.execute(
        "CREATE TABLE depense(id INTEGER PRIMARY KEY, habillement numeric, loyer numeric, nourriture numeric, transport numeric)")
    
table_depense()   
    
       #Definition de la fonction
       
def ajouter_depense():
      
    req="INSERT INTO depense(habillement, loyer, nourriture, transport) values (?,?,?,?)"
    cur.execute(req,(habillement,loyer, nourriture, transport))
    conn.commit()
        
# afficher la fonction
ajouter_depense() 
 
# calcul du depense total

habillement = int(input("donner la depense de habillement"))
loyer= int(input("donner la depense du loyer"))
nourriture= int(input("donner la depense de la nourriture"))
transport=int(input("donner la depense pour le transport")) 

total_depense = habillement+loyer+nourriture+transport

print("vous avez depensez au total:"+str(total_depense)+"fcfa")
if total_depense > 500000:
  print("Attention vous avez trop depensez ce mois !!!")
else:
 print("votre depense est a la normale")
  
# # valider les modifications

conn.commit()

def table_revenu():
    req1="CREATE TABLE revenu(id INTEGER PRIMARY KEY, salaire numeric, business numeric, pension numeric, allocation numeric)"
    cur.execute(req1) 
    conn.commit()
    
table_revenu()

#Definition de la fonction
       
def ajouter_revenu():
    salaire = int(input("donner le revenu de votre salaire "))
    business= int(input("donner le revenu de votre business "))
    pension= int(input("donner le revenu de votre pension "))
    allocation=int(input("donner le revenu de votre allocation "))   
    req1="INSERT INTO revenu(salaire, business, pension, allocation) values (?,?,?,?)"
    cur.execute(req1,(salaire,business, pension, allocation))
    conn.commit()
        
# afficher la fonction

ajouter_revenu()  

# calcul du revenu total

salaire = int(input("donner le revenu de votre salaire "))
business= int(input("donner le revenu de votre business "))
pension= int(input("donner le revenu de votre pension "))
allocation=int(input("donner le revenu de votre allocation "))

total_revenu = salaire+business+pension+allocation

print("la somme de vos revenue est: " +str(total_revenu)+ "fcfa")

#condition sur la revenu

if total_revenu > total_depense:
 print("vous pouvez augmenter vos depenses stp!!")
else:
 print(" vous avez trop depenser cette fois ci !!!") 
conn.commit()

# calcul de l'ecart

if total_depense < total_revenu:
    ecart = total_revenu-total_depense
    print("l'ecart entre les depenses et les  revenus est :"+str(ecart)+"fcfa")
elif total_revenu < total_depense:
    ecart = total_depense-total_revenu
    print("l'ecart entre les depenses est :"+str(ecart)+"fcfa")
else:
    print("pas d'ecart entre les depenses et les revenues")

# print("l'ecart entre vos depense et revenus est estimee a :" + str(ecart) + "fcfa")

conn.commit()

# fermer la connexion
conn.close()









       
        
        
        
        
        

        
        
