# HyperSystem v4.0 Technical Specifications

## 1. Introduction
The HyperSystem is the "Brain" of the Teknofest 2025 Hyperloop pod. It uses a federated architecture where a central orchestrator (`HyperBrain`) manages specialized sub-modules via a state machine.

## 2. Control Logic

### 2.1 Levitation (MagLev)
We utilize a hybrid EMS/EDS approach.
- **Controller**: Digital PID
- **Formula**: $u(t) = K_p e(t) + K_i \int e(t) dt + K_d \frac{de(t)}{dt}$
- **Sensors**: Laser triangulators (x4)

### 2.2 Propulsion (LIM)
- **Motor Type**: Double-sided Linear Induction Motor (DSLIM).
- **Inverter logic**: Vector Control (FOC) for optimal thrust-to-weight ratio.

## 3. Safety Protocols
- **Heartbeat**: < 20ms required for continued operation.
- **Kill Switch**: Hardware interrupt triggers instant negative torque.

## 4. Telemetry Standard
JSON-based packets over TCP/IP:
```json
{
  "timestamp": 1234567890,
  "state": "ACCEL",
  "sensors": {
    "gap_fr": 10.2,
    "gap_fl": 10.1,
    "speed": 120.5
  },
  "crc": "0xDEADBEEF"
}
```
