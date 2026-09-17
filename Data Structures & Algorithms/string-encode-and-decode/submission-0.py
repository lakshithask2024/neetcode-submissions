class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            out.append(str(len(s)) + "#" + s) 
        return "".join(out)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 1) Read the length (could be multiple digits)
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])  # digits between i and j form the length

            # 2) Read exactly 'length' chars after '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # 3) Move i to the start of the next encoded chunk
            i = end
        return res
                





