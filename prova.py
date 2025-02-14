inventario = {
    1 : {"nome": "Il PC di ...", "quantità": 1, "prezzo": 3999},
    2 : {"nome": "Nintendo Switch 2", "quantità": 10, "prezzo": 449},
    3 : {"nome": "GTA VI", "quantità": 3, "prezzo": 100}
}
def aggiunta():
    chiave = len(inventario) + 1
    nome = input("inserisci un nome: ")
    quantità = int(input("inserisci la quantità: "))
    prezzo = int(input("inserisci il prezzo: "))
    inventario[chiave] = {"nome" : nome , "quantità" : quantità , "prezzo" : prezzo}
    print(inventario)
print(aggiunta())

def modifica_quantità():
    if chiave in studente.keys():
        studente["quantità"] = input("inserisci nuovo valore")
        print(studente)
    else:
        print("la chiave non esiste")
