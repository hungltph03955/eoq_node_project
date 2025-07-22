import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu từ bài toán
D = 1040  # Nhu cầu hàng năm (20 chiếc/tuần × 52 tuần)
S = 60    # Chi phí đặt hàng mỗi lần (USD)
H = 25    # Chi phí lưu kho mỗi chiếc mỗi năm (25% × 100 USD)
Q = np.arange(50, 1000, 10)  # Phạm vi số lượng đặt hàng

# Tính toán chi phí
ordering_cost = (D / Q) * S * np.ceil(D / Q)  # Chi phí đặt hàng
holding_cost = (Q / 2) * H   # Chi phí lưu kho
total_cost = ordering_cost + holding_cost  # Tổng chi phí

# Tính EOQ
EOQ = np.sqrt((2 * D * S) / H)
min_total_cost = (D / EOQ) * S + (EOQ / 2) * H

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))
plt.plot(Q, holding_cost, label='Chi phí lưu kho')
plt.plot(Q, ordering_cost, label='Chi phí đặt hàng')
plt.plot(Q, total_cost, label='Tổng chi phí')
plt.axvline(x=EOQ, color='r', linestyle='--', label=f'EOQ ≈ {EOQ:.0f} chiếc')
plt.axhline(y=min_total_cost, color='g', linestyle='--', label=f'Tổng chi phí tối thiểu ≈ {min_total_cost:.0f} USD')
plt.xlabel('Số lượng đặt hàng (chiếc)')
plt.ylabel('Chi phí (USD)')
plt.title('Mối quan hệ chi phí tồn kho và số lượng đặt hàng')
plt.legend()
plt.grid(True)
plt.show()

# Tính chi phí cụ thể
Q1, Q2 = 400, 500
print(f"Chi phí tồn kho với {Q1} chiếc: {(D/Q1*S*np.ceil(D/Q1) + (Q1/2)*H):.0f} USD")
print(f"Chi phí tồn kho với {Q2} chiếc: {(D/Q2*S*np.ceil(D/Q2) + (Q2/2)*H):.0f} USD")