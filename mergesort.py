def merge_sort(a):
    if len(a) > 1:
        m = len(a) // 2
        print("Current array: ", a)
        
        # Split the array into two halves
        left_half = a[:m]
        right_half = a[m:]
        
        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the two halves
        merge(a, left_half, right_half)

def merge(a, left_half, right_half):
    i = 0  # index for left_half
    j = 0  # index for right_half
    k = 0  # index for main array
    
    # Merge the two halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            a[k] = left_half[i]
            i += 1
        else:
            a[k] = right_half[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of left_half, if any
    while i < len(left_half):
        a[k] = left_half[i]
        i += 1
        k += 1
    
    # Copy the remaining elements of right_half, if any
    while j < len(right_half):
        a[k] = right_half[j]
        j += 1
        k += 1
    
    print("Merged array: ", a)

a = [1, 7, 6, 4, 2, 5, 3, 8]
merge_sort(a)
print("Sorted array: ", a)
