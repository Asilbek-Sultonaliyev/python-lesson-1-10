    # 24/07/2023  10-dars   Mavzu:Tarmoqlanish . if-else shartlari

#avtolar=['bmw','audi','hyundai','volvo']
#for avto in avtolar:
 #       if avto == 'bmw':   # == 2 tenglik (tengmi) degan ma'noni anglatadi 
  #          print(avto.upper())     # har bir harfini kattada yoz
   #     else:          # aks holda
    #        print(avto.title())  # avto nomini faqat birinchi harfini kattada yoz
            
#ism='Ali'
#ism.lower()=='ali'

#ism=input("Ismingiz nima?\n>>>")
#if ism.lower() !='ali':                   # (!=) --- teng emasmi ma'nosida
 #         print(f'Uzr,{ism.title()} biz Alini kutyapmiz')
#else:
         # print('Salom , Ali')
          
#javob=float(input('12x6 nechiga teng?\n>>>'))
#if javob!=72 :
 #     print("Javob xato!")       # else har doim qo'yish shart emas
     
        
#yosh=int(input('Yoshingiz nechada?\n>>>'))
#if yosh>=18:                            # >=   katta yoki teng bo'lsa
 #    print("Xush kelibsiz!")
#else:
#     print('Kirish mumkin emas!')    
     
#login= input('Yangi login tanlang\n')
#if len(login)<=5:
 #     print("Login 5 harfdan ko'p bo'lishi shart")
      
#yil=int(input("Tug'ilgan yilingizni kiriting:\n>>>"))
#if 2020-yil<18:
 #       print(f'Siz {2020-yil} yoshda ekansiz')
  #      print('Kirish mumkin emas!')
#else:
 #       print('Xush kelibsiz')
 
#yosh=int(input("Yoshingiz nechada?\n>>>"))         # if bn bir qatorda printni ham ishlatish mumkin        
#if yosh>65:  print("Siz covid-19 risk guruhida ekansiz.")    

x,y=25,50          # if bn else ham bir qatorda keladi:
print("x>y") if x>y  else print("x<y")      # if bu yerda 1-print ga teng

                               # Amaliyot
cars=['mazda','toyota','gm','hyundai','kia']
for car in cars:
    #   if car=='gm':
     #             print(car.upper())
      # else:
       #           print(car.title())
      
  if car!='gm':
       print(car.title())
  else:
       print(car.upper())
       
#ism=input('Login ismingizni kiriting:\n>>>')
#if ism.lower()=='admin':
 #     print("Xush kelibsiz,Admin.Foydalanuvchilar ro'yhatini ko'rasizmi?")
#else:
 #     print(f'Xush kelibsiz,{ism.title()}!')
      
#=int(input('Birinchi sonni kiriting:>>>'))
#s=int(input('Ikkinchi sonni kiriting:>>>'))
#if son==s: 
 #     print("Sonlar teng")
      
#toq_son=int(input('Istalgan son kiriting>>>'))
#if toq_son<0:
#         print("Manfiy son.")
#else:    
 #        print('Musbat son.')     
         
sonn=int(input('Son kiriting:>>>'))
if sonn>-1:
             print(sonn**0.5)
else:
             print("Musbat son kiriting!")     # 10-dars bajarildi.