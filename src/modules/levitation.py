import time

class LevitationController:
    """
    PID Controller for Hyperloop Pod Levitation System.
    Maintains the air gap between the pod and the track.
    """
    def __init__(self, target_gap=10.0, kp=1.5, ki=0.2, kd=0.05):
        self.target_gap = target_gap  # Target air gap in mm
        self.kp = kp
        self.ki = ki
        self.kd = kd
        
        self.prev_error = 0
        self.integral = 0
        self.current_gap = 0.0 # Initial gap (resting on track)
        
        # Simulation parameters
        self.levitation_active = False

    def activate(self):
        print("[LEV] Systems charging... Magnetic field initialized.")
        time.sleep(1)
        self.levitation_active = True
        print("[LEV] Levitation ACTIVE. Target Gap: {}mm".format(self.target_gap))

    def update(self, current_gap_sensor_val, dt):
        """
        Calculates the control output (Current Adjustment) based on PID.
        """
        if not self.levitation_active:
            return 0

        error = self.target_gap - current_gap_sensor_val
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        
        self.prev_error = error
        return output

    def simulate_gap_change(self, control_output):
        """
        Simulates the physical response of the pod to the magnetic force.
        """
        # Simplified physics: Force lifts the pod, Gravity pulls it down.
        # This is just a mock response for the demo.
        lift_factor = 0.1
        self.current_gap += control_output * lift_factor
        
        # Mechanical limits
        if self.current_gap < 0: self.current_gap = 0
        if self.current_gap > 20: self.current_gap = 20 # Max lift height
        
        return self.current_gap
