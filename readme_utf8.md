<div align="center">

```text
██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗ ██╗      ██████╗  ██████╗ ██████╗ 
██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗
███████║ ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║     ██║   ██║██║   ██║██████╔╝
██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗██║     ██║   ██║██║   ██║██╔═══╝ 
██║  ██║   ██║   ██║     ███████╗██║  ██║███████╗╚██████╔╝╚██████╔╝██║     
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     
                                                            v4.0.0-PROTOTYPE
```

![System Status](https://img.shields.io/badge/System-OPERATIONAL-brightgreen?style=for-the-badge&logo=prometheus)
![Architecture](https://img.shields.io/badge/Architecture-MODULAR-blueviolet?style=for-the-badge&logo=visual-studio-code)
![Teknofest](https://img.shields.io/badge/Mission-TEKNOFEST_2025-red?style=for-the-badge&logo=target)

**"Hız, Kontrol, Gelecek."**

</div>

---

## �️ Görev Özeti (Mission Brief)

**Hyperloop**, sadece bir ulaşım projesi değil, bir mühendislik meydan okumasıdır. Bu repo, **Teknofest Hyperloop Geliştirme Yarışması** için tasarlanan *HyperSystem* podunun dijital ikizini ve kontrol mimarisini barındırır. Amaç, ses hızına yakın hızlarda seyredecek bir podun elektromanyetik, mekanik ve yazılımsal entegrasyonunu kusursuz bir şekilde simüle etmek ve yönetmektir.

> [!NOTE]
> Bu bir **Command Center** reposudur. Kodlar, sadece fonksiyonel değil, aynı zamanda sistemin hayatta kalma (survival) protokolleridir.

## 🧠 Bilişsel Mimari (Cognitive Architecture)

Podumuz, merkezi bir "Brain" tarafından yönetilen otonom bir varlıktır. Aşağıdaki diyagram, sistemin düşünce yapısını özetler.

```mermaid
graph TD
    User([Master Control]) -->|Start Sequence| Brain[🧠 Main Brain]
    
    subgraph "SENSORY CORTEX"
        Lidar[LIDAR Stream] --> Telemetry
        IMU[IMU / Accel] --> Telemetry
        Temp[Thermal Sensors] --> Telemetry
    end
    
    subgraph "CORE PROCESSING"
        Brain -->|Request State| StateMachine{State Machine}
        StateMachine -->|IDLE| CheckUnit
        StateMachine -->|LEVITATION| LevControl[Levitation Control]
        StateMachine -->|ACCELERATION| PropEngine[Propulsion Engine]
        StateMachine -->|BRAKING| BrakeSys[Mech/Mag Braking]
    end
    
    LevControl -->|Gap Data| Telemetry[📡 Telemetry Bus]
    PropEngine -->|Speed Data| Telemetry
    
    Telemetry -->|Real-time Packet| Dashboard[🖥️ Ground Station]
    
    style Brain fill:#f96,stroke:#333,stroke-width:2px
    style StateMachine fill:#69f,stroke:#333,stroke-width:2px
```

## ⚡ Teknik Spesifikasyonlar (Technical Specs)

### 1. Levitation (Manyetik Askılama)
Sistemimiz, hava boşluğunu (air gap) mikron seviyesinde kontrol etmek için **PID (Proportional-Integral-Derivative)** algoritmaları kullanır.

- **Teknoloji**: EMS (Electro-Magnetic Suspension) / EDS (Electro-Dynamic Suspension) Hibrit Modeli.
- **Kontrol Döngüsü**: 1000Hz.
- **Hedef Gap**: 8mm - 12mm.

### 2. Propulsion (İtki Sistemi)
Doğrusal İndüksiyon Motoru (LIM) simülasyonu, slip (kayma) ve kuvvet vektörlerini hesaplar.

- **Max Thrust**: 5000N.
- **Max Hız**: 1200 km/h (Teorik).
- **Soğutma**: Aktif sıvı soğutma telemetrisi entegre.

### 3. Telemetry (Telemetri ve Haberleşme)
Pod, Yer İstasyonu ile TCP/UDP üzerinden *Heartbeat* paketleri göndererek sürekli iletişimde kalır.

- **Packet Structure**: `Header | Timestamp | State | SensorData | CRC`
- **Latency**: < 20ms.

## �️ Kurulum ve Başlatma (Deployment)

Bu komuta merkezini yerel makinenizde ayağa kaldırmak için:

1. **Repoyu Klonla**:
   ```bash
   git clone https://github.com/bahattinyunus/teknofest_hyperloop.git
   cd teknofest_hyperloop
   ```

2. **Sanal Ortam ve Bağımlılıklar**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt # (Yakında eklenecek)
   ```

3. **Simülasyonu Başlat**:
   ```bash
   python src/core/main_brain.py
   ```

## �️ Yol Haritası (Roadmap)

- [x] **Project Initialization**: Dizin yapısı ve temeller.
- [ ] **Levitation Module**: PID kontrolcüsü ve fizik motoru.
- [ ] **Propulsion Module**: İtki ve sürtünme simülasyonu.
- [ ] **GUI Dashboard**: PyQt5 tabanlı gerçek zamanlı veri izleme.
- [ ] **Final Test**: Tam sistem entegrasyon testi.

---
<div align="center">
    <i>"Gelecek, hızlanarak gelir."</i><br>
    <b>TEKNOFEST 2025 HYPERLOOP TEAM</b>
</div>

