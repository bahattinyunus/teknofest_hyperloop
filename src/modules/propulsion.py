class PropulsionEngine:
    """
    Simulates the Linear Induction Motor (LIM) or Linear Synchronous Motor (LSM).
    Calculates Thrust, Velocity and Acceleration.
    """
    def __init__(self):
        self.velocity = 0.0 # km/h
        self.thrust = 0.0 # Newtons
        self.is_active = False
        
    def activate(self):
        print("[PROP] Inverters online. HV Battery connected.")
        self.is_active = True

    def calculate_physics(self, throttle_percent, dt):
        """
        Updates velocity based on throttle and mock drag.
        throttle_percent: 0.0 to 1.0
        """
        if not self.is_active:
            return 0.0

        # Constants
        MAX_THRUST = 5000 # N
        MASS = 500 # kg (Pod weight)
        DRAG_COEFF = 0.02 # Low pressure environment drag
        
        # Force Calculation
        thrust_force = throttle_percent * MAX_THRUST
        drag_force = DRAG_COEFF * (self.velocity ** 2)
        net_force = thrust_force - drag_force
        
        # F = ma -> a = F/m
        acceleration = net_force / MASS
        
        # v = u + at
        self.velocity += (acceleration * dt) * 3.6 # Convert m/s to km/h for display
        
        if self.velocity < 0:
            self.velocity = 0
            
        return self.velocity

    def emergency_brake(self):
        print("[PROP] ! EMERGENCY BRAKING ! Reverse thrust applied.")
        self.velocity = 0 # Instant stop for safety demo (in reality, high negative G)
