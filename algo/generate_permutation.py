from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    ans = []
    subset = []
    size = len(nums)

    def backtrack(k: int):
        if size == k:
            ans.append(subset.copy())
        else:
            backtrack(k + 1)
            subset.append(nums[k])
            backtrack(k + 1)
            subset.pop()

    backtrack(0)
    return ans


def permutation(n):
    chosen: List[bool] = [False] * n
    perm = []
    ans = []

    def search():
        if len(perm) == n:
            ans.append(perm.copy())
        else:
            for i in range(n):
                if chosen[i]:
                    continue
                chosen[i] = True
                perm.append(i)
                search()
                chosen[i] = False
                perm.pop()

    search()
    return ans

if __name__ == '__main__':
    print(permutation(3))
    print(subsets([1,2,3]))

