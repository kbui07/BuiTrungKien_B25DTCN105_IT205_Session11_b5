product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả sản phẩm")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    match choice:
        case "1":
            if not product_list:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                for index, product in enumerate(product_list, start=1):
                    if product["quantity"] == 0:
                        status = "Hết hàng"
                    elif product["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                    print(
                        f"{index}. Mã SP: {product['product_id']} | "
                        f"Tên: {product['product_name']} | "
                        f"Giá: {product['price']} | "
                        f"Tồn kho: {product['quantity']} | "
                        f"Đã bán: {product['sold']} | "
                        f"Đổi trả: {product['returned']} | "
                        f"Giảm giá: {product['discount']}% | "
                        f"Trạng thái: {status}"
                    )

        case "2":
            product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == product_id:
                    found = True
                    quantity_buy = input("Nhập số lượng khách mua: ")
                    if not quantity_buy.isdigit() or int(quantity_buy) <= 0:
                        print("Số lượng mua không hợp lệ")
                        break
                    quantity_buy = int(quantity_buy)
                    if quantity_buy > product["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                        break

                    discount_price = (product["price"] * (100 - product["discount"]) / 100)
                    total_money = discount_price * quantity_buy
                    product["quantity"] -= quantity_buy
                    product["sold"] += quantity_buy
                    print(f"Tổng tiền khách cần thanh toán: {int(total_money)}")
                    break

            if not found:
                print("Không tìm thấy sản phẩm cần bán")

        case "3":
            product_id = input("Nhập mã sản phẩm khách muốn đổi/trả: ").strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == product_id:
                    found = True
                    return_quantity = input("Nhập số lượng đổi/trả: ")
                    if not return_quantity.isdigit() or int(return_quantity) <= 0:
                        print("Số lượng đổi/trả không hợp lệ")
                        break

                    return_quantity = int(return_quantity)
                    if return_quantity > product["sold"]:
                        print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
                        break

                    discount_price = (product["price"] * (100 - product["discount"]) / 100)
                    refund_money = discount_price * return_quantity

                    product["sold"] -= return_quantity
                    product["quantity"] += return_quantity
                    product["returned"] += return_quantity
                    print(f"Số tiền hoàn lại: {int(refund_money)}")
                    break

            if not found:
                print("Không tìm thấy sản phẩm cần đổi trả")

        case "4":
            product_id = input("Nhập mã sản phẩm cần áp dụng giảm giá: ").strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == product_id:
                    found = True
                    discount = input("Nhập phần trăm giảm giá: ")
                    if not discount.isdigit():
                        print("Phần trăm giảm giá không hợp lệ")
                        break
                    discount = int(discount)
                    if discount < 0 or discount > 70:
                        print("Phần trăm giảm giá không hợp lệ")
                        break

                    product["discount"] = discount
                    print("Áp dụng giảm giá thành công")
                    break

            if not found:
                print("Không tìm thấy sản phẩm")

        case "5":
            product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == product_id:
                    found = True
                    quantity_import = input("Nhập số lượng nhập thêm: ")
                    if not quantity_import.isdigit() or int(quantity_import) <= 0:
                        print("Số lượng nhập kho không hợp lệ")
                        break
                    
                    product["quantity"] += int(quantity_import)
                    print("Nhập kho thành công")
                    break

            if not found:
                print("Không tìm thấy sản phẩm cần nhập kho")

        case "6":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")