def sort_with_priority(values,group):
    def helper(item):
        if item in group:
            return (0,item)
        return (1,item)
    values.sort(key=helper)
    return values

if __name__ == '__main__':
    nums = [3, 2, 4, 7, 5, 9, 8, 1]
    group = {9,8,7}

    nums2 = sort_with_priority(nums,group)
    print(nums2)

