def perhitunganBMI():
    bb = int(input("Masukkan Berat Badan (Kg): "))
    tb = float(input("Masukkan Tinggi Badan (M): "))
    bmi = bb / tb**2

    print(f"Berat Badan     : {bb}")
    print(f"Tinggi Badan    : {tb}")
    print(f"Nilai BMI       : {bmi}")

    if bmi < 18.5 :
        print("Kategori BMI    : Berat Badan Kurang")
    elif 18.5 <= bmi < 24.9:
        print("Kategori BMI    : Berat Badan Normal")
    elif 25 <= bmi < 29.9:
        print("Kategori BMI    : Kelebihan Berat Badan")
    elif bmi >= 30:
        print("Kategori BMI    : Obesitas")