def can_partition(lessons, k, max_period_limit):
    if not lessons:
        return True
    
    if any(lesson > max_period_limit for lesson in lessons):
        return False
    
    periods_needed = 1
    current_period_time = 0
    
    for lesson_time in lessons:
        if current_period_time + lesson_time <= max_period_limit:
            current_period_time += lesson_time
        else:
            periods_needed += 1
            current_period_time = lesson_time
            
    return periods_needed <= k

def find_min_max_period(lessons, k):
    if not lessons or k <= 0:
        return 0

    low = max(lessons)
    high = sum(lessons)
    
    min_max_period = high

    while low <= high:
        mid = low + (high - low) // 2
        
        if can_partition(lessons, k, mid):
            min_max_period = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return min_max_period

def reconstruct_groups(lessons, min_max_period):
    groups = []
    current_group = []
    current_sum = 0
    
    for lesson_time in lessons:
        if current_sum + lesson_time <= min_max_period:
            current_group.append(lesson_time)
            current_sum += lesson_time
        else:
            groups.append(current_group)
            current_group = [lesson_time]
            current_sum = lesson_time
            
    if current_group:
        groups.append(current_group)
        
    return groups

def solve_and_display(lessons, k):
    min_max_period = find_min_max_period(lessons, k)
    
    groups = reconstruct_groups(lessons, min_max_period)
    
    while len(groups) < k:
        
        max_sum = -1
        split_index = -1
        
        for i, group in enumerate(groups):
            current_sum = sum(group)
            if len(group) > 1 and current_sum > max_sum: 
                max_sum = current_sum
                split_index = i
        
        if split_index == -1:
            groups.append([])
        else:
            group_to_split = groups.pop(split_index)
            
            new_second_part = [group_to_split[-1]]
            new_first_part = group_to_split[:-1]
            
            groups.insert(split_index, new_first_part)
            groups.insert(split_index + 1, new_second_part)
    
    group_sums = [sum(g) for g in groups]
    
    max_sum = max(group_sums) if group_sums else 0
    
    non_zero_sums = [s for s in group_sums if s > 0]
    min_sum = min(non_zero_sums) if non_zero_sums else 0 
    
    diff = max_sum - min_sum

    print(f"Max period: {max_sum}")
    print(f"Diff: {diff}")
    print("Groups:")
    
    for i, group in enumerate(groups):
        group_sum = group_sums[i]
        lessons_str = ', '.join(map(str, group))
        print(f"  Group {i + 1}: [{lessons_str}] → sum = {group_sum}")

if __name__ == "__main__":
    print("*** CLASS SCHEDULE ***")
    user_input = input('Lesson times / periods: ').strip().split(' / ')
    lessons_str = user_input[0].strip()
    k = int(user_input[1].strip())
    lessons = [int(i) for i in lessons_str.split(' ') if i.strip()]
    solve_and_display(lessons, k)
