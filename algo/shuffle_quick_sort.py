class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        def swap(f, s):
            tmp = nums[f]
            nums[f] = nums[s]
            nums[s] = tmp

        def shuffle():
            size = len(nums)
            for i in range(size):
                swap(i, random.randrange(size - 1))

        def partition(low: int, high: int) -> int:
            i = low + 1
            j = high

            while True:
                while nums[i] < nums[low]:
                    if i == high:
                        break
                    i+=1
                while nums[j] > nums[low]:
                    if j == low:
                        break
                    j-=1

                if i >= j: 
                    break
                swap(i, j)

            swap(low, j)
            return j

        
        def quickSort(low: int, high: int) -> None:
            if low >= high:
                return

            j = partition(low, high)
            quickSort(low, j - 1)
            quickSort(j + 1, high)

        shuffle()
        quickSort(0, len(nums) - 1)
        return nums

sol = Solution()
print(sol.sortArray([4,23,45,23,1,2,3,1,5]))
