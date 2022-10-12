# -*- coding: utf-8 -*-
"""
Created on Wed Oct  12 12:16 2022

@author: Belva Luthfiah Andini
"""
import calendar
print("Welcome to calendar program! program ini membantu mengetahui jumlah hari pada bulan dan tahun yang diinginkan")
ulang = "back"
while ulang == "back" or ulang == "<back>": 
    year = int(input("masukan tahun yang diinginkan [ex: 2004]: ")) 
    month = int(input("masukan bulan yang diinginkan [1-12]: "))
    print("ada", (calendar.monthrange(year, month)[1]), "Hari di bulan ke",month, "tahun", year)
    ulang = input("ketik <back> jika ingin menggunakan program kembali, ketik <stop> jika berhenti ")
    if ulang == "stop" or ulang == "<stop>":
        print("Terimakasih sudah menggunakan program ini bestie!")
        print("-----------------------------------------------")
        print("author : Belva Luthfiah Andini - 065002200035")
        break