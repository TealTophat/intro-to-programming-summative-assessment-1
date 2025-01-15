bono = {"Species":"Dog","Name":"Bono","Owner":"Katya"}
jean = {"Species":"Cat","Name":"Jean","Owner":"Paul"}
princess = {"Species":"Dog","Name":"Princess","Owner":"Maurice"}
bubbles = {"Species":"Fish","Name":"Bubbles","Owner":"Ted"}
ari = {"Species":"Bird","Name":"Ari","Owner":"Jaiden"}

pets = (bono, jean, princess, bubbles, ari)

for item in pets:
    print("PET NO. "+ str(pets.index(item)+1))
    print("- SPECIES: "+item.get("Species"))
    print("- NAME: "+item.get("Name"))
    print("- OWNER: "+item.get("Owner"))
