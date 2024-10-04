print("=======================================")
print("##----       Program Kasir       ----##")
print("=======================================")

x = int(input("Berapa Banyak Boneka yang Ingin Dibeli : "))
if x <= 0:
    print("Program ERROR")
elif x <= 12:
    print("Harga per Boneka adalah 20.000")
    print("Harga Total adalah",x * 20000)
elif x <= 24:
    print("Harga per Boneka adalah 19.500")
    print("Harga total adlah ",x * 19500)
elif x <= 50:
    print("Harga per Boneka adalah 18.000")
    print("Harga total adalah ",x * 18000)
else:
    print("Harga per Boneka adalah 17.000")
    print("Harga Total adalah ",x * 17000)

print("=======================================")
print("##----     Program Selesai       ----##")
print("=======================================")