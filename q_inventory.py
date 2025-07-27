# Giả sử anh quản lý kho linh kiện điện tử, mặt hàng là pin AA. Q = 200 pin (số lượng đặt mỗi lần từ EOQ). R = 50 pin (điểm đặt hàng, dựa trên nhu cầu 10 pin/ngày * 5 ngày giao hàng).

# Cài đặt:
# Ngăn 1: Chứa 150 pin (phần dùng hàng ngày).
# Ngăn 2: Chứa 50 pin (dự phòng = R).
# Quy trình:
# Công nhân lấy pin từ ngăn 1 trước. Sau vài ngày, ngăn 1 hết (trống).
# Chuyển sang lấy từ ngăn 2 (dự phòng 50 pin), đồng thời gửi phiếu đặt hàng sẵn (200 pin) đến nhà cung cấp.
# Trong 5 ngày chờ hàng về, ngăn 2 cung cấp đủ (50 pin > nhu cầu 10*5=50, nhưng có an toàn).
# Hàng mới 200 pin về: Lấp đầy ngăn 2 về 50 pin, dư 150 pin cho ngăn 1.
# Lợi ích: Đơn giản, không cần theo dõi số liệu phức tạp, chỉ dựa vào ngăn trống.

class TowBinSystem:
    def __init__(self, bin1_initial, bin2_level, Q, daily_demand, lead_time):
        self.bin1 = bin1_initial # Ngăn 1 ban đầu
        self.bin2 = bin2_level # Ngăn 2 (R)
        self.Q = Q # Số lượng đặt mỗi lần
        self.daily_demand = daily_demand # Nhu cầu hàng ngày
        self.lead_time = lead_time # Thời gian giao hàng (ngày)
        self.days = 0 # Ngày mô phỏng
        self.order_placed = False # Đơn hàng đã đặt chưa

    def simulate_day(self):
        """Mô phỏng một ngày: Rút hàng và kiểm tra đặt hàng."""
        self.days += 1
        # Rút hàng từ ngăn 1 trước 
        if self.bin1 >= self.daily_demand:
            self.bin1 -= self.daily_demand
            print(f"Ngày {self.days}: Ngăn 1 còn lại là:  {self.bin1} đơn vị.")
        else:
            # lúc này ngăn 1 đã hết và chuyển sang rút ngăn 2
            remaining = self.daily_demand - self.bin1
            self.bin1 = 0
            # đoạn này là trừ lượng mua hàng của ngày hôm nay sang cho ngăn 2 trước
            self.bin2 -= remaining
            print(f"Ngày {self.days}: Ngăn 1 đã hết ngăn 2 còn lại:  {self.bin2} đơn vị.")
            if not self.order_placed:
                print(f"Ngày {self.days}: Ngăn 1 trống! Đặt hàng {self.Q} đơn vị.")
                self.order_placed = True
                self.order_day = self.days
        
        # kiểm tra hàng về sau lead time
        if self.order_placed and self.days == self.order_day + self.lead_time:
            print(f"Ngày {self.days}: Hàng mới {self.Q} đơn vị về.")
            fill_bin2 = min(self.Q, self.bin2_level - self.bin2)
            self.bin2 += fill_bin2
            remaining = self.Q - fill_bin2
            # phần dư thì cho lại vào ngăn 1:
            self.bin1 += remaining
            self.order_placed = False
        
        print(f"Ngày {self.days}: Ngăn 1 = {self.bin1}, Ngăn 2 = {self.bin2}")

system = TowBinSystem(bin1_initial = 150, bin2_level = 50, Q = 200, daily_demand = 10, lead_time = 5)
for _ in range(20): 
    system.simulate_day()