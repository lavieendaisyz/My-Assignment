indeks = {
    "Celcius"    ": ""c",
    "Kelvin"     ": ""k",
    "Fahrenhait" ": ""f"
}
print("==========Indeks Satuan Skala Suhu==========")
for i in indeks:
    print("Satuan suhu :", i, "\t indeks : ", indeks)

suhu = float(input("Masukkan suhu :"))
satuan = input("Masukkan indeks satuan skala suhu : ")

if(satuan == "c"):
        print(suhu, "derajat celcius : ")
        print("Kelvin = ", (suhu + 273))
        print("Celcius = ", (suhu-273))
        print("Fahrenheit = ", (suhu*9/5)+32)

