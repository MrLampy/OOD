def insert_recur(sort_list, value):
    if not sort_list or value < sort_list[0]:
        return [value] + sort_list
    return [sort_list[0]] + insert_recur(sort_list[1:], value)

def find_index_recur(Alist, new_sorted, index=0):
    if index >= len(Alist) or Alist[index] != new_sorted[index]:
        return index
    return find_index_recur(Alist, new_sorted, index + 1)

def sort_recur(arr, Alist=[], mode = 0):
    if not arr:
        return Alist
    
    new_sorted = insert_recur(Alist, arr[0])
    insert_index = find_index_recur(Alist, new_sorted)
    
    if mode:
        if arr[1:]:
            print(f'insert {arr[0]} at index {insert_index} : {new_sorted} {arr[1:]}')
        else:
            print(f'insert {arr[0]} at index {insert_index} : {new_sorted}')
    if insert_index == 0: mode = 1
    
    return sort_recur(arr[1:], new_sorted, mode)

user_input = [int(i) for i in input('Enter Input : ').split()]
sorted_list = sort_recur(user_input)
print("sorted")
print(sorted_list)