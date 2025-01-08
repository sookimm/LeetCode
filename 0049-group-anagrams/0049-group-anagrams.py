class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            sorted_word = "".join(sorted(i))

            if sorted_word not in dic:
                dic[sorted_word] = []

            dic[sorted_word].append(i)
        
        return list(dic.values())
        
        