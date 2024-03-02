import random
 #Kivi-paber käärid
ma=input("Mängija 1 sisestage oma nimi: ")
mb=input("Mängija 2 sisestage oma nimi: ")
v=int(input("Sisestage soovitud voorude arv: "))
ta=[ ]
tb=[ ]
result = 0
for i in range(v):
    a=input(f"{ma}, valige oma käik [kivi / paber / käärid]")
    b=input(F"{mb} valige oma käik [kivi / paber / käärid]")
    if a == b:
        print("Viik")
    elif (a == "kivi" and b == "käärid") or \
        (a == "käärid" and b == "paber") or \
        (a == "paber" and b == "kivi"=):
        print(f"{ma},võitis seda vooru , + 1")
        print(ta)
    elif (b == "kivi" and a == "käärid") or \
        (b == "käärid" and a == "paber") or \
        (b == "paber" and a == "kivi"=):
        print(f"{mb},võitis seda vooru , + 1")
        print(tb)
    else:
        print("Viga! Alustage uuesti!")
        break
print(f"Tilemus mängija", {ma}, result)
print(f"Tilemus mängija", {mb}, result)
        
        
         
         
    




input("Sisestage oma nimi ")
n=int(input("Sisestage soovitud voorude arv: "))
Nimekirja=[ ]
result = 0
for i in range(n):
    l = int(input("2 + 3 = "))
    if l == 5:
        print("Voor", i + 1)
        # n=Nimekirja.append(i )
        result += 1
    else: 
        print("Voor", i +1 )
        print("Vale!")

print("Su punktide tulemus:",result)
    