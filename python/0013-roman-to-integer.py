#!/usr/bin/env python3
import pytest
import sys


class Solution1:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        s = s[::-1]
        char = s[0]
        output = symbols[char]
        for i in range(1, len(s)):
            # ("MMMCMXCIX", 3999),
            factor = -1 if symbols[s[i]] < symbols[char] else 1
            output += symbols[s[i]] * factor
            char = s[i]
        return output


class Solution2:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        output = 0
        for i in range(1, len(s)):
            factor = 1
            conditions = [
                (s[i - 1] == "I" and s[i] == 'V'),
                (s[i - 1] == "I" and s[i] == 'X'),
                (s[i - 1] == "X" and s[i] == 'L'),
                (s[i - 1] == "X" and s[i] == 'C'),
                (s[i - 1] == "C" and s[i] == 'D'),
                (s[i - 1] == "C" and s[i] == 'M'),
            ]
            if any(conditions):
                factor = - 1
            output += symbols[s[i - 1]] * factor
        output += symbols[s[-1]]
        return output


class Solution(Solution1):
    pass


tests = [
    ("I", 1),
    ("II", 2),
    ("III", 3),
    ("IV", 4),
    ("IX", 9),
    ("X", 10),
    ("XI", 11),
    ("XV", 15),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("MMMCMXCIX", 3999),
]


@pytest.mark.parametrize("value", tests)
def test_values(value):
    obj = Solution()
    output = obj.romanToInt(value[0])
    msg = f"f('{value[0]}') = {output} -> Expected {value[1]}"
    assert output == value[1], msg


if __name__ == "__main__":
    obj = Solution()
    output = obj.romanToInt(sys.argv[1])
    print(output)
