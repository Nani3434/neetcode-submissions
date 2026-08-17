class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        # Step 2 - loop through each word
        for word in strs:
            # Step 3 - sort the word to get the key
            key = tuple(sorted(word))
            
            # Step 4 - if key not in hashmap create empty list
            if key not in groups:
                groups[key] = []
            
            # Step 5 - add word to its group
            groups[key].append(word)
        
        # Step 6 - return all groups as a list
        return list(groups.values())