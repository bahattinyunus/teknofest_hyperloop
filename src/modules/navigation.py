import time

class NavigationSystem:
    """
    Hyperloop Navigation System (Section 7 Specs).
    Calculates position and speed using the reflector strip system.
    """
    def __init__(self):
        self.total_track_length = 208 # m
        self.race_parkour_length = 186 # m
        self.reflector_count = 0
        self.position = 0.0 # m
        self.current_speed = 0.0 # m/s
        
        # Spec 7.b: Reflector every 4m after first 6m.
        self.reflector_interval = 4.0
        self.first_reflector_pos = 6.0
        
    def update_from_reflector(self, sensor_trigger):
        """
        Updates position based on reflector detection (Spec 7a).
        """
        if sensor_trigger:
            self.reflector_count += 1
            self.position = self.first_reflector_pos + (self.reflector_count - 1) * self.reflector_interval
            print(f"[NAV] Reflector {self.reflector_count} detected. Position: {self.position}m")
            
    def check_zone(self):
        """
        Checks if the pod is in specific markers (Spec 7f, 7g).
        """
        # "Son 100m" check
        if 86 <= self.position < 100:
            return "PRE-FINISH ZONE (TRANSITION)"
        # "Son 48m" check
        if 160 <= self.position:
            return "END OF TRACK MARKER"
        return "RACING"

    def sensor_fusion_check(self, imu_speed, encoder_speed):
        """
        Spec 7e: Enkoder/İvmeölçer are secondary.
        """
        # Simplified validation
        avg_secondary = (imu_speed + encoder_speed) / 2
        return avg_secondary
