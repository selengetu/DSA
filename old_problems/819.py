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


    class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone_map[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        backtrack("", digits)
        return output