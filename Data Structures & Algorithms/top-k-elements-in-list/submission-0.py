class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1 - count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Step 2 - sort by frequency and return top k
        return sorted(count, key=lambda x: count[x], reverse=True)[:k]