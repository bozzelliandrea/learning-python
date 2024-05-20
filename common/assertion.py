from typing import Any

from common.colors import Colors


def assertEquals(expected: Any, wanted: Any) -> None:
    if expected != wanted:
        raise Exception("Assertion failed!")

    print(Colors.SUCCESS + f"Assertion Success. Result is {wanted}" + Colors.ENDC)
