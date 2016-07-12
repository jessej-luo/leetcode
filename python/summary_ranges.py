class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        final_lst = []
        
        if len(nums) == 1:
            final_lst.append(str(nums[0]))
            return final_lst
            
        first = nums[0]
        last = nums[0]
        
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == last + 1:
                last = nums[i]
            else:
                interval = str(first)
                if first != last:
                    interval += "->" + str(last)
                final_lst.append(interval)
                if i < len(nums):
                    first = nums[i]
                    last = nums[i]
                
        # interval = str(first)
        # if first != last:
        #     interval += "->" + str(last)
        # final_lst.append(interval)
        
        return final_lst
                
                
                
            
        