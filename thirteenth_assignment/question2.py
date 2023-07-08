def remove_duplicates(sorted_list):
    if not sorted_list:
        return sorted_list
    
    current = sorted_list[0]
    unique_list = [current]

    for i in range(1, len(sorted_list)):
        if sorted_list[i] != current:
            current = sorted_list[i]
            unique_list.append(current)
    
    return unique_list
