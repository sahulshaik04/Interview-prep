class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(words)!=len(pattern):
            return False
        for i in range(len(pattern)):
            pi=pattern.index(pattern[i])
            wi=words.index(words[i])
            if wi!=pi:
                return False
        return True            
        