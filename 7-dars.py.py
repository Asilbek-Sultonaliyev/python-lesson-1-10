#22/07/2023 
#MAVZU:LIST

#mevalar=["olma","anjir","banan","nok"]   # mevalar ro'yhati
#narxlar=[1200,2000,5600,8990]
#sonlar=['bir','ikki',3,4,5]   #matn va son aralash list
#ismlar=[]        # bo'sh list

#print(mevalar[0])   # birinchi element 0 hisoblanadi
#print(sonlar[3])
#print(mevalar[-1])   # -1 listdagi oxirgi element hisoblanadi, -2 oxiridan 2-element

#print("Birinchi meva: " , mevalar[0])

# agar list ichidagi elementlar matn ko'rinishida bo'lsa , string metodlarini ishlatsak bo'ladi
#print("Birinchi meva: " , mevalar[0].upper())

# listda arifmetik amallar bajarish ham mumkin
#print(narxlar[1] + narxlar[3])

                     # elementlarni qo'shish, o'chirish va o'zgartirish
#narxlar[0]=1500
#narxlar[2]=6000
#narxlar[3]=narxlar[3]+2000
#print(narxlar)

                           # Yangi element qo'shish
     # .append()    metodi  --- yangi element qo'shadi
#cars=[]
#cars.append("malibu")
#cars.append("cobalt")
#print(cars)

#    .insert()     metodi --- listning istalgan joyiga yangi element qo'shadi
#cars.insert(0, "Damas")
#print(cars)

#  del  ---  list ning istalgan joyidan elementni olib tashlaydi
#del mevalar[1]
#print(mevalar)  

#  .remove(element nomi)   --- qiymatni o'chirish uchun
#sonlar.remove('bir')
#print(sonlar)  # agar list da 2 ta bir xil element bo'lsa, 
# .remove() 1-kelganini olib tashlaydi

#     .pop()   --- elementni sug'urib oladi

#bozorlik=["un","yog'","go'sht"]
#mahsulot=bozorlik.pop(2)
#print("Men " + mahsulot + " sotib oldim")
#print(bozorlik)


                            # AMALIYOT
#ismlar=['Feruz','Abror','ozodbek']
#print('Salom '  + ismlar[1]  + ', yaxshimisan ')
#print(ismlar[2].title() + ", qalaysan")

#sonlar=[23,-54,98,109,7]
#sonlar.append(87)
#print(sonlar)
#sonlar.insert(0,69)
#del sonlar[2]
#print(sonlar)

tarixiy=['Buxoriy','Navoiy','Xorazmiy']
zamonaviy=['Mask','Shoxrux','Ronaldo']
football=zamonaviy.pop(2)
math=tarixiy.pop(2)
#print("Men zamonaviy shaxslardan " +  football + "  bilan, tarixiy shaxslardan esa "  +  math  +   "  bilan uchrashishni xoxlardim")


friends=[]
friends.append('Feruzbek')
#print(friends)
friends.append('Shukurullo')
friends.append('Ozodbek')
#print(friends)
friends.remove('Feruzbek')
#print(friends)
friends.insert(0,'Abror')
#print(friends)
friends.insert(2,'Muhsinjon')
print(friends)
mehmonlar=[]
kel=friends.pop(0)
mehmonlar.append(kel)
print(mehmonlar)