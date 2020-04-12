def searchInsert(self, nums: List[int], target: int) -> int:
        last = len (nums) - 1
        if (target < nums[0]):
            return 0
        if (target > nums[last]):
            return last + 1

        first = 0
        while first < last :
            mid = (first + last) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                    last = mid
            else:
                    first = mid+1
        return first
