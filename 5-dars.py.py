# 5-dars. String (matn)
#sana:21/07/2023

#shahar="Фаргона"

#matn="men yangi 📱 oldim"
#print(matn)

#ism='Asilbek'
#print("Mening ismim " + ism)

#ism="Ahad"
#familiya="Qayum"
#print(ism + familiya) # ahad va qayum qo'shilib yozildi

#print(ism + " " + familiya) # ahad va qayum ajratilib yozildi
#print(ism+ " "+familiya)

# f-string
#ism='Ahad'
#familiya='Qayum'
#ism_sharif=f"{ism} {familiya}"
#print(ism_sharif)

#ism='James'
#familiya='Bond'
#print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

#Maxsus belgilar
#print("hello world!")
#print("hello \tworld!")
#print("hello \nworld!")

# string metodlar
#matn.metod() ko'rinishida yoziladi

#ism='James'
#familiya='Bond'
#ism_sharif=f"{ism} {familiya}"
#print(ism_sharif.upper())
#print(ism_sharif.lower())
#print(ism_sharif.capitalize())
#print(ism_sharif.title())

#meva="     nok      "
#print("Men " +meva.lstrip() + " yaxshi ko'raman")
#print('Men ' + meva.rstrip() + "ni yaxshi ko'raman")
#print("Men " + meva.strip() + "ni yaxshi ko'raman")
#print("Men " + meva + "yaxshi ko'raman")

# INPUT

#ism=input("Ismingiz nima?")
#print("Assalomu alaykum, " + ism)

#ism=input("Ismingiz nima?\n>>>")
#print("Assalomu alaykum, " + ism.title())

                                # AMALIYOT
                
#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
#print(kocha)
#print(mahalla)
#print(tuman)
#print(viloyat)


#kocha=input("Kochangiz nomi nima?")
#mahalla=input("Mahallangiz nomi nima?")
#tuman=input("Tumaningiz nomi nima?")
#viloyat=input("Viloyatingiz nomi nima?\n>>>")   
#print("Assalomu alaykum, " + viloyat.title() +"da yashovchi fuqaro")   
#("Assalomu alaykum,\n " + viloyat.title() +"da yashovchi fuqaro")   

#ism=input('Ismingiz nima?\n>>>')     
#manzil=input("Manzilingizni kiriting\n>>>")
#print("Assalomu alaykum, " + manzil.title() + "da yashovchi "  + ism.title())  

#manzil="Fergana"            
#print(f"Salom, men  {manzil}danman")

#manzil=f"{viloyat} {tuman}"
#print(manzil)
 
#manzil=f"{viloyat}\t, \t{tuman}"
#print(manzil.upper())
#print(manzil.capitalize())
#print(manzil.title())
#print(manzil.lower())