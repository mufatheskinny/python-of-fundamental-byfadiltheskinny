""""
Semua Sintaksis dasar bahasa pemrograman terdiri dari :
1. Sekuensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali-kali selama/kondisi terpenuhi
"""
# Sekuensial
print('Ibu Berkata, "Pergi ke Toko"')
print('Budi Menjawab, "Baik bu, apa yang harus saya beli?"')
print('Ibu Menjawab, "Beli 1 botol susu, jika ada telur beli 6"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek uangnya, dan ternyata cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else :
        print("Budi mebeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyerahkan hasilnya pada ibu")