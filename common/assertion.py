from typing import Any

from common.colors import Colors


def assertEquals(expected: Any, given: Any) -> None:
    if expected != given:
        raise Exception(f"Assertion failed! expected {expected} but result is {given}")

    print(Colors.SUCCESS + f"Assertion Success. Result is {given}" + Colors.ENDC)
