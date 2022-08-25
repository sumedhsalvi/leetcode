class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            middle = (left + right) // 2
            hours_spent = 0
            
            for pile in piles:
                hours_spent += math.ceil(pile / middle)
                
            if hours_spent <= h:
                res = min(res, middle)
                right = middle - 1
            else:
                left = middle + 1
        return res