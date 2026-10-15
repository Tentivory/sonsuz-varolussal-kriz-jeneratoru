#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Varoluşsal Kriz Jeneratörü
Bu kod gerçekten çalışır. Ama hayatın anlamını bulmaz.
"""

import random
import time

krizler = [
    "Belki de hepimiz bir simülasyonun içindeyiz ve bu simülasyonu yazan kişi de kendi varoluşunu sorguluyordur.",
    "Eğer hiçbir şey yapmazsan, yine de bir şey yapmış olursun: hiçbir şey yapmamak.",
    "Kahve içmek varoluşsal bir eylemdir. Kahve bitince varoluş da biter mi?",
    "Neden buradayız? Bu soruyu sormak bile bir cevap değildir.",
    "Belki de kod yazmak, evrenin bize verdiği en büyük şakadır.",
    "Bir gün herkes ölecek. O güne kadar da gereksiz repolar açabiliriz.",
    "Eğer ağaç ormanda düşerse ve kimse duymasa, o ağaç GitHub'a push etmiş midir?",
    "Varlık, yokluğun şikayeti midir yoksa yokluk varlığın mazereti midir?"
]

derin_sorular = [
    "Bu cümleyi okurken ne hissettin?",
    "Bu hissetme eyleminin kendisi bir kriz miydi?",
    "Kriz olmasa kriz olur muydu?",
    "Cevap vermek zorunda değilsin. Zaten cevap da yoktur."
]

def kriz_uret():
    print("\n--- YENİ KRİZ BAŞLIYOR ---")
    time.sleep(1)
    print(random.choice(krizler))
    time.sleep(0.5)
    print(random.choice(derin_sorular))
    print("--- KRİZ BİTTİ (ama bitmedi) ---\n")

def main():
    print("Sonsuz Varoluşsal Kriz Jeneratörü'ne hoş geldin.")
    print("Bu program seni kurtarmayacak. Belki daha da batıracak.")
    while True:
        kriz_uret()
        cevap = input("Başka bir kriz ister misin? (e/h): ").strip().lower()
        if cevap != 'e':
            print("Anladım. Krizden kaçmak da bir krizdir. Güle güle.")
            break

if __name__ == "__main__":
    main()

# gizli not: bazen en absürt şeyler en gerçek olanlardır
