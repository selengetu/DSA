class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # Handle edge case where input is empty
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare prefix with every other string
        for s in strs[1:]:
            # Narrow down the prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from prefix
                if not prefix:  # If prefix becomes empty, return ""
                    return ""
        
        return prefix
