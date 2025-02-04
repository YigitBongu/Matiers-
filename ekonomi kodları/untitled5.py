# -*- coding: utf-8 -*-
"""
A/P


@author: yigit
"""

i = 0.326

# Kullanıcıdan süreyi al ve geçerli bir sayı olup olmadığını kontrol et
while True:
    try:
        n = int(input("Süreyi girin: "))
        break
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin.")

# Kullanıcıdan parayı al ve geçerli bir sayı olup olmadığını kontrol et
while True:
    try:
        para = float(input("Parayı girin: "))
        break
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin.")

# Hesaplama
deger =  para* (i*((1.326)**n))/ ((1.326**n)-1)


print(f"Hesaplanan değer: {deger}")
