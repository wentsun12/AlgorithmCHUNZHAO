#33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0: return -1
        low = 0 
        high = len(nums) -1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: 
                return mid
            # 前一部分为升序
            if nums[low] <= nums[mid]: 
                if nums[mid] >= target and target >= nums[low]:
                    high = mid -1
                else:
                    low = mid +1
            # 前一部分为旋转
            else:
                if nums[mid]<=target and target <= nums[high]:
                    low = mid +1
                else:
                    high = mid - 1 
        return -1

# 74 搜索矩阵
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

# 153
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1          
        while left < right:                    
            mid = (left + right) //2          
            if nums[mid] > nums[right]:         
                left = mid + 1                  
            elif nums[mid] < nums[right]:       
                right = mid                    
        return nums[left]  
