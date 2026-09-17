class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            buckets[f].append(num)

        
        res = []
        for f in range(len(buckets) - 1, 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
        return res