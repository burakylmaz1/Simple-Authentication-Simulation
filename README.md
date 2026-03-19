# Simple-Authentication-Simulation
A Python-based authentication simulation featuring username/password validation, login attempt limits, and error feedback logic.
## Öne Çıkan Özellikler
- **Mantıksal Doğrulama:** Kullanıcı adı ve parolanın sistem kayıtlarıyla ayrı ayrı veya birlikte hatalı olma durumlarının (`if-elif-else`) tespiti.
- **Dinamik Hak Yönetimi:** Kullanıcıya tanımlanan 3 giriş hakkının her hatalı denemede azaltılması ve hak bitiminde sistemin otomatik kapanması.
- **Durum Geri Bildirimi:** Hangi verinin (kullanıcı adı veya parola) hatalı olduğuna dair kullanıcıya spesifik mesajlar iletilmesi.

## Teknik Detaylar
- **Dil:** Python 3.x
- **Yapılar:**
  - `while True` ile interaktif oturum yönetimi.
  - Azaltan sayaç (`giriş_hakkı -= 1`) kullanımı.
  - Mantıksal operatörler (`and`, `!=`, `==`).

## Nasıl Çalıştırılır?
1. Bilgisayarınızda Python yüklü olduğundan emin olun.
2. `kullanici_girisi.py` dosyasını terminalden çalıştırın.
3. Sistemde tanımlı kullanıcı adı ve parolasını girerek giriş yapmayı deneyin.
