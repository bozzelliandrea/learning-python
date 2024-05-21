from common.assertion import assertEquals


def urlify(string: str, wanted_size: int) -> str:
    chars = list(string)
    space_uri_char = "%20"
    for i in range(len(chars)):
        if i >= wanted_size:
            break

        if chars[i] == " ":
            chars[i] = space_uri_char

    return "".join(chars)


if __name__ == "__main__":
    print(urlify("Mr John Smith", 13))
    print(urlify("Mr John Smith            ", 13))
    assertEquals("Mr%20John%20Smith", urlify("Mr John Smith", 13))