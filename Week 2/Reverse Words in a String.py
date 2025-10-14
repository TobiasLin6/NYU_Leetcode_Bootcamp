class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_str = ""

        for word in words[::-1]:
            reversed_str += word + " "

        return reversed_str[:-1]

        