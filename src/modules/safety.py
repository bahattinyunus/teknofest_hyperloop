import time

class SafetySystem:
    """
    Hyperloop Safety & BMS Management (Section 8 Specs).
    Monitors battery temperature, voltage, and emergency conditions.
    """
    def __init__(self, cells_count=100):
        self.cells_count = cells_count
        # Spec 8.g: 1 sensor per 10 cells
        self.temp_sensors_count = max(1, cells_count // 10)
        self.temperatures = [25.0] * self.temp_sensors_count # Initial degrees Celsius
        self.emergency_stop_triggered = False
        
    def monitor_bms_health(self):
        """
        Continuous health monitoring (Spec 8f, 8z).
        """
        max_temp = max(self.temperatures)
        
        # Spec 8.j: Ideal shutdown at 55 degrees
        if max_temp >= 55.0:
            print(f"[SAFETY] CRITICAL TEMP DETECTED: {max_temp}C. Emergency shutdown!")
            self.emergency_stop_triggered = True
            return False
            
        # Spec 8.i: Buzzer/Flasher check (Simulated)
        if max_temp >= 45.0:
            print(f"[SAFETY] WARNING: High temperature ({max_temp}C). Activating Buzzer (80dB).")
            
        return True

    def trigger_emergency_stop(self, reason="Manual/Signal"):
        """
        Immediate shutdown (Spec 8b).
        """
        print(f"[SAFETY] ! EMERGENCY STOP ({reason}) !")
        self.emergency_stop_triggered = True
        return True
