nama = str(input("Nama : "))
asal = str(input("Asal : "))
jabatan = str(input("Jabatan : "))
gaji = input("Gaji : ")

# tunjangan gaji
if(gaji > 15000000) : 
    tunjangan = 0.1 * gaji
    print(tunjangan)

elif(gaji > 10000000) : 
    tunjangan = 0.12 * gaji
    print(tunjangan)

else :
    tunjangan = 0.15 * gaji
    print(tunjangan)

# Potongan gaji dan bonus
if(asal == "Jakarta" and jabatan == "Manager"):
    potong = gaji - (0.025 * gaji)
    print(potong)
    bonus = potong + 250000
    print(bonus)

elif(asal == "Jakarta" and jabatan == "Middle Officer"):
    potong = gaji - (0.02 * gaji)
    print(potong)
    bonus = potong + 125000
    print(bonus)


elif(asal == "Bandung" and jabatan == "Middle Officer"):
    potong = gaji - (0.02 * gaji)
    print(potong)
    bonus = potong + 125000
    print(bonus)

elif(asal == "Bandung" and jabatan == "Ass. Manager"):
    potong = gaji - (0.02 * gaji)
    print(potong)
    bonus = potong + 175000
    print(bonus)

elif(asal == "Semarang" and jabatan == "Junior Officer"):
    potong = gaji - (0.018 * gaji)
    print(potong)
    bonus = potong + 100000
    print(bonus)