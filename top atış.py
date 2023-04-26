import random
import math
import time

random.seed(time.time())

max_yukseklik = 23
aci = 30
top_konum = [0, max_yukseklik]

def menzil_hesaplayici(hiz, hedef_uzaklik, aci):
    ucus_sure = hedef_uzaklik  / (hiz * math.cos(math.radians(aci)))
    mesafe = hiz * math.sin(math.radians(aci)) * ucus_sure
    return mesafe

def atis(hiz, hedef_uzaklik, aci, baslangic_hedefi, menzil):
    mesafe_hesapla = menzil_hesaplayici(hiz, hedef_uzaklik, aci)
    if mesafe_hesapla < baslangic_hedefi:
        print("Onune dustu")
        return "onu"
    elif mesafe_hesapla > menzil:
        print("Uzagina dustu")
        return "arka"
    else:
        print("Hedefi vurdun")
        return "vur"

def yukseklik_hesabi():
    global hiz_min
    global hiz_max
    
    hiz_min = 330
    hiz_max = 1800
    hiz_baslangic = (hiz_min + hiz_max) / 2
    atis_sayisi = 0
    
    while True:
        hedef_uzaklik = 20000 + 200 * random.randint(-10, 10)
        baslangic_hedefi = hedef_uzaklik
        menzil = hedef_uzaklik + 1000 + 100 * random.randint(-2, 2)
        ani_hiz = hiz_baslangic
        
        while True:
            atis_sayisi += 1
            print(f"{atis_sayisi}. seferde vurus gerceklesmistir hedefi vurmak icin gerekli hiz m/s: {ani_hiz:.2f}")
            result = atis(ani_hiz, hedef_uzaklik, aci, baslangic_hedefi, menzil)
            if result == "vur":
                print(f"The target was hit after {atis_sayisi} shots with a speed of {ani_hiz:.2f} m/s!")
                break
            elif result == "onu":
                hiz_max = ani_hiz
            elif result == "arka":
                hiz_min = ani_hiz
            ani_hiz = (hiz_min + hiz_max) / 2
            if ani_hiz < hiz_min:
                ani_hiz = hiz_min
            if ani_hiz > hiz_max:
                ani_hiz = hiz_max
        if atis_sayisi >= 5:
            break
    
    return hiz_min, hiz_max

hiz_min, hiz_max = yukseklik_hesabi()
print(f"Gerekli hiz araligi: {hiz_min:.2f} - {hiz_max:.2f}")