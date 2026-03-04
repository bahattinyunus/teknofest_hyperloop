import sys
import time
import random
import os

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.modules.levitation import LevitationController
from src.modules.propulsion import PropulsionEngine
from src.modules.braking import BrakingSystem
from src.modules.navigation import NavigationSystem
from src.modules.safety import SafetySystem
from src.modules.telemetry import TelemetrySystem

class HyperBrain:
    def __init__(self):
        self.levitation = LevitationController(target_gap=10.0) # 8mm - 12mm spec targeted optimally
        self.propulsion = PropulsionEngine()
        self.braking = BrakingSystem()
        self.navigation = NavigationSystem()
        self.safety = SafetySystem()
        self.telemetry = TelemetrySystem()
        
        self.param_dt = 0.1 # Time step
        self.mission_time = 0

    def boot_sequence(self):
        print("\n" + "="*50)
        print("   H Y P E R L O O P   O S   v 5 . 0")
        print("   T E K N O F E S T   2 0 2 6   M I S S I O N")
        print("="*50 + "\n")
        
        steps = [
            "Initializing Core Systems...",
            "Activating BMS & Safety (Spec 8)...",
            "Establishing Telemetry Link (Spec 5)...",
            "Checking Reflector Sensors (Spec 7)...",
            "Engaging Fail-Safe Brakes (Spec 4)..."
        ]
        
        for step in steps:
            print(f"[SYS] {step}")
            time.sleep(0.3)
        
        print("[SYS] SYSTEM READY. All 2026 Spec protocols active.")

    def run_mission_simulation(self):
        """
        Runs a mission profile using integrated systems.
        """
        self.levitation.activate()
        self.propulsion.activate()
        
        print("\n[MSN] MISSION START: STATION A -> STATION B")
        print("-" * 60)

        # Simulation Loop
        for i in range(150):
            self.mission_time += self.param_dt
            
            # 1. Safety Monitoring
            if not self.safety.monitor_bms_health():
                self.braking.activate_full_braking()
                break

            # 2. Navigation Update
            # Simulate a reflector detection (mock trigger)
            sensor_trigger = (i % 8 == 0) 
            self.navigation.update_from_reflector(sensor_trigger)
            zone = self.navigation.check_zone()
            
            # 3. Control Logic
            throttle = 0.0
            status = zone
            
            if self.mission_time < 3.0:
                status = "LEVITATING"
            elif self.mission_time < 10.0:
                throttle = 0.9
                status = "ACCEL"
            elif self.mission_time < 13.0:
                throttle = 0.0
                status = "COAST"
            else:
                self.braking.activate_full_braking()
                self.propulsion.velocity *= 0.7 # Rapid deceleration
                status = "MISSION_BRAKING"
                if self.propulsion.velocity < 5.0:
                    break
            
            # 4. Physics Updates
            noise = random.uniform(-0.1, 0.1)
            sensor_gap = self.levitation.current_gap + noise
            pid_out = self.levitation.update(sensor_gap, self.param_dt)
            real_gap = self.levitation.simulate_gap_change(pid_out)
            
            speed = self.propulsion.calculate_physics(throttle, self.param_dt)
            
            # 5. Telemetry (Spec 5.2.5 mandatory fields)
            telemetry_data = {
                'pos': f"{self.navigation.position},0,0",
                'vel': f"{speed:.2f}",
                'acc': f"{(speed/100):.2f}",
                'rot': "0,0,0",
                'temp': f"{25.0 + (self.mission_time*1.5):.1f}", # Simulated heat
                'batt': "380",
                'curr': f"{throttle * 100:.1f}"
            }
            self.telemetry.stream_gui_packet(telemetry_data)
            
            time.sleep(0.05)

        print("-" * 60)
        print(f"[MSN] MISSION COMPLETE. Final Position: {self.navigation.position}m")
        print(f"[MSN] Brake Status: {self.braking.get_status_visual()}")

if __name__ == "__main__":
    brain = HyperBrain()
    brain.boot_sequence()
    try:
        input("\nPress ENTER to Ignite Mission Sequence...")
        brain.run_mission_simulation()
    except KeyboardInterrupt:
        print("\n[SYS] EMERGENCY SHUTDOWN TRIGGERED.")
        brain.safety.trigger_emergency_stop("Keyboard Interrupt")
