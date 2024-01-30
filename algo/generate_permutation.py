from typing import List


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