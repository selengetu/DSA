class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
            # Normalize the paragraph by converting to lowercase and removing punctuation
            words = re.findall(r'\w+', paragraph.lower())
            
            # Create a set of banned words for quick lookup
            banned_set = set(banned)
            
            # Count the occurrences of each word, excluding banned words
            word_count = Counter(word for word in words if word not in banned_set)
            
            # Find the most common non-banned word
            most_common_word, _ = word_count.most_common(1)[0]
            
            return most_common_word


    