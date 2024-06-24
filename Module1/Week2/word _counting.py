if __name__ == "__main__":
    with open('/workspaces/AIO---Exercise/Module1/Week2/P1_data.txt', 'r') as f:
        document = f.read()
    words = document.split()

    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    print(counter)

    


