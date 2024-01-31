class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def count_map(target):
            char_dict = {}
            for char in target:
                char_dict[char] = char_dict.get(char, 0) + 1
            return char_dict

        ransom_map = count_map(ransomNote)
        magazine_map = count_map(magazine)

        result = all(key in magazine_map and magazine_map[key] >= val for key, val in ransom_map.items())
        return result
