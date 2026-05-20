class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_dict = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            bucket_dict[n] = 1 + bucket_dict.get(n,0) ##.get returns 1 if seen and 0 else
        for n,c in bucket_dict.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if(len(result) == k):
                    return result

        