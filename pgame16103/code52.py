buah=('Durian','Mangga','Rambutan','Mangga')
print("Jumlah Elemen :", len(buah))
print("JUmlah Buah Mangga :", buah.count("Mangga"))

#buah.append("Mangga")
#print("Jumlah Buah Mangga :", buah.count("Mangga"))

buah=('Durian', 'Mangga', 'Rambutan', 'Mangga', 'Salak', ('Nangka', 'Apel'))
print("Buah [-1][0] :","buah[-1]][0]")

x_buah = list(buah)
x_buah[0] = "Melon"
Buah = tuple(x_buah)
print("Tuple :", buah)
