# -*- coding: utf-8 -*-
"""
A / F

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
deger = para *  i / (((1+i)**n)-1)