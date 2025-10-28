def auto_int(x):
    return int(x) if x.is_integer() else x

def remove_duplicates_keep_first(arr):
    seen = set()
    result = []
    count = 0
    for item in arr:
        if item not in seen:
            result.append(item)
            seen.add(item)
        else: count += 1
    return (result, count)

# only if the list size is odd number
def get_index(nums : list, target, CO = 0) -> float:
    mid_index = auto_int(len(nums)/2 - 0.5)
    if type(mid_index) == float or mid_index == 0:
        if len(nums) != 2:
            if target < nums[-1]: nums.pop(-1)
            elif target == nums[-1]: return float(len(nums) - 1 + CO)
            elif target == nums[0]: return float(CO)
            elif target > nums[0]:
                    nums.pop(0)
                    CO += 1
            return get_index(nums, target, CO)
        if len(nums) == 2:
            if nums[0] == target: return float(mid_index*2 + CO)
            elif nums[-1] == target: return float(mid_index*2 + CO + 1)
            else:
                if target < nums[0]: return float(mid_index*2 + CO - 0.5)
                elif target > nums[-1]: return float(mid_index*2 + CO + 0.5)
                else:
                    return 'Not work wa'
    if target > nums[mid_index]:
        return get_index(nums[mid_index+1:],target, mid_index)
    elif target == nums[mid_index]:
        return float(mid_index + CO+1)
    else:
        return get_index(nums[:mid_index],target)
    
def get_percentile(nums: list, index, count):
    return (index+1)*100/(len(nums)+count)

if __name__ == '__main__':
    nums, target = input('Enter Input : ').split('/')
    nums = [auto_int(float(i)) for i in nums.strip().split(' ')]
    nums = remove_duplicates_keep_first(nums)
    target = auto_int(float(target))
    nums, count = nums[0],nums[1]
    if target < nums[0]:
        index = -1
        percentile = 0
    elif target > nums[-1]:
        index = 999
        percentile = 100
    elif target == nums[-1]:
        index = float(len(nums)-1)
        percentile = 100
    elif target == nums[0]:
        index = float(0)
        percentile = get_percentile(nums,index, count)
    else:
        index = get_index(nums,target)
        percentile = get_percentile(nums,index, count)
    print(f'\nindex      :   {index}\npercentile :   {percentile}')