# Wireless Electric Chess Board – Project Design

## Executive Summary

This project designs a wireless electric chess board that integrates four wireless power coils beneath a 12″ x 12″ wooden board. The board is powered from a standard household outlet by converting mains AC to a regulated DC bus and then generating a high-frequency AC drive (≈40 V, 100 kHz) for the coils. The design leverages off-the-shelf, pre-certified modules to ensure safety and ease-of-integration, making it a suitable project for amateur engineers and hobbyists.

## System Architecture

The design is organized into several key subsystems:

1. **AC-to-DC Power Conversion:**  
   - **Input:** 120/230 V AC mains  
   - **Output:** A regulated DC bus (either 48 V or 24 V with a boost stage)  
   - **Modules:** Pre-certified switching power supplies (e.g., Mean Well RS series)

2. **DC-to-High Frequency AC Inversion:**  
   - Converts the DC bus voltage into a high-frequency AC waveform (≈40 V at 100 kHz) required to drive the wireless coils.  
   - Utilizes resonant or high-frequency inverter modules typically found in wireless charging systems.

3. **Wireless Power Coils:**  
   - Four pre-wound coils (one per quadrant) designed for efficient inductive power transfer at high frequency.  
   - Sourced from established suppliers (e.g., Qi wireless charging modules).

4. **Integration & PCB:**  
   - A custom integration board (or modular protoboard) interconnects all modules, handles control signals, and includes additional safety components (fuses, EMI filters, etc.).

5. **Enclosure & Safety Accessories:**  
   - A robust, non-conductive enclosure houses the system.  
   - Includes proper fusing, overcurrent protection, and isolation to ensure safe operation from a household outlet.

## Block Diagram


```plaintext
       +---------------------+     +----------------------------+
       |    Household AC     | --> | AC-to-DC Power Supply      |
       |  (120/230 V mains)  |     |   (48 V DC or 24 V + boost)|
       +---------------------+     +-------------+--------------+
                                                 |
                                                 v
                                        +-------------------+
                                        |  DC Bus (48 V DC) |
                                        +-------------------+
                                                 |
                                                 v
                                        +-------------------+
                                        | High-Frequency    |
                                        |   Inverter Module |
                                        |  (≈40 V, 100 kHz) |
                                        +-------------------+
                                                 |
                                                 v
                                      +---------------------+
                                      | Wireless Power Coils|
                                      |  (4 Pre-wound Units)|
                                      +---------------------+
```

## Python Calculations for System Modeling

The following Python code simulates the coil design and evaluates the power requirements and MOSFET specifications. Save the code in a file named `coil_simulation.py`.

### Running the Python Script

1. Ensure you have Python installed on your system.
2. Save the provided Python code in a file named `coil_simulation.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where `coil_simulation.py` is saved.
5. Run the script using the command:
   python coil_simulation.py

### Interpreting the Output

- **Calculated Inductance:** The inductance of the coil in Henries.
- **Required Coil Voltage:** The voltage required across the coil at the specified frequency and current.
- **MOSFET Specification Check:** A summary of whether the chosen MOSFET meets the required specifications for current, voltage, and power dissipation.

## Safety Considerations

- **Certified Components:** All AC-to-DC supplies and inverters are UL/CE certified, ensuring isolation, overcurrent, and overvoltage protection.
- **Modular Integration:** Each high-power element is mounted on its own PCB, with the integration board used solely for control and wiring.
- **Enclosure & Fusing:** The final system is housed in a non-conductive, ventilated enclosure with appropriate fusing and EMI filtering to prevent short circuits and overheating.
- **Testing:** Each module is individually tested before final assembly to ensure that all electrical parameters remain within safe limits.

## Conclusion

This project combines off-the-shelf, pre-certified modules with custom integration to deliver a safe and effective wireless power solution for a wooden chess board. The design is modular, scalable, and demonstrative of sound electrical engineering principles—making it an ideal project to showcase on a professional portfolio.
