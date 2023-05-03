# Design an algorithm to encode a list of strings to a string. The encoded
# string is then sent over the network and is decoded back to the original list
# of strings.

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s)) + '#' + s for s in strs])
        

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i] 
                i += 1
            i += 1
            decoded = ''
            while len(decoded) < int(length):
                decoded += s[i]
                i += 1
            result.append(decoded)

        return result

codec = Codec()
strs = ['bog', 'dog', 'testing', '##', '#2ab']
assert codec.decode(codec.encode(strs)) == strs

print('ALL TESTS PASS')
