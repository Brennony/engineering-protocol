# Brennon York  |  Search Algorithms  |  9/17/2025



def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left,right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1



if __name__ == "__main__":
    data = [877, 378, 844, 508, 891, 98, 421, 693, 293, 548, 999,
            524, 708, 893, 350, 92, 827, 529, 569, 768, 367, 123,
            868, 321, 640, 32, 94, 519, 502, 626, 637, 688, 513,
            381, 391, 141, 687, 846, 513, 893, 93, 806, 611, 843]
    print(
        "Data:\n"
        f"{data}\n"
    )

    sorted_data = merge_sort(data)
    print(
        "Sorted Data:\n"
        f"{sorted_data}"
    )