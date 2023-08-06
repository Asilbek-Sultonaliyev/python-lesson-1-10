# 24/07/2023
 #  9-dars. Mavzu : for takrorlash  operatori  (for loop) 
 
# mehmonlar=['Ali','Vali','Anvar']
# for mehmon in mehmonlar:                   # har bir inson uchun bitta kod yetarli
#        print('Salom ,', mehmon) 
 # bu yerda biz mehmon so'zi o'rniga istalgan narsa yozishimiz mumkin
       
#        print('Hayr,',mehmon)  # joy tashlanmasa kod bajarilmaydi

# for mehmon in mehmonlar:             # : ikki nuqta yozish shart !   bu tsikl boshlanish qatori
#     print(f"Hurmatli {mehmon},sizni 30-iyul kuni to'yga taklif qilamiz")  # mana shu ikki(yoki bazida bir) qator tsikl badani deyiladi.
#     print("Hurmat bilan,palonchiyevlar oilasi\n") # agar mana shu 3-qatorga joy tashlanmasa,u 1 marta takrorlanadi, holos
       
  
#sonlar=list(range(1,11))    
#for son in sonlar:       
   #     print(f"{son} ning kvadrati {son**2} ga teng")
        
# sonlar=list(range(11))
# sonlar_kvadrati=[]
# for son in sonlar:  # sonlardagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ini hisoblab chiqaradi
# print(sonlar)
# print(sonlar_kvadrati)

#dostlar=[]
#print("5 ta eng yaqin do'stingiz kim?")
#for n in range(5):
 #      dostlar.append(input(f"{n+1}- do'stingizning ismini kiriting:\n"))
#print(dostlar)

                 # AMALIYOT
# ismlar=['Ozodbek','Abror','Odil']
# for ism in ismlar:
#      print(f'Qalaysan,{ism}')
# print(f'Kod {len(ismlar)} marta takrorlandi')

# toq_sonlar=list(range(9,100,2))
# sonlar_kubi=[]
# for t in toq_sonlar:
#           sonlar_kubi.append(t**3)
# print(toq_sonlar)
# print(sonlar_kubi)

# kinolar=[]
# print("5 ta eng yoqtirgan kinolaringiz qaysilar?")
# for d in range(5):
#      kinolar.append(input(f"{d+1}-yoqtirgan kinongizni kiriting:\n"))
# print(kinolar)

odamlar=[]
print(input('Bugun nechta inson bilan uchrashdingiz?:\n>>>'))
for i in odamlar:
    odamlar.append(input(f"{i+1}-insonnig ismini kiriting:"))
print(odamlar)
    