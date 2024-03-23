
ilk=[]
son=[]

borclar1=int(input(""))

for i in range(borclar1):
    ilk.append(input(""))

borclar2=int(input(""))

for i in range(borclar2):
    son.append(input(""))

isimi=[]
borci=[]
birles=[]
fark=[]
sonuc=[]
para= 0
isim=""
s=0
for ilkler in ilk:
    for sonlar in son:
        if ilkler.split()[0]==sonlar.split()[0]:
           para= int(ilkler.split()[1]) + int(sonlar.split()[1])
           birles.append(ilkler.split()[0]+ " " + str(para))    
    


for value in ilk:
    s=0
    for bir in birles:
       if value.split()[0]==bir.split()[0]:
          s+=1
    if s==0:
      fark.append(value)


for value in son:
    s=0
    for bir in birles:
       if value.split()[0]==bir.split()[0]:
          s+=1
    if s==0:
      fark.append(value)


sonuc= fark + birles
sirali = sorted(sonuc)

print(len(sirali))
for i in sirali:
   print(i)
