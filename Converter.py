# Mengonversi satuan temperature dari celcius ke satuan lain

indeks = {
    "Celcius   " : "c",
    "Fahrenheit" : "f",
    "Kelvin    " : "k",
    "Reamur    " : "r"
}

print("\n========Indeks Satuan Skala Suhu========\n")

for i in indeks :
    print("Satuan suhu :", i , "\t indeks :", indeks[i])

suhu = float(input("Masukkan suhu : "))
satuan = input("Masukkan indeks satuan skala suhu : ")

if (satuan == "c"):
    print(suhu, "derajat celcius equal to : ")
    print("Reamur       = " ,(suhu*5/4), "derajat")
    print("Fahrenheit   = " ,((suhu*9/5)+32), "derajat")
    print("Kelvin       = " ,(suhu + 273), "derajat")
