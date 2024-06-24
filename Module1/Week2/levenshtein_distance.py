def levenshtein_distance(token1, token2):
    m = len(token1)
    n = len(token2)
    distances = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        distances[i][0] = i

    for j in range(n + 1):
        distances[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if token1[i - 1] == token2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                insert_cost = distances[i][j - 1]
                delete_cost = distances[i - 1][j]
                replace_cost = distances[i - 1][j - 1]
                distances[i][j] = min(insert_cost, delete_cost, replace_cost) + 1

    return distances[m][n]

if __name__ == "__main__":
    token1 = input("Nhập chuỗi thứ nhất: ")
    token2 = input("Nhập chuỗi thứ hai: ")

    distance = levenshtein_distance(token1, token2)
    print(f"Khoảng cách Levenshtein giữa '{token1}' và '{token2}' là: {distance}")
