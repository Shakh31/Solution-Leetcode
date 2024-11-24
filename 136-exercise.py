def singleNumber(nums) -> int:
    for i in nums:
        if nums.count(i) == 1:
            return i

n = list(map(int, input('n = ').split()))
print(singleNumber(n))