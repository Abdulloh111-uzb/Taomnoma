
hisob = 0
palov = True
shashlik = False
Shorva  = False
salat = True
choy = False 
kampot = True
osh = float(input("Palovni porsisini kiriting:"))
sal = float(input("Salatni porsisini kiriting:"))
kam = float(input("Kampotni porsisini kiriting:"))
if palov:
    pal = osh * 120000
    print("Palov buyurtma qildingiz")
    hisob += pal
if shashlik:
    sala = sal * 17000
    print("Shashlik buyurtma qildingiz")
    hisob += sala
if Shorva:
    print("Shorva buyurtma qildingiz")
    hisob += 30000
if salat:
    print("Salat buyurtma qildingiz")
    hisob += 40000
if choy:
    print("Choy buyurtma qildingiz")
    hisob += 10000
if kampot:
    kamp  = kam * 20000
    print("Kampot buyurtma qildingiz")
    hisob += kamp
print("Umumiy hisobingiz:" ,hisob)
