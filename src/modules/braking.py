import time

class BrakingSystem:
    """
    Hyperloop Braking System (Section 4 Specs).
    Includes dual independent mechanisms and fail-safe logic.
    """
    def __init__(self):
        self.front_brake_active = False
        self.rear_brake_active = False
        self.emergency_mode = False
        self.buildup_time = 0.2  # Max 0.5s per Spec 4(k)
        
    def activate_full_braking(self):
        """
        Activates both front and rear brakes simultaneously (Spec 4b).
        """
        print("[BRAKE] Activating Dual Independent Braking Systems...")
        time.sleep(self.buildup_time) # Simulate mechanical buildup
        self.front_brake_active = True
        self.rear_brake_active = True
        print("[BRAKE] Brakes DEPLOYED. Dual system functional.")

    def fail_safe_check(self, pressure_lost=False, power_lost=False):
        """
        Fail-safe activation (Spec 4i).
        """
        if pressure_lost or power_lost:
            print("[BRAKE] FAIL-SAFE TRIGGERED: Engaging brakes automatically.")
            self.activate_full_braking()
            return True
        return False

    def get_status_visual(self):
        """
        Visual status indicator logic (Spec 4l).
        """
        if self.front_brake_active and self.rear_brake_active:
            return "READY/ENGAGED (RED LIGHT)"
        return "DISENGAGED (GREEN LIGHT)"
