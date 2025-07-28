import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 15) # day from 1 to 14 
demand = np.array([50, 60, 40, 70, 30, 80, 20, 90, 50, 60, 40, 70, 30, 80])
R = 400 # point ordering
Q = 300 #  quality ordering
lead_time = 5 # dilivery time (day)
OH = 500 # quality begining envontory 
SR = 0 # quality imported flow to original plan
BO = 0 # initial reserve unit # Đơn hàng dự trữ ban đầu

inventory = [OH]
order_placed_day = None
for day, d in enumerate(demand, start=1):
    current_inventory = inventory[-1] - d
    if current_inventory < 0:
        BO += abs(current_inventory)
    if current_inventory <= R and order_placed_day is None:
        print(f"Ngày {day}: Tồn kho {current_inventory} < R={R}. Đặt hàng {Q} chiếc.")
        order_placed_day = day
    if order_placed_day and day == order_placed_day + lead_time:
        current_inventory += Q
        print(f"Ngày {day}: Hàng {Q} chiếc về. Tồn kho cập nhật: {current_inventory}")
    inventory.append(current_inventory)


# Vẽ biểu đồ
plt.figure(figsize=(12, 6))
plt.plot(days, inventory[:-1], label='Tồn kho', color='blue', linewidth=2)
plt.axhline(y=R, color='red', linestyle='--', label=f'Điểm đặt hàng R = {R}')
plt.fill_between(days, 0, inventory[:-1], where=(np.array(inventory[:-1]) <= R), color='pink', alpha=0.3, label='Khu vực dưới R')
plt.xticks(days)
plt.xlabel('Ngày', fontsize=12)
plt.ylabel('Số lượng tồn kho (chiếc)', fontsize=12)
plt.title('Quá trình tồn kho từ ngày 1 đến 14 (Trường hợp 2)', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# In kết quả chi tiết
print("Tồn kho theo ngày:", [f"{d}: {inv}" for d, inv in zip(days, inventory[:-1])])
print(f"Tổng BO (nếu có): {BO} chiếc")

plt.show()