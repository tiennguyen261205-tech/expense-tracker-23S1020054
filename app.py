# Biến toàn cục lưu trữ dữ liệu
expenses = []

def add_expense():
    description = input("Nhập mô tả: ")
    amount = float(input("Nhập số tiền: "))
    
    item = {"description": description, "amount": amount}
    expenses.append(item)

    print("Đã thêm khoản chi thành công!")

def show_expenses():
    if not expenses:
        print("Chưa có khoản chi nào.")
        return

    print("\n--- DANH SÁCH CHI TIÊU ---")
    for i, item in enumerate(expenses, start=1):
        print(f"{i}. {item['description']} - {item['amount']} VND")

def total_expenses():
    print("Chức năng đang được phát triển!")

def main():
    while True:
        print("\n--- QUẢN LÝ CHI TIÊU ---")
        print("1. Thêm khoản chi")
        print("2. Xem danh sách")
        print("3. Tính tổng tiền")
        print("4. Thoát")

        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
