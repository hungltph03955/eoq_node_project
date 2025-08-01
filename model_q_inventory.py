# <P> khoảng thời gian (cố định)
# <Q> số lượng đặt hàng (có thể thay đổi)
# <T> mức tồn kho mục tiêu
# IP = OH + SR - BO
# Số lượng đặt hàng cho đơn hàng mới sẽ là : Q = T - IP
# Giả sử anh quản lý một cửa hàng bán đèn LED:

# Nhu cầu (D): 10 đèn/tuần (cố định). // nhu cầu trong 1 khoảng thời gian cố định 
# Thời gian giao hàng (L): 1 tuần.(7 day) 
# Kỳ kiểm tra định kỳ (P): 2 tuần.
# Tồn kho ban đầu (OH): 50 đèn.
# Hàng đang giao (SR): 0 đèn.
# Đơn hàng dự trữ (BO): 0 đèn.

# Mức tồn kho mục tiêu (T):
# T = D * (P + L) = 10 * (2 + 1) = 30 đèn.

# Mức tồn kho hiện tại (IP):
# IP = OH + SR - BO = 50 + 0 - 0 = 50 đèn.

#Số lượng đặt hàng (Q):
# Q = T - IP = 30 - 50 = -20 (âm, không đặt hàng vì tồn kho đủ).

import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu giả định
D = 10  # Nhu cầu/tuần
L = 1   # Thời gian giao hàng (tuần)
P = 2   # Kỳ kiểm tra định kỳ (tuần)
OH = 50 # Tồn kho ban đầu
SR = 0  # Hàng đang giao
BO = 0  # Đơn hàng dự trữ
weeks = np.arange(1, 9)  # 8 tuần (4 chu kỳ P)
# Mô phỏng tồn kho 

inventory = [OH] # gán mức tồn kho ban đầu 
orders = [] # lưu số lượng đặt hàng 

# for week in weeks:
#     current_inventory = inventory[-1] - D
#     if current_inventory < 0:
#         BO + abs(current_inventory)
#         current_inventory = 0
#     inventory.append(current_inventory)

#     # kiểm tra định kì vào cuối mỗi P 
#     if (week - 1) % P == 0 and week > 1: # bắt đầu từ tuần thứ 2 
#         T = D * (P + L) # mức tồn kho mục tiêu
#         IP = current_inventory + SR - BO
#         # Q số lượng đặt hàng theo định kì 
#         Q = max(0, T - IP) # không đặt số lượng là âm 
#         orders.append(Q)
#         if Q > 0:
#             print(f"Tuần {week}: IP = {IP}, T = {T}, Đặt {Q} đèn (hàng về tuần {week + L}).")
#             SR = Q # hàng đang giao
#         else:
#             orders.append(0)
#             SR = 0
        
#         # Hàng về sau lead time
#     if week > L and (week - L - 1) % P == 0:
#         order_week = week - L
#         if order_week in weeks and orders[weeks.tolist().index(order_week)] > 0: 
#             current_inventory += orders[weeks.tolist().index(order_week)]
#             print(f"Tuần {week}: Hàng {orders[weeks.tolist().index(order_week)]} đèn về từ tuần {order_week}.")
#             SR = 0
#             BO = 0

for week in weeks:
    current_inventory = inventory[-1] - D  # Giảm theo nhu cầu
    if current_inventory < 0:
        BO += abs(current_inventory)
        current_inventory = 0
    inventory.append(current_inventory)
    
    # Kiểm tra định kỳ vào cuối mỗi P
    if (week - 1) % P == 0 and week > 1:  # Bắt đầu từ tuần 2
        T = D * (P + L)  # Mức tồn kho mục tiêu
        IP = current_inventory + SR - BO
        Q = max(0, T - IP)  # Không đặt âm
        orders.append(Q)
        if Q > 0:
            print(f"Tuần {week}: IP = {IP}, T = {T}, Đặt {Q} đèn (hàng về tuần {week + L}).")
            SR = Q  # Hàng đang giao
        else:
            orders.append(0)
            SR = 0

    # Hàng về sau lead time
    if week > L and (week - L - 1) % P == 0:
        # index = (week - L - 1) // P - 1
        index = (week - 1);
        current_inventory += orders[index]
        SR = 0
        BO = 0
    else:
        orders.append(0)

    inventory[-1] = current_inventory
    # Điều chỉnh mảng inventory

inventory = inventory[:-1]
# Vẽ biểu đồ
plt.figure(figsize=(12, 6))
line, = plt.plot(weeks, inventory, label='Tồn kho', color='blue', linewidth=2)
plt.axhline(y=D * L, color='green', linestyle='--', label=f'Tồn kho an toàn = {D*L} đèn')
plt.fill_between(weeks, 0, inventory, where=(np.array(inventory) <= D * L), color='pink', alpha=0.3, label='Khu vực thiếu')
plt.xticks(weeks)
plt.xlabel('Tuần', fontsize=12)
plt.ylabel('Số lượng tồn kho (đèn)', fontsize=12)
plt.title('Quá trình tồn kho theo mô hình P (4 chu kỳ)', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# In kết quả
print("Tồn kho theo tuần:", [f"{w}: {inv}" for w, inv in zip(weeks, inventory)])
print(f"Tổng BO (nếu có): {BO} đèn")
print(f"Số lượng đặt hàng mỗi chu kỳ:", orders)
plt.show()









