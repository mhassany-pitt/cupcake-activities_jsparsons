def quick_sort(data, first, last):
    if first < last:
        pivot = partition(data, first, last)
        quick_sort(data, first, pivot-1)
        quick_sort(data, pivot+1, last)
    return data
