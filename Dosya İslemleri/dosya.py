import os
import json

f = open("dosya.txt","r")
icerik = f.read()
#satir = f.readline()
print(icerik)
f.close()

w = open("dosya.txt","w")
w.write("Selamlar!\n")
w.write("Veri Bilimi")
w.close()

a = open("dosya.txt","a")
a.write("Merhabalar!\n")
a.write("Veri Bilimi")
a.close()

with open("dosya.txt","r") as m:
    icerkler = m.read()
    print(icerkler)

if os.path.exists("dosya.txt"):
    print("Dosya yazdiginiz konumda!")
else:
    print("dosya bulunamadi!")

#os.mkdir("yeni_klasor")

print(os.path.isdir("yeni_klasor"))

#os.rename("demo.txt","yeni.txt")

#os.rmdir("yeni_klasor")
#os.remove("yeni.txt")

veri = {"ad": "Ahmet", "yas": 38}

with open("veri.json","w") as j:
    json.dump(veri,j)

with open("veri.json","r") as js:
    okunan = json.load(js)
    print(okunan)