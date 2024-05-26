#Internet source / insperation: https://www.programiz.com/dsa/merge-sort

#To sort a[left...right] into ascending order:
#1. If left < right:
#1.1. Let m be an integer about midway between left and right.
#1.2. Sort a[left...m] into ascending order.
#1.3. Sort a[m+1...right] into ascending order.
#1.4. Merge a[left...m] and a[m+1...right] into auxiliary array b.
#1.5. Copy all components of b into a[left...right].
#2. Terminate.

# Test Vars: a = [4,3,4,5,2,3,4,6,8,9,10]  # O(1)

# Test Vars: 
a = ["fox", "cow", "pig", "cat", "rat", "lion", "tiger", "goat", "dog"]  # O(1)
# Test Vars: a = [23, 56, 7, 44, 768, 90, 107, 22, 45, 66, 99, 1, 12]  # O(1)

arr = a[:]  # O(n)

def merge_sort(arr):  # O(1)
    if len(arr) <= 1:  # O(1)
        return arr  # O(1)

    # Divide the array into two halves
    mid = len(arr) // 2  # O(1)
    left = arr[:mid]  # O(n)
    right = arr[mid:]  # O(n)

    # Recursively sort each half
    left = merge_sort(left)  # O(log n)
    right = merge_sort(right)  # O(log n)

    # Merge the sorted halves
    return merge(left, right)  # O(n)

def merge(left, right):  # O(1)
    result = []  # O(1)
    left_index = right_index = 0  # O(1)

    while left_index < len(left) and right_index < len(right):  # O(n)
        if left[left_index] < right[right_index]:  # O(1)
            result.append(left[left_index])  # O(1)
            left_index += 1  # O(1)
        else:
            result.append(right[right_index])  # O(1)
            right_index += 1  # O(1)

    # Append the remaining elements of left or right (if any)
    result.extend(left[left_index:])  # O(n)
    result.extend(right[right_index:])  # O(n)

    return result  # O(1)

print(merge_sort(arr))  # O(1)