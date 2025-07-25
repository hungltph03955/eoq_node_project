import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu từ bài toán
D = 1040  # Nhu cầu hàng năm (20 chiếc/tuần × 52 tuần)
S = 60    # Chi phí đặt hàng mỗi lần (USD)
H = 25    # Chi phí lưu kho mỗi chiếc mỗi năm (25% × 100 USD)
Q = np.arange(50, 1000, 5)  # Phạm vi số lượng đặt hàng, bước nhảy 5 để chính xác hơn
print(Q);

# Tính toán chi phí
# ordering_cost = (D / Q) * S * np.ceil(D / Q)  # Chi phí đặt hàng
# holding_cost = (Q / 2) * H                    # Chi phí lưu kho
# total_cost = ordering_cost + holding_cost     # Tổng chi phí
ordering_cost = (D / Q) * S     # Chi phí đặt hàng (liên tục)
holding_cost = (Q / 2) * H      # Chi phí lưu kho
total_cost = ordering_cost + holding_cost  # Tổng chi phí

# Tính EOQ
EOQ = np.sqrt((2 * D * S) / H) # căn bậc 2 
min_total_cost = (D / EOQ) * S + (EOQ / 2) * H

# Tìm chỉ số gần nhất của EOQ trong mảng Q
closestQIndex = np.abs(Q - EOQ).argmin()
closestQ = Q[closestQIndex]
intersection_holding_cost = holding_cost[closestQIndex]
intersection_ordering_cost = ordering_cost[closestQIndex]

# Kiểm tra lý thuyết tại EOQ
print(f"Tại EOQ ≈ {EOQ:.2f} chiếc:")
print(f"Chi phí đặt hàng: {(D / EOQ) * S:.2f} USD")
print(f"Chi phí lưu kho: {(EOQ / 2) * H:.2f} USD")
print(f"Tổng chi phí: {min_total_cost:.2f} USD")
print("(Hai chi phí bằng nhau, khớp lý thuyết)")

# Vẽ biểu đồ
plt.figure(figsize=(12, 8))  # Kích thước lớn hơn để dễ đọc
plt.plot(Q, holding_cost, label='Chi phí lưu kho', color='red', linewidth=2)
plt.plot(Q, ordering_cost, label='Chi phí đặt hàng', color='blue', linewidth=2)
plt.plot(Q, total_cost, label='Tổng chi phí', color='green', linewidth=2)

# Đánh dấu điểm EOQ
plt.axvline(x=closestQ, color='purple', linestyle='--', label=f'EOQ ≈ {EOQ:.0f} chiếc (gần {closestQ})')
plt.scatter(closestQ, intersection_holding_cost, color='purple', s=100, label='Giao điểm chi phí lưu kho')
plt.scatter(closestQ, intersection_ordering_cost, color='purple', s=100, label='Giao điểm chi phí đặt hàng')
plt.axhline(y=min_total_cost, color='orange', linestyle='--', label=f'Tổng chi phí tối thiểu ≈ {min_total_cost:.0f} USD')

# Tùy chỉnh biểu đồ
plt.xlabel('Số lượng đặt hàng (chiếc)', fontsize=12)
plt.ylabel('Chi phí (USD)', fontsize=12)
plt.title('Mối quan hệ chi phí tồn kho và số lượng đặt hàng', fontsize=14, pad=15)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()

# Tính chi phí cụ thể
Q1, Q2 = 400, 500
total_cost_400 = (D / Q1 * S * np.ceil(D / Q1)) + (Q1 / 2) * H
total_cost_500 = (D / Q2 * S * np.ceil(D / Q2)) + (Q2 / 2) * H
print(f"Chi phí tồn kho với 400 chiếc: {total_cost_400:.0f} USD")
print(f"Chi phí tồn kho với 500 chiếc: {total_cost_500:.0f} USD")