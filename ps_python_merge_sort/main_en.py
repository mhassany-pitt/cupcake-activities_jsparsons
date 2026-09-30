def merge(data):
    if len(data) <= 1:
        return data
    middle = len(data)//2
    left = merge(data[:middle])
    right = merge(data[middle:])
    return merge_sort(left, right)
