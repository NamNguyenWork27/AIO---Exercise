def count_characters(input_w):
    result_dict = {}
    
    for char in input_w:
        if char in result_dict:
            result_dict[char] += 1
        else:
            result_dict[char] = 1
    
    return result_dict

if __name__ == "__main__":
    input_w = input("Nhập chuỗi cần đếm số lần xuất hiện các ký tự: ")
    result_dict = count_characters(input_w)
    
    print("Số lần xuất hiện của mỗi ký tự trong chuỗi:")
    for char, count in result_dict.items():
        print(f"{char}: {count}")
