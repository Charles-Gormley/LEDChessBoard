# Wireless Electric Chess Board – Project Costs

## Detailed Module Descriptions & Bill of Materials (BOM)

1. **AC-to-DC Power Supply Module**
   - **Option A: 48 V DC Supply**
     - Description: Regulated 48 V DC output, sufficient for high-frequency inverter headroom.
     - Price Range: $50–$100
     - Vendor Example: Mean Well RS-25-48
     - Safety: UL/CE certified for mains isolation and overcurrent protection.
   - **Option B: 24 V DC Supply + Boost Converter**
     - Description: 24 V DC supply with an additional boost stage to achieve required inverter input.
     - Price Range: $30–$60 (24 V supply) + $20–$40 (boost converter) = $50–$100 total.
     - Vendor Example: Mean Well RS-15-24
     - Safety: Similar certifications apply; additional design care for the boost stage is needed.

2. **DC-to-High Frequency AC Inverter Module**
   - Description: Converts the DC bus voltage to ~40 V AC at 100 kHz.
   - Price Range: $30–$60
   - Vendor Example: Wireless charging transmitter modules (available on Amazon, Alibaba, etc.)
   - Safety: Pre-designed for high-frequency operation with proper EMI filtering and isolation.

3. **Wireless Power Coils**
   - Description: Four pre-wound coils designed for efficient inductive transfer.
   - Price Range: $10–$20 each, total $40–$80.
   - Vendor Example: Qi wireless charging coil modules (sourced from Digi-Key, Mouser, etc.)
   - Safety: Manufactured to industry standards to avoid overheating and ensure efficiency.

4. **Integration Components & PCB/Heat Management**
   - Description: Custom PCB or protoboard to connect modules, additional safety components (fuses, connectors, EMI filters), and optional heat sinks.
   - Price Range: $10 -> $30
   - Vendor Example: JLCPCB, OSH Park for PCB fabrication; Digi-Key for ancillary components.

## Total Estimated Cost

Approximately $80 -> $200 depending on the exact modules and components chosen.
