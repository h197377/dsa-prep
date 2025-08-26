def twoSum(nums, target) -> int[]:
    if len(nums) < 2:
        return []
    
    hm = {}
    for i, n in enumerate(nums):
        missing = target - n
        if missing in hm:
            return [hm[missing], i]
        hm[n] = i

    return []