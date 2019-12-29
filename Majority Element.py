def majorityElement(self, nums: List[int]) -> int:
    from collections import Counter
    stats = Counter(nums)
    value=max(stats, key=stats.get)
    return value
