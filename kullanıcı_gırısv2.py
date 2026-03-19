print("""
********************
Kullanıcı Giriş Programı
********************
""")

sys_kullanıcı_adı="bburak"
sys_parola="12345"
giriş_hakkı=3


while True:
    kullanıcı_adı=input("Kullanıcı adı:")
    parola=input("Parola:")
    if(kullanıcı_adı!=sys_kullanıcı_adı and parola==sys_parola):
        print("KULLANICI ADI HATALI...")
        giriş_hakkı -=1

    elif(kullanıcı_adı==sys_kullanıcı_adı and parola!=sys_parola):
        print("PORALA HATALI...")
        giriş_hakkı -=1
    elif(kullanıcı_adı!=sys_kullanıcı_adı and parola!=sys_parola):
        print("KULLANICI ADI ve PAROLA HATALI...")
        giriş_hakkı -=1
    else:
        print("SİSTEME GİRİŞ YAPILDI...")
        break
    if(giriş_hakkı==0):
        print("GİRİŞ HAKKINIZ KALMAMIŞTIR...")
        break


