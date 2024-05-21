from collections import Counter

from common.assertion import assertEquals


def permutation(s1: str, s2: str) -> bool:
    if (not s1 and s2) or (s1 and not s2) or len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)

def permutation_with_array(s1: str, s2: str) -> bool:
    if (not s1 and s2) or (s1 and not s2) or len(s1) != len(s2):
        return False

    charset = [0] * 128

    for c in s1:
        charset[ord(c)]+=1

    for c in s2:
        if charset[ord(c)] == 0:
            return False
        charset[ord(c)]-=1

    return True

if __name__ == '__main__':
    assertEquals(True, permutation("aksjdu23", "aksjdu23"))
    assertEquals(False, permutation(None, "aksjdu23"))
    assertEquals(False, permutation("aksjdu23", None))
    assertEquals(False, permutation("aksjdu23", ""))
    assertEquals(False, permutation("aksjdu23", "aksjdu24"))

    assertEquals(True, permutation_with_array("aksjdu23", "aksjdu23"))
    assertEquals(False, permutation_with_array(None, "aksjdu23"))
    assertEquals(False, permutation_with_array("aksjdu23", None))
    assertEquals(False, permutation_with_array("aksjdu23", ""))
    assertEquals(False, permutation_with_array("aksjdu23", "aksjdu24"))