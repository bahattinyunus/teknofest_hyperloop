import time

class TelemetrySystem:
    """
    Hyperloop Telemetry & Ground Station Link (Section 5 Specs).
    Handles mandatory 2026 GUI packet structures.
    """
    def __init__(self):
        self.update_freq = 1.0 # Hz (Spec 5.2.5c)
        self.last_update = time.time()
        
    def stream_gui_packet(self, data):
        """
        Spec 5.2.5 requirement for mandatory GUI params.
        """
        current_time = time.time()
        if (current_time - self.last_update) >= (1.0 / self.update_freq):
            print("\n" + "="*40)
            print(" [GROUND STATION TELEMETRY PACKET] ")
            # Mandatory params: X,Y,Z pos/vel/accel, Orientation, Pressure, Temp, Battery
            print(f" > Position:  {data.get('pos', '0,0,0')} m")
            print(f" > Velocity:  {data.get('vel', '0,0,0')} km/h")
            print(f" > Accel:     {data.get('acc', '0,0,0')} g")
            print(f" > Heading:   {data.get('rot', '0,0,0')} (R,P,Y)")
            print(f" > Thermal:   {data.get('temp', '0')} C")
            print(f" > Energy:    {data.get('batt', '0')} V | {data.get('curr', '0')} A")
            print("="*40 + "\n")
            self.last_update = current_time
            return True
        return False
