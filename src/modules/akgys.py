import time

class AKGYS:
    """
    Akıllı Kapsül Güvenlik Yönetim Sistemi (AKGYS) - Section 4 Specs.
    Provides autonomous, sensor-fused risk management and error tolerance.
    """
    def __init__(self):
        self.rpn = 0
        self.status = "NOMINAL"
        self.last_decision = "CONTINUE"
        
    def sensor_fusion(self, temp, pressure, accel):
        """
        Fuses data from multiple sensors to detect anomalies (Bölüm 4, 3.c.i).
        """
        anomalies = 0
        if temp > 60.0: anomalies += 1
        if pressure < 0.5: anomalies += 1 # Bar (Spec assumes pressure drop = failure)
        if abs(accel) > 5.0: anomalies += 1 # Gs (High vibration)
        
        return anomalies

    def perform_risk_analysis(self, anomalies_count):
        """
        Simulated Risk analysis (FMEA/FTA) based on Section 4, 3.c.ii.
        Returns a Risk Priority Number (RPN).
        """
        # Logic: RPN = Severity * Occurrence * Detection (Simplified)
        severity = 10 if anomalies_count > 1 else 5
        occurrence = anomalies_count * 2
        detection = 1 # High detection capability in our digital twin
        
        self.rpn = severity * occurrence * detection
        return self.rpn

    def autonomous_decision_engine(self, current_rpn):
        """
        Autonomous Decision Mechanism (State Machine) - Section 4, 3.c.iv.
        MUST decide within 5 seconds (Spec 4.3.b).
        """
        if current_rpn > 50:
            self.status = "CRITICAL_FAILURE"
            self.last_decision = "AUTO_EMERGENCY_STOP"
        elif current_rpn > 20:
            self.status = "WARNING"
            self.last_decision = "ALERT_OPERATOR"
        else:
            self.status = "NOMINAL"
            self.last_decision = "CONTINUE"
            
        return self.last_decision

    def notify_passengers(self):
        """
        Passenger & Operator notification logic (Bölüm 4, 3.c.vi).
        """
        if self.status == "CRITICAL_FAILURE":
            return "!!! UYARI: KRİTİK HATA TESPİT EDİLDİ. ACİL DURUŞ BAŞLATILIYOR. LÜTFEN SAKİN KALIN !!!"
        elif self.status == "WARNING":
            return "İkaz: Sistem parametreleri sınır değerlere yaklaşıyor. Teknik ekip bilgilendirildi."
        return "Tüm sistemler normal. Yolculuk devam ediyor."

    def monitor(self, temp, pressure, accel):
        """
        High-level supervisor call.
        """
        anomalies = self.sensor_fusion(temp, pressure, accel)
        rpn = self.perform_risk_analysis(anomalies)
        decision = self.autonomous_decision_engine(rpn)
        notification = self.notify_passengers()
        
        return {
            'rpn': rpn,
            'decision': decision,
            'status': self.status,
            'message': notification
        }
