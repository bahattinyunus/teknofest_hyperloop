<div align="center">

```text
██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗ ██╗      ██████╗  ██████╗ ██████╗ 
██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗
███████║ ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║     ██║   ██║██║   ██║██████╔╝
██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗██║     ██║   ██║██║   ██║██╔═══╝ 
██║  ██║   ██║   ██║     ███████╗██║  ██║███████╗╚██████╔╝╚██████╔╝██║     
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     
                                                            v5.0.0-PROTOTYPE
```

![System Status](https://img.shields.io/badge/System-OPERATIONAL-brightgreen?style=for-the-badge&logo=prometheus)
![Architecture](https://img.shields.io/badge/Architecture-MODULAR-blueviolet?style=for-the-badge&logo=visual-studio-code)
![Teknofest](https://img.shields.io/badge/Mission-TEKNOFEST_2026-red?style=for-the-badge&logo=target)

**"Hız, Kontrol, Gelecek."**

</div>

---

## 🗺️ Görev Özeti (Mission Brief)

**Hyperloop**, sadece bir ulaşım projesi değil, bir mühendislik meydan okumasıdır. Bu repo, **Teknofest 2026 Hyperloop Geliştirme Yarışması** (5. Yıl) için tasarlanan *HyperSystem* podunun dijital ikizini ve kontrol mimarisini barındırır. 

2026 Şartnamesi uyarınca podumuz 3 ana teknik daldaki gereksinimleri karşılamaktadır:
1.  **Performans:** 208m tünelde tam sistem entegrasyonu.
2.  **Teknoloji Gösterim:** İleri seviye Levitasyon ve İtki (LIM) geliştirme.
3.  **Tanımlı Problem Çözümü:** Akıllı Kapsül Güvenlik Yönetim Sistemi (AKGYS).

---

## ⚡ 2026 Teknik Şartname Detayları (Detailed Specs)

### 📏 Tünel ve Parkur (Section 2)
- **Toplam Uzunluk:** 208 Metre.
- **Yarışma Parkuru:** 186 Metre (İlk 5m yerleştirme, son 17m güvenlik alanı).
- **Basınç:** Atmosferik basınç (1.0 Bar).
- **Ray Yapısı:** Alüminyum 6101-T6 (Alt plaka) ve 6061-T6 (Kılavuz ray).

### 🛠️ Kapsül Mekanik Kriterleri (Section 3)
- **Ağırlık Limiti:** Maksimum **250 kg**.
- **Uzunluk:** 300 mm - 3500 mm arası.
- **Kurtarma Sistemi:** Arka kısımda M8x1,25 dişli standart kurtarma bağlantı plakası (Çekme kuvveti dayanımı: 2x Fren Kuvveti).

### 🛑 Fren ve Güvenlik (Section 4)
- **Çift Mekanizma:** Ön ve arka bağımsız, eş zamanlı aktivasyon.
- **Fail-Safe:** Güç veya hava kaybında otomatik aktivasyon.
- **Reaksiyon Süresi:** Maksimum **0.5 saniye** (Build-up time).
- **Görsel İkaz:** Uzaktan görülebilir Fren Durum Işığı (Kırmızı: Devrede / Yeşil: Serbest).

### 📡 Haberleşme ve Telemetri (Section 5)
- **AEM (Ağ Erişim Modülü):** 2.4 GHz Router, 20 Mbps bant genişliği, <10ms gecikme.
- **Zorunlu Telemetri (1Hz):** 
  - Pozisyon (X, Y, Z), Hız ve İvme verileri.
  - Roll, Pitch, Yaw yönelimleri.
  - Batarya Voltaj/Sıcaklık ve Güç tüketimi.
  - AKGYS Güvenlik Durumu ve RPN değeri.

### 🧭 Navigasyon (Section 7)
- **Reflektör Sistemi:** İlk 6m'den sonra her 4m'de bir mikro-prizmatik reflektör şeritleri.
- **Özel İşaretçiler:** 
  - **Son 100m:** 5cm aralıklarla 20 adet şerit.
  - **Son 48m:** 5cm aralıklarla 10 adet şerit.

### 🛡️ AKGYS - Akıllı Güvenlik (Bölüm 4)
- **Otonom Karar:** Harici merkeze bağlı kalmadan <5 saniye içinde duruş kararı.
- **Sensör Füzyonu:** Sıcaklık, Basınç, İvme verilerinin birleşik analizi.
- **Risk Analizi:** RPN (Risk Priority Number) tabanlı FMEA/FTA metodolojisi.

---

## 🧠 Yazılım Mimari (Software Architecture)

### Modüler Yapı
```bash
src/
├── core/
│   └── main_brain.py        # Merkezi Kontrol Ünitesi (2026 Master Logic)
├── modules/
│   ├── levitation.py        # PID tabanlı Manyetik Askılama (8-12mm)
│   ├── propulsion.py        # LIM (Linear Induction Motor) Fiziği
│   ├── braking.py           # Çift Kademe Frenleme Kontrolü
│   ├── navigation.py        # Reflektör Sayma ve Konumlandırma
│   ├── safety.py            # BMS ve Termal Guard (55°C Limit)
│   ├── telemetry.py         # 1Hz Standart Veri Yayını
│   └── akgys.py             # Akıllı Güvenlik ve Risk Analiz Motoru
```

---

## 🚀 Kurulum ve Başlatma (Deployment)

1. **Gereksinimler:** Python 3.9+
2. **Klonla ve Yükle:**
   ```bash
   git clone https://github.com/bahattinyunus/teknofest_hyperloop.git
   cd teknofest_hyperloop
   pip install -r requirements.txt
   ```
3. **Simülasyonu Çalıştır:**
   ```bash
   python src/core/main_brain.py
   ```

---
<div align="center">
    <i>"Gelecek, hızlanarak gelir."</i><br>
    <b>TEKNOFEST 2026 HYPERLOOP TEAM</b>
</div>
