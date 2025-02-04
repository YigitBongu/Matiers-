# -*- coding: utf-8 -*-
"""
P / A

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
deger = para *  (((1+i)**n)-1)/(((1+i)**n)*i)

print(f"Hesaplanan değer: {deger}")
