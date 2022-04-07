""" from re import X
from telnetlib import NAOL


print("David \nadmin123")
print("Harry " + "hermiona " + "ron") """
#print("ahoj " + input("zadejte sve jmeno :)\n") )

#name = input("jake je tve jmeno? :) \n")
#print( "moc me tesi " + name + " ja jsem siri")

#city = input("v jakem meste bydlis\n")
#print( "bydlim ve meste " + city)

""" 
name = input("zadej sve jmeno\n")
length = len(name)
print(name)                                                                 delka zadaneho jmena
print(length)
"""


"""  
print("vitejte v aplikaci na generovani vtipnych jmen")
name = input("jake je tvoje jmeno?\n")
print(name)                                                                 generator vtipnych jmen
vlastnost = input("jaka je tva typicka vlastnost\n")
print("tvoje vtipne jmeno je " + name + " " + vlastnost + " :) ")
 """

""" 
age = 14
print("ahoj ja jsem deny a je mi " + str(age) + " let")
 """


""" 
number = input("zadej dvouciferneé cislo\n")
prvni = int(number[0])
druhe = int(number[1])
print(prvni + druhe)
print(type(prvni))
 """
""" 
 3**5 = 3 NAOL patou 
 v pythonu je +,-,*, / a // - tohle je deleni ktery zbytek ořeze
mame jeste tohle %, jmenuje se to modulo to mi vypise zbytek deleni 26 % 7 = 5
/ - deleno vzdy vyvraci float (2.5)
 """
""" 
vaha = input("zadejte cislo sve vahy v kg\n")

vyska = input("zadejte cislo vasi vysky v metrech\n")

bmi = int(vaha) / float(vyska) * float(vyska)
bmi = int(bmi)
print("vas mbi je: " + str(bmi))

 """

# print(round(5.002 / 2, 2))
""" 
x = 1
x = x + 1

X += 1
x *= 1
x -= 1
print(f"promena ma hodnotu: {X} ")

name = "deny"
age = 15
print(f" {name} je uz {age} ")
 """
""" 
vek = input("zadej svuj vek\n")
max_vek = 90
leta = max_vek - int(vek)
mesice = leta * 12
tydny = leta * 52
dny = leta * 365
print(f"zbyva ti: {leta} let\n {mesice} mesicu\n {tydny} tydnu\n {dny} dnu zivota :)" )

 """
""" 
print("vytejte v kalkulacce\n\n")
first_number = int(input("zadejte prvni cislo\n"))
second_number = int(input("zadejte druhe cislo\n"))
plus = (first_number) + (second_number)
minus = (first_number) - (second_number)
krat = (first_number) * (second_number)
deleno = (first_number) / (second_number)

print(f"vas vysledek scitani je {plus}, v minusu {minus}, krat {krat} a v deleni {deleno} ")
 """

print("Ahoj ja jsem papousek lorra, rad opakuji vase slova \n")
text = input("zadej prosim text \n")
cislo = int(input("kolikrat chces abych to zopakoval\n"))
print(text * cislo)




