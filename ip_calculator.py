# R = (Nhu cầu trung bình * Thời gian giao hàng trung bình) + Tồn kho an toàn
# R (Reorder Point), Điểm đặt hàng 
# Q (Quantity)
# IP — Inventory Position)
# SR — Seheduled receipts) (đã đặt và sắp giao từ đơn hàng trước).
# OH — On-hand inventory) (hàng hiện có trong kho).
# BO - Backorders). 10 cuốn (khách đã đặt nhưng hết hàng, đang nợ).
# IP = OH + SR - BO
# Ví dụ minh họa

# Mô hình quản trị hàng tồn kho liên tục được sử dụng để theo dõi số
# lượng tồn kho còn lại của một mặt hàng mỗi khi hàng hóa đó được xuất kho
# để xác định thời điểm tiến hành đặt hàng. Khi mức tồn kho chạm ngưỡng
# tồn kho tối thiểu đã được xác định trước, hay còn gọi là điểm đặt hàng R
# (Reorder Point), một lượng hàng hóa Q (Quantity) cố định sẽ được đặt hàng
# bổ sung. Mức tổn kho (kí hiệu là IP — Inventory Position) sẽ bao gồm hàng
# nhập kho theo kế hoạch (kí hiệu là SR — Seheduled receipts), hàng tồn kho
# hiện có (kí hiệu là OH — On-hand inventory), và đơn hàng dự trữ (kí hiệu là BO - Backorders). Hàng nhập kho theo kế hoạch là đơn hàng đã được đặt
# nhưng chưa nhận hàng. Đơn hàng dự trữ là số lượng hàng chưa được đáp
# ứng của đơn hàng mà khách hàng đã đặt do hết hàng tồn kho. Cụ thể, mức
# tồn kho sẽ được xác định như sau:

# Giả sử anh quản lý một cửa hàng bán sách. Mặt hàng là sách "Harry Potter", 
# với nhu cầu trung bình 10 cuốn/ngày, thời gian giao hàng từ nhà cung cấp là 5 ngày, 
# và tồn kho an toàn là 20 cuốn. Điểm đặt hàng R = (10 cuốn/ngày * 5 ngày) + 20 = 70 cuốn.

def  calculate_inventory_position(OH, SR, BO):
    "Tính mức tồn kho IP:"
    return OH + SR - BO

def check_reorder_point(IP, R, Q):
    """Kiểm tra và quyết định đặt hàng."""
    if IP <= R:
        return f"Đặt hàng ngay! Mức tồn kho đã chạm ngưỡng. Đặt bổ sung: {Q} đơn vị."
    else:
        return "Chưa cần đặt hàng."

OH = 50  # Hàng tồn kho hiện có
SR = 30  # Hàng nhập kho theo kế hoạch
BO = 10  # Đơn hàng dự trữ
R = 70   # Điểm đặt hàng = (10 * 5) + 20 = 70 
Q = 100  # Số lượng đặt hàng cố định

IP = calculate_inventory_position(OH, SR, BO)
status = check_reorder_point(IP, R, Q)

print(f"Mức tồn kho (IP): {IP} đơn vị")
print(f"Trạng thái: {status}")


