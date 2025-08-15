def calculate_volumetric_weight(length, width, height, quantity, unit="cm3", divisor_m3=167, divisor_cm3=6000):
    """
        Tính trọng lượng thể tích dựa trên kích thước, số lượng, và đơn vị.
        length, width, height: Kích thước mỗi thùng (m hoặc cm).
        quantity: Số lượng thùng.
        unit: Đơn vị ('m3' hoặc 'cm3').
        divisor_m3: Hệ số cho m³ (mặc định 167).
        divisor_cm3: Hệ số cho cm³ (mặc định 6000).
    """
    volume = length * width * height * quantity
    if unit == "m3":
        volumetric_weight = volume * divisor_m3
    elif unit == "cm3":
        volumetric_weight = volume / divisor_cm3
    else:
        raise ValueError("Đơn vị phải là 'm3' hoặc 'cm3'")
    
    return volumetric_weight, volume

def calculate_chargeable_weight(actual_weight, length, width, height, quantity, unit="cm3", divisor_m3=167, divisor_cm3=6000):
    """
    Tính trọng lượng tính cước dựa trên trọng lượng thực tế và thể tích.
    actual_weight: Trọng lượng thực tế tổng (kg).
    """
    volumetric_weigh, _ = calculate_volumetric_weight(length, width, height, quantity, unit, divisor_m3, divisor_cm3)
    chargeable_weight = max(actual_weight, volumetric_weigh)
    return chargeable_weight

def calculate_cost(chargeable_weight, rate_per_kg):
    """
    Tính chi phí vận chuyển dựa trên trọng lượng tính cước và giá mỗi kg.
    rate_per_kg: Giá vận chuyển mỗi kg (USD).
    """
    return chargeable_weight * rate_per_kg

# Ví dụ 1: Lô hàng 50 thùng vải
actual_weight_fabric = 50 * 15  # 750 kg
length_m_fabric = 0.5  # m
width_m_fabric = 0.5   # m
height_m_fabric = 0.5  # m
length_cm_fabric = 50  # cm
width_cm_fabric = 50   # cm
height_cm_fabric = 50  # cm
quantity_fabric = 50
rate_per_kg = 10  # USD/kg

# Tính với đơn vị m³
volumetric_weight_fabric_m3, volume_m3 = calculate_volumetric_weight(length_m_fabric, width_m_fabric, height_m_fabric, quantity_fabric, unit="m3")
chargeable_weight_fabric_m3 = calculate_chargeable_weight(actual_weight_fabric, length_m_fabric, width_m_fabric, height_m_fabric, quantity_fabric, unit="m3")
cost_fabric_m3 = calculate_cost(chargeable_weight_fabric_m3, rate_per_kg)

# Tính với đơn vị cm³
volumetric_weight_fabric_cm3, volume_cm3 = calculate_volumetric_weight(length_cm_fabric, width_cm_fabric, height_cm_fabric, quantity_fabric, unit="cm3")
chargeable_weight_fabric_cm3 = calculate_chargeable_weight(actual_weight_fabric, length_cm_fabric, width_cm_fabric, height_cm_fabric, quantity_fabric, unit="cm3")
cost_fabric_cm3 = calculate_cost(chargeable_weight_fabric_cm3, rate_per_kg)


print("Lô hàng 50 thùng vải (đơn vị m³):")
print(f"Trọng lượng thực tế: {actual_weight_fabric} kg")
print(f"Thể tích: {volume_m3:.2f} m³")
print(f"Trọng lượng thể tích: {volumetric_weight_fabric_m3:.2f} kg")
print(f"Trọng lượng tính cước: {chargeable_weight_fabric_m3:.2f} kg")
print(f"Chi phí vận chuyển: {cost_fabric_m3:.2f} USD")

print("\nLô hàng 50 thùng vải (đơn vị cm³):")
print(f"Trọng lượng thực tế: {actual_weight_fabric} kg")
print(f"Thể tích: {volume_cm3} cm³")
print(f"Trọng lượng thể tích: {volumetric_weight_fabric_cm3:.2f} kg")
print(f"Trọng lượng tính cước: {chargeable_weight_fabric_cm3:.2f} kg")
print(f"Chi phí vận chuyển: {cost_fabric_cm3:.2f} USD")

