def find_subsets(nums, target):
    results_by_len = [[] for _ in range(len(nums) + 1)]
    
    def backtrack(index, current):
        if index == len(nums):
            if sum(current) == target and current:
                results_by_len[len(current)].append(current[:])
            return
        
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()

        backtrack(index + 1, current)

    backtrack(0, [])

    flattened = []
    for sublist in results_by_len:
        for subset in sublist:
            n = len(subset)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if subset[j] > subset[j + 1]:
                        subset[j], subset[j + 1] = subset[j + 1], subset[j]
                        
        if len(sublist) > 1:
            n = len(sublist)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if sublist[j] > sublist[j+1]:
                        sublist[j], sublist[j+1] = sublist[j+1], sublist[j]
        flattened.extend(sublist)

    return flattened 

user_input = input("Enter Input : ")
user, numbers = user_input.split('/')
user = int(user)
numbers = [int(i) for i in numbers.split()]

subsets = find_subsets(numbers, user)
if not subsets: print("No Subset")
else:
    for subset in subsets: print(subset)