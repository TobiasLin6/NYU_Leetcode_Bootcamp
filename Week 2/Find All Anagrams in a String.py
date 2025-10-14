from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        result = []

        p_count = Counter(p)
        s_count = Counter()

        for i in range(len(s)):
            s_count[s[i]] += 1

            if i >= len(p):
                s_count[s[i - len(p)]] -= 1
                if s_count[s[i - len(p)]] == 0:
                    s_count.pop(s[i - len(p)])
            
            if s_count == p_count:
                result.append(i - (len(p) - 1))

        return result