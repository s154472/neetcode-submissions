class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqDict = {} # "number" : "frequency"
        freqArray = [[] for i in range(len(nums)+1)] #index = # of occurences, value = list of nums w/ that occurence

        #step 1: build our freqDict
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        
        #step 2: build out freqArray
        for num, freq in freqDict.items():
            freqArray[freq].append(num)
        
        #step 3: traverse freqArray right to left for k answers:
        res = []
        
        for i in range(len(freqArray)-1,-1,-1):
            for num in freqArray[i]:
                res.append(num)
                if k == len(res):
                    return res