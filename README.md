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

**"Hızda Sınır Tanımayan Kontrol, Geleceği Tasarlayan Mühendislik."**

</div>

---

## 🗺️ Görev Özeti (Mission Brief)

**Hyperloop Geliştirme Projesi**, salt bir ulaşım aracı tasarımı değil, geleceğin 5. nesil taşımacılık altyapısını kurmaya yönelik multidisipliner bir mühendislik ekosistemidir. Bu depo (repository), **Teknofest 2026 Hyperloop Geliştirme Yarışması**'nın 5. yılında, *HyperSystem* podunun fiziksel dünyadaki davranışlarını en yüksek doğrulukla simüle eden bir dijital ikiz (digital twin) ve bu sistemi otonom olarak yönetecek olan gelişmiş kontrol mimarisini barındırmaktadır. Geliştirilen yazılım katmanları, podun tünel içerisindeki her milisaniyelik hareketini takip ederek güvenliği ve verimliliği en üst düzeye çıkarmayı amaçlar.

2026 Teknik Şartnamesi'nin katı kuralları doğrultusunda revize edilen sistemimiz, yarışmanın temel direklerini oluşturan üç ana kategoride de tam uyumluluk ve üstün performans sergileyecek şekilde optimize edilmiştir:
1.  **Performans Kategorisi:** 208 metrelik test tüneli içerisinde, tüm alt sistemlerin (İtki, Levitasyon, Fren, Navigasyon) kusursuz entegrasyonu ile tam parkur başarısı ve maksimum hız elde etmeyi hedefler.
2.  **Teknoloji Gösterim Kategorisi:** Manyetik askılama (levitasyon) ve lineer indüksiyon motoru (LIM) teknolojilerinde derinlemesine uzmanlaşarak, enerji verimliliği ve stabilite odaklı özgün donanım çözümleri sunar.
3.  **Tanımlı Problem Çözümü:** 2026 yılının özel problemi olan Akıllı Kapsül Güvenlik Yönetim Sistemi (AKGYS) ile pod içerisinde gelişebilecek anomali durumlarını otonom olarak analiz edip, insan hayatını önceliklendiren akıllı karar mekanizmalarını bünyesinde barındırır.

---

## ⚡ 2026 Teknik Şartname Detayları (Detailed Technical Specifications)

### 📏 Tünel Altyapısı ve Parkur Dinamikleri (Section 2)
Hyperloop test tüneli, toplamda 208 metre uzunluğa sahip, yüksek mukavemetli çelikten inşa edilmiş kapalı bir yapıdır. Yarışma, bu uzunluğun 186 metrelik aktif parkurunda gerçekleştirilmektedir; bu parkur ilk 5 metrelik kapsül yerleştirme (staging) ve son 17 metrelik acil durum duruş (safety buffer) alanlarını kapsamaktadır. Tünel içerisindeki ray sistemi, beton zemin üzerine monte edilmiş Alüminyum 6101-T6 alt plaka ve manyetik kılavuzlama için optimize edilmiştir. İçerideki basınç atmosferik seviyede (1.0 Bar) sabit tutulmakta olup, podun aerodinamik sürtünme katsayıları bu yoğunluğa göre hesaplanmıştır.

### 🛠️ Kapsül Mekanik Tasarım Kriterleri (Section 3)
Pod tasarımı, 2026 yılı için belirlenen radikal ağırlık limitlerine tam uyum sağlamaktadır. Maksimum **250 kg** toplam ağırlık sınırı, hafif kompozit yapıların kullanımını ve şasi rijitliğinin optimizasyonunu zorunlu kılmaktadır. 300 mm ile 3500 mm arasında değişebilen pod uzunluğu, aerodinamik verimlilik için kritik bir parametredir. Ayrıca, operasyonel güvenlik için arka kısımda konumlandırılan standart M8x1,25 dişli kurtarma plakası, hesaplanan maksimum frenleme kuvvetinin en az 2 katı yük değerine dayanacak şekilde şasiye entegre edilmiştir.

### 🛑 Gelişmiş Frenleme ve Emniyet Protokolleri (Section 4)
Güvenlik mimarimiz, birbirinden tamamen bağımsız ve eş zamanlı (redundant) çalışan ön ve arka mekanik/manyetik fren ünitelerinden oluşur. Fail-safe (emniyetli arıza) prensibi gereği, pod üzerindeki ana güç kaynağının kaybı veya pnomatik sistemlerdeki basınç düşüşü durumunda frenler mekanik olarak otomatik olarak kilitlenir. Sistem, maksimum 0.5 saniyelik reaksiyon süresi (build-up time) ile en yüksek hızlarda dahi güvenli duruş mesafesini korur. Podun dış yüzeyinde yer alan görsel ikaz ışıkları, frenlerin durumunu (Kırmızı: Kilitli / Yeşil: Serbest) yer istasyonundan fiziksel olarak doğrulanabilir kılar.

