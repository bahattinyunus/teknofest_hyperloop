<p align="center">
  <img src="assets/banner.png" alt="Teknofest 2026 Hyperloop Banner" width="100%">
</p>

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
![Category](https://img.shields.io/badge/Category-MULTI--DOMAIN-orange?style=for-the-badge&logo=aircanada)

**"Sınırları Zorlayan Hız, Akılla Birleşen Güvenlik: Hyperloop 2026."**

</div>

---

## 🗺️ Görev Özeti (Mission Brief)

**Hyperloop Geliştirme Projesi**, sadece bir ulaşım teknolojisi prototipi değil, geleceğin "5. Taşıma Modu" için geliştirilen kapsamlı bir mühendislik çözümüdür. Bu repository (depo), **Teknofest 2026 Hyperloop Geliştirme Yarışması** kapsamında tasarlanan *HyperSystem* kapsülünün kontrol yazılımını, fiziksel simülasyon ortamını ve akıllı güvenlik katmanlarını içermektedir. 

2026 yılındaki 5. Yarışma, takımlardan sadece hız yapmalarını değil; enerji verimliliği, otonom güvenlik ve ileri seviye elektromanyetik askılama konularında da yetkinlik beklemektedir. Yazılım mimarimiz, bu çok disiplinli gereksinimleri tek bir çatı altında birleştirerek, tünel içerisindeki kritik verileri mikrosaniye hassasiyetinde işler.

---

## 🏎️ Yarışma Kategorileri (Competition Domains)

Podumuz, 2026 şartnamesinde tanımlanan üç kritik alanda da en yüksek standartları karşılamaktadır:

### 1. Performans Kategorisi (Efficiency & Speed)
208 metrelik vakum-benzeri test tünelinde, itki ve levitasyon sistemlerinin harmonik çalışmasıyla elde edilir.
- **Hedef:** 186 metrelik aktif parkurda maksimum ivme ve kontrollü duruş.
- **Odak:** Enerji tüketimi minimizasyonu ve hava aralığı kararlılığı.

### 2. Teknoloji Gösterim Kategorisi (Core Tech)
İleri seviye donanım yetkinliklerini kanıtlamak üzere tasarlanmıştır.
- **Levitasyon:** Çelik raylar üzerinde, temassız ve minimum sürtünmeli askılama (TRL 5+).
- **İtki (LIM):** Lineer İndüksiyon Motoru ile temassız kuvvet iletimi ve rejeneratif frenleme analizi.

### 3. Tanımlı Problem Çözümü: AKGYS (Autonomous Safety)
2026'nın özel teması olan **Akıllı Kapsül Güvenlik Yönetim Sistemi**.
- **Senaryo:** Kapsül içi dekompresyon, yangın veya donanım arızası durumunda insan müdahalesi olmadan karar verme.
- **Metodoloji:** FMEA ve FTA tabanlı risk önceliklendirme (RPN).

---

## ⚡ 2026 Teknik Şartname El Kitabı (Deep-Dive Specs)

### 📏 Tünel ve Parkur Geometrisi
- **Dış Çap:** 1168 mm | **İç Çap:** 1148 mm.
- **Parkur Yapısı:** 
  - **0-5m:** Kapsül Yerleştirme Alanı (Staging).
  - **5-191m:** Aktif Yarış Alanı (186 Metre).
  - **191-208m:** Güvenlik ve Bariyer Bölgesi.
- **Ray:** Alüminyum 6101-T6 (Alt) ve 6061-T6 (Kılavuz). Ray sertlik değeri, fren balatalarından yüksek olmalıdır.

### 🛠️ Mekanik ve Yapısal İsterler
- **Kütle (MASS):** Tam olarak **250 kg** limiti. Her gram, ivmelenme eğrisini doğrudan etkiler.
- **Kurtarma (Recovery):** Arka plakada M8x1,25 vida delikleri. Diş derinliği min. 10mm. Bu plaka, podun toplam ağırlığının 2 katı çekme kuvvetine dayanıklıdır.
- **Isıl Yönetim:** Ray üzerindeki sıcaklık artışı (ΔT), 30°C'yi kesinlikle geçmemelidir.

### 🛑 Frenleme ve Fail-Safe Mantığı
- **Dual Redundancy:** Ön ve arka frenler birbirinden izole çalışır.
- **Fail-Safe Mode:** Güç kaybında veya yazılım çökmesinde yay baskılı mekanizmalar otonom olarak kapanır.
- **Build-up Time:** Frenlerin tam kuvvete ulaşma süresi < 0.5s.

### 📡 Haberleşme ve Veri Paketi
- **AEM:** 12-36V DC besleme, DB9 konnektör, 5 adet RJ45 portu.
- **Paket Yapısı (1Hz):** 
  - `POS_X`, `POS_Y`, `POS_Z` (Metre cinsinden).
  - `VEL_X`, `ACC_X` (Hız ve İvme).
  - `BMS_TEMP1`, `BMS_TEMP2`, `BMS_VOLT`, `PWR_CONS`.
  - `AKGYS_RPN` ve `SYS_STATUS`.

---

## 🛡️ AKGYS ve Risk Analizi (Smart Security Engine)

Akıllı Kapsül Güvenlik Yönetim Sistemi, podun "bilinçli" kısmıdır. 2026 şartnamesi Bölüm 4 uyarınca aşağıdaki mantıkla çalışır:

| Parametre | Tespit Yöntemi | Kritik Eşik | Aksiyon |
| :--- | :--- | :--- | :--- |
| **İç Basınç** | Barometrik Sensör | < 0.5 Bar (Düşüş) | Acil Durdurma |
| **Sıcaklık** | 10 Hücrede 1 Sensör | > 55°C | Güç Kesme + Fren |
| **İvme** | 3-Eksenli IMU | > 2.5G (Anormal) | Uyarı / Stabilizasyon |

**RPN Hesaplama Formülü:**
`RPN = Şiddet (S) x Olasılık (O) x Tespit Edilebilirlik (D)`
- `RPN > 50`: Otomatik Acil Durdurma (AUTO_EMERGENCY_STOP).
- `RPN 25-50`: Operatör Uyarısı (WARNING_MODERATE).

---

## 🧠 Yazılım ve Kontrol Mimarisi (Architecture)

### PID Levitasyon Kontrolü
Levitasyon modülümüz, manyetik hava aralığını 10.0mm'de sabit tutmak için çift katmanlı bir PID döngüsü kullanır:
- **Kp (Proportional):** Hızlı tepki için optimize edildi.
- **Ki (Integral):** Kalıcı hata payını (steady-state error) sıfırlar.
- **Kd (Derivative):** Salınımı ve ani zıplamaları sönümler.

### Navigasyon: Reflektör Sayma Algoritması
Tünel tavanındaki mikro-prizmatik reflektörleri okuyan lazer sensörleri, `navigation.py` içerisinde şu mantığı yürütür:
1.  Her 4m'de bir "Normal Puls" üretilir.
2.  Son 100m'de puls frekansı 80 kat artar (Son 100m İşaretçisi).
3.  Sensör füzyonu ile Encoder verisi, Reflektör verisiyle çaprazlanır (Cross-check).

---

## 🚀 Kurulum ve Kullanım (Setup Guide)

### Gereksinimler
- Python 3.9+
- `numpy`, `matplotlib` (Simülasyon görselleştirme için)

### Hızlı Başlangıç
```bash
# 1. Depoyu klonlayın
git clone https://github.com/bahattinyunus/teknofest_hyperloop.git

# 2. Dizin içerisine girin
cd teknofest_hyperloop

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 4. Ana Kontrol Beynini Çalıştırın
python src/core/main_brain.py
```

---

## 📅 Gelecek Planları (Roadmap)
- [ ] **GUIdashboard:** 2026 AEM uyumlu gerçek zamanlı grafik arayüz.
- [ ] **Hardware-in-the-Loop (HIL):** ESP32 tabanlı fiziksel kontrolcü entegrasyonu.
- [ ] **AI-Predictive Maintenance:** RPN analizine LSTM tabanlı anomali tahmini eklenmesi.

---
<div align="center">
    <img src="https://img.shields.io/badge/Powered%20by-Python%203.9-blue?style=for-the-badge&logo=python" alt="Python">
    <br>
    <i>"Gelecek, hızlanarak gelir."</i><br>
    <b>TEKNOFEST 2026 HYPERLOOP TEAM</b>
</div>
