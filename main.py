import time

# Kullanıcıdan e-posta ve şifre al
email = input("E-posta adresinizi girin: ")
password = input("Şifrenizi girin: ")

# E-postayı ve şifreyi kontrol ediyormuş gibi göster
print("Giriş yapılıyor...")
time.sleep(2)  # Giriş işlemini simüle etmek için bekliyor
print("Başarıyla giriş yapıldı.")

# Kullanıcıdan kontrol etmek istediği takımın adını al
team_name = input("Hangi takımın maçlarını kontrol etmek istersiniz? ")

# Takımın maç uygunluğu kontrol ediliyor
print(f"{team_name} takımının maç uygunluğu kontrol ediliyor...")
time.sleep(2)  # Kontrol ediyormuş gibi bekliyor

# En yakın maçın kontrolü ve bilet alım süreci
print("En yakın ev sahibi olduğu maç bulunuyor...")
time.sleep(2)  # Maçın bulunmasını simüle etmek için bekliyor
print(f"{team_name} için en yakın ev sahibi olduğu maç bulundu.")
print("Bilet alımı bekleniyor...")

# Son
print("İşlem tamamlandı.")
