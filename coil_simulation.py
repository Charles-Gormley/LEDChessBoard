import math

# Coil Inductance Calculator (Wheeler's Formula)
def calculate_inductance_flat_spiral(N, r_outer, wire_diameter):
    """
    Calculate the inductance of a flat spiral coil using Wheeler's formula.
    Parameters:
      N             : Number of turns
      r_outer       : Outer radius (in inches)
      wire_diameter : Diameter of the wire (in inches)
    Returns:
      L_H : Inductance in Henries
    """
    r_inner = r_outer - N * wire_diameter
    if r_inner <= 0:
        raise ValueError("Adjust the coil parameters: r_inner must be positive.")
    r_avg = (r_outer + r_inner) / 2
    w = r_outer - r_inner  # Total radial width
    L_microH = (r_avg**2 * N**2) / (8 * r_avg + 11 * w)  # Inductance in microhenries
    return L_microH * 1e-6  # Convert to Henries

# Coil Voltage Calculator
def calculate_coil_voltage(I_target, L, frequency):
    """
    Calculate the voltage required across the coil.
    Parameters:
      I_target  : Desired current (A)
      L         : Inductance (H)
      frequency : Operating frequency (Hz)
    Returns:
      V_required : Required voltage (V)
    """
    X_L = 2 * math.pi * frequency * L  # Inductive reactance (Ohms)
    return I_target * X_L

# MOSFET Specification Checker
def check_mosfet_specifications(I_required, V_required, I_D_max, V_DS_max, R_DS_on, P_D_max):
    """
    Check if the MOSFET meets the required specifications.
    Parameters:
      I_required : Coil current requirement (A)
      V_required : Voltage across the coil (V)
      I_D_max    : Maximum drain current (A)
      V_DS_max   : Maximum drain-source voltage (V)
      R_DS_on    : On-state resistance (Ohms)
      P_D_max    : Maximum power dissipation (W)
    Returns:
      Dictionary with check results.
    """
    results = {
        "current_ok": I_required <= I_D_max,
        "voltage_ok": V_required <= V_DS_max,
        "P_conduction": I_required**2 * R_DS_on,
    }
    results["power_ok"] = results["P_conduction"] <= P_D_max
    return results

# Example parameters:
N = 10             # Number of turns
r_outer = 3.0      # Outer radius in inches
wire_diameter = 0.025  # Wire diameter in inches (approx. AWG22)

L = calculate_inductance_flat_spiral(N, r_outer, wire_diameter)
I_target = 2.0     # Target current in Amperes
frequency = 100e3  # Operating frequency (100 kHz)
V_required = calculate_coil_voltage(I_target, L, frequency)

print(f"Calculated Inductance: {L:.6e} H")
print(f"Required Coil Voltage at {frequency/1e3:.0f} kHz: {V_required:.2f} V")

# Example MOSFET parameters (based on datasheet values):
I_D_max = 10
V_DS_max = 60
R_DS_on = 0.05
P_D_max = 30

mosfet_status = check_mosfet_specifications(I_target, V_required, I_D_max, V_DS_max, R_DS_on, P_D_max)
print("MOSFET Specification Check:")
for key, value in mosfet_status.items():
    print(f"  {key}: {value}")
