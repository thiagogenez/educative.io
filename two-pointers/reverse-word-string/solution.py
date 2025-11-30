def reverse(word: list[str], left: int, right: int):
    """Reverse the portion of the list word from left to right (inclusive).
    Args:
        word: List of characters (list of str)
        left: Left index (int)
        right: Right index (int)
    """
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1


def reverse_each_word(word: list[str]):
    """Reverse each word in the list of characters `word`.
    Args:
        word: List of characters (list of str)
    """
    n = len(word)
    i = 0

    while i < n:
        if word[i] == " ":
            i += 1
            continue

        start = i
        while i < n and word[i] != " ":
            i += 1

        reverse(word, start, i - 1)


def remove_extra_spaces(word: list[str]) -> str:
    """Remove extra spaces from the list of characters `word`.
    Args:
        word: List of characters (list of str)
    Returns:
        str: The cleaned-up string.
    """
    n = len(word)
    result = []
    i, j = 0, n - 1

    while i <= j:
        # copy non-space characters
        if word[i] != " ":
            result.append(word[i])
            i += 1

        # skip space run
        while i <= j and word[i] == " ":
            i += 1

        # add a single space if more words remain
        if i <= j and word[i - 1] == " ":
            result.append(" ")

    return "".join(result)


def reverse_words(sentence: str) -> str:
    """Reverse the words in the input sentence.
    Args:
        sentence: Input sentence (str)
    Returns:
        str: Sentence with words reversed.
    """
    s = list(sentence.strip())
    n = len(s)

    # 1) Reverse full string
    reverse(s, 0, n - 1)

    # 2) Reverse each word individually
    reverse_each_word(s)

    # 3) Clean spaces
    return remove_extra_spaces(s)


def main():
    tests = [
        ("hello world", "world hello"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("the sky   is blue", "blue is sky the"),
        ("    one", "one"),
        ("one    ", "one"),
        ("   hello    world    test   ", "test world hello"),
        ("single", "single"),
        ("", ""),
        ("      ", ""),
        ("a    b    c", "c b a"),
        ("ab", "ab"),
        ("ab   cd", "cd ab"),
    ]

    all_passed = True

    for inp, expected in tests:
        out = reverse_words(inp)
        status = "OK" if out == expected else "FAIL"
        print(f"Input: {inp!r}")
        print(f"Output:   {out!r}")
        print(f"Expected: {expected!r}")
        print(f"Status: {status}")
        print("-" * 40)

        if out != expected:
            all_passed = False

    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("Some tests FAILED.")


if __name__ == "__main__":
    main()