### 📡 Haberleşme Mimarisi ve Telemetri Protokolü (Section 5)
Sistemin merkezi sinir ağı, 2.4 GHz bandında çalışan ve 20 Mbps'lik kesintisiz bant genişliği sunan Ağ Erişim Modülü (AEM) üzerinden kurgulanmıştır. Yer istasyonu ile kurulan iletişimde gecikme süresi (latency) kritik bir eşik olan 10ms'nin altında tutulmaktadır. 1Hz frekansında yayınlanan telemetri paketleri; podun tünel içindeki 3 eksenli (X, Y, Z) pozisyon, hız ve ivme verilerinin yanı sıra roll/pitch/yaw yönelimlerini, batarya hücre sıcaklıklarını, anlık güç tüketimini ve AKGYS'den gelen otonom güvenlik raporlarını içermektedir.

### 🧭 Navigasyon ve Pozisyon Doğrulama (Section 7)
Navigasyon sistemimiz, tünel tavanına saat 9-3 yönlerinde monte edilmiş mikro-prizmatik yansıtıcı (reflektör) şeritleri temel alır. İlk 6 metrelik referans noktasından sonra her 4 metrede bir yerleştirilen bu şeritler, pod üzerindeki yüksek hassasiyetli lazer sensörler tarafından sayılarak gerçek zamanlı konum verisi üretilir. Tünelin son 100 metre ve son 48 metre girişleri, 5 cm aralıklarla sıklaştırılmış özel şerit konfigürasyonları ile işaretlenmiştir; bu sayede pod, yarışın bitişine ne kadar yaklaştığını milimetrik hassasiyetle doğrular.

### 🛡️ AKGYS: Akıllı Güvenlik Yönetim Sistemi (Section 4 - Problem Definition)
2026 yılının tanımlı problemi olan AKGYS, podun kendi kendini denetleyen bir otonom "süpervizör" mekanizmasıdır. Sistem; iç basınç, terminal sıcaklık ve yapısal ivmelenme verilerini sensör füzyonu (sensor fusion) teknikleriyle harmanlayarak bir Risk Öncelik Sayısı (RPN) hesaplar. Herhangi bir anomali durumunda sistem, harici bir komuta ihtiyaç duymadan **5 saniyenin altında** otonom duruş kararını verebilmekte ve yolcu bilgilendirme arayüzlerini anlık olarak yönetmektedir. Bu mimari, EN 50126 raylı sistem güvenlik standartları referans alınarak kurgulanmıştır.

---

## 🧠 Yazılım Mimari (Software Architecture Overview)

### Modüler ve Katmanlı Yapı (Modular Design)
Hyperloop kontrol yazılımı, bakımı kolay ve test edilebilirliği yüksek olan katı bir modüler yapı üzerine inşa edilmiştir. Her bir modül, podun hayati bir fonksiyonundan sorumludur ve merkezi `MainBrain` ünitesi ile sıkı bir veri alışverişi içerisindedir:

```bash
src/
├── core/
│   └── main_brain.py        # Merkezi Kontrol Ünitesi: Otonom görev döngüsünü ve modül entegrasyonunu yönetir.
├── modules/
│   ├── levitation.py        # Levitasyon Kontrolörü: Manyetik askı hava boşluğunu (8-12mm) PID algoritmalarıyla denetler.
│   ├── propulsion.py        # İtki Motoru: Lineer İndüksiyon Motoru (LIM) fiziğini ve thrust vektörlerini simüle eder.
│   ├── braking.py           # Fren Yönetimi: Mekanik ve magnetik frenleme sekanslarını 0.5s hassasiyetle yönetir.
│   ├── navigation.py        # Navigasyon Motoru: Reflektör tabanlı konumlandırma ve parkur bölgesi tespitini yapar.
│   ├── safety.py            # Güvenlik & BMS: Batarya sağlığını ve 55°C kritik sıcaklık limitlerini takip eder.
│   ├── telemetry.py         # Telemetri Yayını: 2026 standardına uygun GUI veri paketlerini TCP/UDP üzerinden sunar.
│   └── akgys.py             # Akıllı Güvenlik: Otonom risk analizi (FMEA) ve acil karar mekanizmalarını çalıştırır.
```

---

## 🚀 Kurulum ve Başlatma (Deployment Guide)

Hyperloop simülasyonunu ve kontrol merkezini kendi yerel sisteminizde çalıştırmak için aşağıdaki adımları izleyiniz:

1. **Sistem Gereksinimleri:** Modern bir Python 3.9 veya üzeri sürümün yüklü olduğundan emin olunuz. Geliştirme sürecinde yüksek örnekleme hızları için stabil bir işlem gücü önerilir.
2. **Depo Kurulumu ve Bağımlılıklar:**
   ```bash
   git clone https://github.com/bahattinyunus/teknofest_hyperloop.git
   cd teknofest_hyperloop
   # Bağımlılıkları yükleyerek simülasyon ortamını hazırlayın:
   pip install -r requirements.txt
   ```
3. **Komuta Merkezini Aktive Etme:**
   Merkezi `main_brain.py` dosyasını çalıştırarak önyükleme (boot) sekansını başlatın. Sistem tüm 2026 protokollerini kontrol edip onayladıktan sonra sizden görev ateşleme (mission ignite) komutunu bekleyecektir:
   ```bash
   python src/core/main_brain.py
   ```

---
<div align="center">
    <i>"Gelecek, hızlanarak gelir."</i><br>
    <b>TEKNOFEST 2026 HYPERLOOP TEAM</b>
</div>
