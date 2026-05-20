class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_dict = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            if n in bucket_dict:
                bucket_dict[n] += 1
            else:
                bucket_dict[n] = 1
        for n, c in bucket_dict.items():
            freq[c].append(n)
            
        result = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if(len(result) == k):
                    return result

        