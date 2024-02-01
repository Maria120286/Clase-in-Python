'''
o clasa eset o schita sau un prototip definit de programator in care sunt create obiecte
clasalele ofera un mijloc de a grupa datele si functionalitatile.
crearea unei clase noi creza un nou tip de obiect permitind instantiere unor obiecte din acest tip
(instantiere-crearea unui obiect

fiecare instanta de clasa poate avea atribute de atasate pentru mentinerea starii sale.Instantele de clasa pot avea si metode pt modificarea starii lor
un obiect este instanta unei clase diferente dintre obiect si calsa:
o clasa este ca o schita  in timp ce obiect este o copie a clasei cu valori reale
'''
class Dog: # clasa se scrie cu litera mare
    #atributele clasei
    specie='manifer'
    varsta=6
    nume='Bruno'
# instantierea unei obiect
d=Dog() # D=obiectul
print(type(d))
print(d.specie)
print(d.varsta)
print(d.nume)

d2=Dog()
d2.nume='Pufi' # name pt d2 devine atribut de distanta pt obiectul d2(nu se mai poate modifica decat numai d2

print(d.nume,d2.nume)
Dog.nume='Rex' # schimbarea atributului de clasa nu are nici uun efect asupraatributului de intanta
print(d.nume,d2.nume)
