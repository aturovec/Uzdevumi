'''
1. uzdevums
Uzrakstīt Python programmu 'maksa',kas lietotājam palūdz ievadīt divus skaitļus(precescenu un daudzumu)un izvada maksu par pirkumu.
'''
print('1.uzdevums\n')
print('*****************************************')# izvada uz ekrāna ievietotu tekstu
print('*                 MAKSA                 *')
print('* Autore Anastasija Turoveca 10.a klase *')
print('*****************************************')
input('\nLai turpinātu, nospied taustiņu ENTER\n\n')# programmas apturēšana

#IEVADE
while True:  
    cena = input ("Ievadiet preces cenu (eiro): ")#cena ir mainīgais
    try:
        cena = float (cena)
    except:
        print ("Lūdzu, ievadiet korekto preces cenu, izmantojiet ciparus!")
        continue
    if cena < 0:
        print ("Lūdzu, ievadiet korekto preces cenu!")
        continue
    break

while True:  
    daudzums = input ("Ievadiet preču daudzumu: ")#daudzums ir mainīgais
    try:
        daudzums = int (daudzums)
    except:
        print ("Lūdzu, Ievadiet korekto preču daudzumu, izmantojiet ciparus!")
        continue
    if daudzums < 0:
        print ("Lūdzu, ievadiet korekto preču daudzumu!")
        continue
    break

#RISINĀJUMS
print ('Jums par savu pirkumu jāmaksa' , cena * daudzums, 'eiro.')#datu un rezultātu izvade

input('\n\nLai izietu, nospied taustiņu ENTER')# programmas apturēšana
import os 
os.system('clear')# notīra ekrānu

'''
2.uzdevums
Uzrakstīt Python programmu 'atrums',kas lietotājam palūdz ievadīt divus skaitļus (attālumu metros un laiku sekundēs) un izvada ātrumu ar kuru pieveikts ievadītais attālums.
'''
print('2.uzdevums\n')
print('*****************************************')# izvada uz ekrāna ievietotu tekstu
print('*                ĀTRUMS                 *')
print('* Autore Anastasija Turoveca 10.a klase *')
print('*****************************************')
input('\nLai turpinātu, nospied taustiņu ENTER\n\n')# programmas apturēšana

#IEVADE
while True:  
    attalums = input ("Ievadiet paveikto attālumu (m): ")#attalums ir mainīgais
    try:
        attalums = float (attalums)
    except:
        print ("Lūdzu, ievadiet korekto paveikto attālumu, izmantojiet ciparus!")
        continue
    if attalums < 0:
        print ("Lūdzu, ievadiet korekto paveikto attālumu!")
        continue
    break

while True:  
    laiks = input ("Ievadiet patērēto laiku uz šo attālumu (s): ")#laiks ir mainīgais
    try:
        laiks = float (laiks)
    except:
        print ("Lūdzu, ievadiet korekto laiku, izmantojiet ciparus!")
        continue
    if laiks < 0:
        print ("Lūdzu, ievadiet korekto patērēto laiku uz šo attālumu!")
        continue
    break

#RISINĀJUMS
print ('Jūsu ātrums ir ' , attalums * laiks, ' m\s.')#datu un rezultātu izvade

input('\n\nLai izietu, nospied taustiņu ENTER')# programmas apturēšana
import os 
os.system('clear')# notīra ekrānu

'''
3. uzdevums
Uzrakstīt Python programmu 'laiks',kas lietotājam palūdz ievadīt divus skaitļus (attālumu kilometros un ātrumu m/s) un izvada laiku,cik minūtēs var pieveikt šo attālumu.
'''
print('3.uzdevums\n')
print('*****************************************')# izvada uz ekrāna ievietotu tekstu
print('*                LAIKS                  *')
print('* Autore Anastasija Turoveca 10.a klase *')
print('*****************************************')
input('\nLai turpinātu, nospied taustiņu ENTER\n\n')# programmas apturēšana

#IEVADE
while True:  
    attalums = input ("Ievadiet paveikto attālumu (km): ")#attalums ir mainīgais
    try:
        attalums = float (attalums)
    except:
        print ("Lūdzu, ievadiet korekto paveikto attālumu, izmantojiet ciparus!")
        continue
    if attalums < 0:
        print ("Lūdzu, ievadiet korekto paveikto attālumu!")
        continue
    break

while True:  #mainīgo ievades validācija
    atrums = input ("Ievadiet Jūsu ātrumu (m/s): ")
    #atrums ir mainīgais, kurš nozīme cilvēka vai transportlīdzekļa ātrumu
    try:
        atrums = float (atrums)
    except:
        print ("Lūdzu, ievadiet korekto Jūsu ātrumu, izmantojiet ciparus!")
        continue
    if atrums < 0:
        print ("Lūdzu, ievadiet korekto Jūsu ātrumu!")
        continue
    break

#RISINĀJUMS
print ('Jūsu patērētais laiks uz šo attalumu ir ', ((attalums * 1000) / atrums) / 60 , ' minūtes!')#datu un rezultātu izvade

input('\n\nLai izietu, nospied taustiņu ENTER')# programmas apturēšana
import os 
os.system('clear')# notīra ekrānu
