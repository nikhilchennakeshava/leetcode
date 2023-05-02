class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            min_height = min(height[l], height[r])
            area = max(area, (r - l) * min_height)
            if height[l] < height[r]:
                l+=1
                while height[l]<min_height:
                    l+=1
            else:
                r-=1
                while height[r]<min_height:
                    r-=1			
        return area
        
        # m = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = (j-i) * min(height[i], height[j])
        #         m = max(area, m)
        # return m 
