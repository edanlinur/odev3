# Kullanıcının girdiği metni bir değişkene kaydeden, okuyan ve ekrana yazdıran Python programı 

def metin_yaz_ve_oku():
    # Kullanıcıdan tek satır metin alma
    metin = input("Bir metin girin: ")
    print("\nGirilen Metin:")
    print(metin)

def satir_satir_yaz_ve_oku():
    print("Lütfen 5 farklı satır girin:")
    satirlar = [input(f"Satır {i+1}: ") for i in range(5)]
    
    print("\nGirilen Satırlar:")
    for satir in satirlar:
        print(satir)

# Ana program
metin_yaz_ve_oku()
satir_satir_yaz_ve_oku()
