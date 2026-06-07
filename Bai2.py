product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def is_valid_float(valid_str):
    if valid_str.startswith('-'):
        valid_str = valid_str[1:]
       
    if valid_str.count('.') <= 1:
        clean_str = valid_str.replace('.', '', 1)
        if clean_str.isdigit() and len(clean_str) > 0:
            return True
    return False

def parse_product(product_str):
    parts = product_str.split("-")
    if len(parts) != 4:
        print(f"Bỏ qua sản phẩm {parts[0]} do sai cấu trúc dữ liệu.")
        return None
        
    product_id, name, price_str, rating_str = parts

    cleaned_price = "".join([c for c in price_str if c.isdigit()])
    if cleaned_price == "":
        print(f"Bỏ qua sản phẩm {product_id} do giá tiền không hợp lệ.")
        return None

    if not is_valid_float(rating_str):
        print(f"Bỏ qua sản phẩm {product_id} do đánh giá không hợp lệ.")
        return None

    return {
        "id": product_id,
        "name": name,
        "price": int(cleaned_price),
        "rating": float(rating_str)
    }

def display_labels():
    print("\n--- DANH SÁCH TEM NHÃN ---")
    template = "Mã: {id:<10} | Tên: {name:<20} | Giá: {formatted_price} VND | Rating: {rating}*"
    for product in product_list:
        data = parse_product(product)
        if data is not None:
            data["formatted_price"] = f"{data['price']:,}"
            print(template.format_map(data))

def smart_sort():
    global product_list
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    valid_products = []
    for product in product_list:
        parsed = parse_product(product)
        if parsed:
            valid_products.append(parsed)

    valid_products.sort(key=lambda x: (-x['rating'], x['price']))

    product_list = [f"{p['id']}-{p['name']}-{p['price']}-{p['rating']}" for p in valid_products]
    
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    for index, p in enumerate(product_list, 1):
        print(f"{index}. {p}")

def calculate_total_value():
    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    prices = []
    for p in product_list:
        parsed = parse_product(p)
        if parsed:
            prices.append(parsed['price'])
            
    if not prices:
        print("Không có sản phẩm hợp lệ để tính tổng.")
        return 0
        
    total_value = 0
    for price in prices:
        total_value += price

    print(f"Tổng giá trị các mặt hàng hiện tại là: {total_value:,} VND.")
    return total_value

def main():
    while True:
        print("\n============= E-COMMERCE ANALYTICS =============")
        print("1. Hiển thị tem nhãn sản phẩm (format_map & F-String)")
        print("2. Sắp xếp sản phẩm thông minh (sort key)")
        print("3. Tính tổng giá trị kho hàng (reduce)")
        print("4. Đóng hệ thống")
        print("================================================")
        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            display_labels()
        elif choice == "2":
            smart_sort()
        elif choice == "3":
            calculate_total_value()
        elif choice == "4":
            print("Đã đóng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 4!")

if __name__ == "__main__":
    main()