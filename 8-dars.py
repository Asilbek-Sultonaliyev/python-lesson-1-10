#23/07/2023
# 8-dars.  list 

# cars=['bmw','volvo','gm','tesla','chevrolet']
#cars.sort()
#print(cars)        # .sort()   metodi --- alifbo tartibida tartiblaydi
#   !!! agar list da kichik harfli so`z va katta harfli so'z birga kelsa,
# kattasi birinchi keladi
#animals=['cow','Sheep','ayiq']
#animals.sort()
#print(animals)      # listni to'g'ri tartiblash uchun hamma so'zlar butunlay
#     kichik yoki katta harflar bilan boshlanishi kerak

  # listni teskari alifboda tartiblash uchun  .sort(reverse=true)  metodidan foydalaniladi
#cars.sort(reverse=True)
#print(cars)

# sorted()  metodi ro'yhatni qayta tartiblaydi 
# print(sorted(cars))
# sorted() bilan teskari tartiblash uchun unga reverse=True  argumentini qo'shamiz
# print(sorted(cars,reverse=True))

#bu ikki usul bilan biz sonli ro'yhatni tartiblashimiz ham mumkin

                  # RO'YHATNI AYLANTIRISH
 #  .reverse()--- (boshini oxiriga, oxirini boshiga) aylantirish uchun
# cars.reverse()
# print(cars)

#                   RO'YHATNI UZUNLIGINI BILISH
 # len()
# print("elementlar soni: " + str(len(cars)))                 
# print("elementlar soni:",str(len(cars)))    

#  range()  funksiyasi ---  ma`lum oraliqdagi sonlarni yaratishimiz mumkin
# sonlar=list(range(0,10))        #  0 dan 10 gacha emas, 0 dan 9 gacha chiqadi    
# print(sonlar)                 # list esa (range(0,10)) ni ro'yhatga aylantiradi

# range()   yordamida qadam berish ham mumkin
# juft_sonlar=list(range(0,20,2))    # 0 dan 20 gacha 2 ta oraliqda sonlar yaratadi
# print(juft_sonlar)

# sonlar=list(range(10))
# print(sonlar)   # agar sonlar ketma-ketligi 0 bilan boshlansa, oxirgi sonni
#kiritishning o'zi kifoya

# narhlar=[2000,3333,9000,6570,5600]
# arzon=min(narhlar)             #  min(list nomi) --- minimum narh yoki son 
# qimmat=max(narhlar)             # max(list nomi) --- maximum son
# summa=sum(narhlar)                   # sum()  --- jami summa
# print("Eng arzon narx:" , arzon,",eng qimmat narx:" , qimmat, ",jami summa:", summa)

# my_cars=cars[0:3]             # kesish
# print(my_cars)          # 0-indeksdan 3-indeksgacha  0,1,2 o'rindagilar 

# mcar=cars[:5]
# print(mcar)      # agar boshlang'ich raqamni berilmasa 0 dan boshlanadi
# mcar=cars[3:]
# print(mcar)      # agar 2-raqam berilmasa oxirgi elementgacha oladi

# royhatdan nusxa olish
# numbers=[1,2,3,4,5]
# numbers2=numbers[:]     #  kochirib oldik
# numbers2.append(6)
# print("bu sonlar ro'yhati: " ,numbers )     # bu to'g'ri kesib olish usuli
# print("bu sonlat ro'yhati:" , numbers2)


                               # tuples --- o'zgarmas ro'yhat
# toys=('bus','lizard','snake','dino')    # qavs o'zgarmas ro'yhat
# #toys.append('teddy')  # bu amalga oshmaydi chunki bu o'zgarmas ro'yhat
# # o'zgartirish mumkin
# toys=list(toys)    # ro'yhatga aylantirmaiz
# toys.append('teddy')
# toys.remove('bus') 
# toys[1]="mcqueen"
# toys=tuple(toys)   # qayta tuple qilamiz
# print(toys)   # bu amalga oshdi


                        # AMALIYOT
# davlatlar=['USA','Angliya','Ispaniya']
# print(len(davlatlar))           
# print(sorted(davlatlar))      
# print(sorted(davlatlar,reverse=True))

# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
juft_sonlar=list(range(120,1202,2))
print(juft_sonlar)
summa=sum(juft_sonlar)
print("Sonlar yig'indisi: " , summa)
katta=max(juft_sonlar)
kichik=min(juft_sonlar)
ayirma=int(katta)-int(kichik)
print("Ayirma:" , ayirma)
print(len(juft_sonlar))
bosh=juft_sonlar[0:21]
print(bosh)

oxiri=juft_sonlar[521:]
print(oxiri)

# taomlar=['osh','manti','mastava','somsa']
# nonushta=taomlar[:]
# nonushta.remove('osh')
# nonushta.remove('mastava')
# nonushta.append('qatiq')
# nonushta.append('shakar')
# print(nonushta)
# print(taomlar)
# nonushta=tuple(nonushta)
# nonushta[0]='qaymoq va non'
