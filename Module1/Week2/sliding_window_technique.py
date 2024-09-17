def max_sliding_window(k, n):
    num_list = []
    result = []
    sub_list = []
    print(f"Nhập {n} phần tử của list:")
    for i in range(n):
        num = int(input(f"Nhập phần tử thứ {i + 1}: "))
        num_list.append(num)

    for element in num_list:
        sub_list.append(element)

        if len(sub_list) == k:
            result.append(max(sub_list))
            del sub_list[0]

    return result
    
if __name__ == "__main__":
    n = int(input("Nhập số lượng phần tử của list (n): "))
    k = int(input("Nhập kích thước cửa sổ (k): "))

    result = max_sliding_window(k, n)
    print("Result:", result)