import sys
import time
import random
import os

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.modules.levitation import LevitationController
from src.modules.propulsion import PropulsionEngine

class HyperBrain:
    def __init__(self):
        self.levitation = LevitationController(target_gap=12.0)
        self.propulsion = PropulsionEngine()
        self.param_dt = 0.1 # Time step
        self.mission_time = 0

    def boot_sequence(self):
        print("\n" + "="*50)
        print("   H Y P E R L O O P   O S   v 4 . 0")
        print("   T E K N O F E S T   2 0 2 5   M I S S I O N")
        print("="*50 + "\n")
        
        steps = ["Initializing Core...", "Checking Sensors...", "Calibrating IMU...", "Connecting Telemetry..."]
        for step in steps:
            print(f"[SYS] {step}")
            time.sleep(0.5)
        
        print("[SYS] SYSTEM READY. Waiting for command...")

    def run_mission_simulation(self):
        """
        Runs a predefined mission profile: Hover -> Accelerate -> Cruise -> Brake
        """
        self.levitation.activate()
        self.propulsion.activate()
        
        print("\n[MSN] MISSION START: STATION A -> STATION B")
        print("-" * 60)
        print("{:<10} | {:<15} | {:<15} | {:<10}".format("TIME (s)", "SPEED (km/h)", "GAP (mm)", "STATUS"))
        print("-" * 60)

        # Simulation Loop
        for i in range(100):
            self.mission_time += self.param_dt
            
            # --- Logic / State Machine ---
            throttle = 0.0
            status = "IDLE"
            
            if self.mission_time < 2.0:
                # Hover check
                status = "LEVITATING"
            elif self.mission_time < 7.0:
                # Acceleration Phase
                throttle = 0.8
                status = "ACCEL"
            elif self.mission_time < 9.0:
                # Coasting
                throttle = 0.0
                status = "COAST"
            else:
                # Braking
                throttle = -0.5 # Braking is handled differently in real physics, simplified here
                self.propulsion.velocity *= 0.9 # Mock braking friction
                status = "BRAKING"
            
            # --- Physics Updates ---
            
            # 1. Levitation Logic (PID manages gap)
            # Add some random noise to sensor reading
            noise = random.uniform(-0.5, 0.5)
            sensor_gap = self.levitation.current_gap + noise
            pid_out = self.levitation.update(sensor_gap, self.param_dt)
            real_gap = self.levitation.simulate_gap_change(pid_out)
            
            # 2. Propulsion Logic
            speed = self.propulsion.calculate_physics(throttle, self.param_dt)
            
            # --- Telemetry Output ---
            if i % 5 == 0: # Print every 0.5 sec
                print("{:<10.1f} | {:<15.2f} | {:<15.2f} | {:<10}".format(
                    self.mission_time, speed, real_gap, status))
            
            time.sleep(0.05) # Speed up simulation execution slightly

        print("-" * 60)
        print("[MSN] MISSION COMPLETE. POD STOPPED.")

if __name__ == "__main__":
    brain = HyperBrain()
    brain.boot_sequence()
    try:
        input("\nPress ENTER to Ignite Mission Sequence...")
        brain.run_mission_simulation()
    except KeyboardInterrupt:
        print("\n[SYS] EMERGENCY SHUTDOWN TRIGGERED.")
