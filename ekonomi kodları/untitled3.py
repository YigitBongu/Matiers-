# -*- coding: utf-8 -*-
"""
P / F

"""
faiz = 0.3262

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
deger = para *( 1 / ((1 + faiz) ** n))

print(f"Hesaplanan değer: {deger}")
