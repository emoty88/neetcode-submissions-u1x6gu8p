class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            letter_count=len(s)
            encoded += f'{letter_count}#{s}'
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        letter_count = 0
        strs = []
        i=0
        while i < len(s):
            if s[i] == '#':
                strs.append(s[i+1:i+letter_count+1])
                i = i+letter_count+1
                letter_count = 0
                continue
            else:
                letter_count = letter_count*10+int(s[i])
                i+=1
        return strs


