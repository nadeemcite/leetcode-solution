class Solution:

    def encode(self, strs: list[str]) -> str:
        final_str = ""
        for sub_str in strs:
            final_str += str(chr(len(sub_str))) +sub_str
        return final_str

    def decode(self, s: str) -> list[str]:
        strs = []
        i = 0
        if len(s) <1:
            return []
        while True:
            next_length = ord(s[i])
            target_str = s[i+1: i+next_length+1]
            strs.append(target_str)
            i += next_length+1
            if i>=len(s):
                break
        return strs
    
encoded = Solution().encode([""])
print(encoded)
decoded = Solution().decode(encoded)

print(decoded)
