# python3

def build_heap(data):
    swaps = []
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    n = len(data)
    index = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] < data[index]:
        index = left
    if right < n and data[right] < data[index]:
        index = right

    if i != index:
        data[i], data[index] = data[index], data[i]
        swaps.append((i, index))
        sift_down(data, index, swaps)

def main():
   
    choice = input("Choose the input method")
    if "F" in choice:
        filename = input()
        if "a" in filename:
            print("File names with letter a are not allowed")
            return
        with open("test/" + filename, 'r') as file:
                    n = int(file.readline())
                    data = list(map(int, file.readline().split()))
                    assert len(data) == n
                    swaps = build_heap(data)
    elif "I" in choice:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
