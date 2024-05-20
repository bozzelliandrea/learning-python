# CTCI 1.1
from typing import List
from common.assertion import assertEquals

def is_unique(string: str) -> bool:
    """
    Implement an algorithm to determine if a string has all unique characters.
    :param string: input string
    :return: true if it doesn't contain duplicate chars
    """
    # clarify if we use ASCII char code, if yes we're using only 128 chars, otherwise we can use a hashmap like Counter
    # clarify if we consider the space as char
    dict: List[bool] = [False] * 128

    for c in string:
        if dict[ord(c)]:
            return False
        dict[ord(c)] = True

    return True



def is_unique_without_memory(string: str) -> bool:
    """
    What if you cannot use additional data structures?
    :param string: input string
    :return: true if it doesn't contain duplicate chars
    """
    copy_tmp = sorted(string)

    for i in range(1, len(copy_tmp)):
        if copy_tmp[i - 1] == copy_tmp[i]:
            return False

    return True


if __name__ == '__main__':
    assertEquals(True, is_unique("aksjdu23"))
    assertEquals(False, is_unique("aks2du23"))
    assertEquals(False, is_unique("aks+du++"))
    assertEquals(False, is_unique("aks+du  "))
    assertEquals(True, is_unique("aks+du\ "))

    assertEquals(True, is_unique_without_memory("aksjdu23"))
    assertEquals(False, is_unique_without_memory("aks2du23"))
    assertEquals(False, is_unique_without_memory("aks+du++"))
    assertEquals(False, is_unique_without_memory("aks+du  "))
    assertEquals(True, is_unique_without_memory("aks+du\ "))
