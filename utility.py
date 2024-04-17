def stampaDizionario (diz):
    for key, value in diz.items():
        print("La chiave è ... "+ key)
        print("il valore è ... " + str (value))
    

def stampaOre(diz):
    #calcolare il totale delle ora del dizionario 
    totOre=0
    for key, value in dizionario.items():
        totOre= totOre+value
    return(totOre)
    #print("ore totali: " + str (totOre))

def stampaCattedrePiene(diz):
    # numero degli insegnanti con cattedra piena 
    cattedrePiene=0
    for key,value in dizionario.items():
        if value==18:
            cattedrePiene=cattedrePiene+1   
    return(cattedrePiene)
    #print("cattedre piene: " +str(cattedrePiene))

def modificaOreInsegnante(diz, professore, ore): 
    if professore in diz:
        dizionario[professore]=ore
    
def scalaOre(diz, professore, oreScal):
    if professore in diz:
        if diz[professore]-oreScal>=0:
            diz[professore]=diz[professore]-oreScal

dizionario = {"Rossi":18, "Bianchi": 16, "Verdi" : 6, }
# inserire un elemento dentro il dizionario 
dizionario ["Viola"]= 14
print(dizionario)
# modificare una coppia chiave valore 
dizionario["Bianchi"]=18
print(dizionario)

#professore="Rossi"
#ore=15

print(stampaDizionario(dizionario))

print(stampaOre(dizionario))

print(stampaCattedrePiene(dizionario))

print(modificaOreInsegnante(dizionario, "Rossi", 8))
print (dizionario)

print(scalaOre(dizionario, "Rossi",8))
print(dizionario)
#scrivere una funzione che modifichi le ore allocate ad un insegnante 
