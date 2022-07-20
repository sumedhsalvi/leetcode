class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = []
        
        empty = 0
        fresh = 1
        rotten = 2
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        minutes_ctr = 0
        fresh_oranges = 0
        
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == rotten:
                    queue.append((r, c))
                elif grid[r][c] == fresh:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        while queue:
            size = len(queue)
            minutes_ctr += 1
            for i in range(size):     
                row, col = queue.pop(0)
                for x, y in directions:
                    new_row = row + x
                    new_col = col + y

                    if new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == fresh:
                        grid[new_row][new_col] = rotten
                        queue.append((new_row, new_col))
                        fresh_oranges -= 1
                    
        return minutes_ctr - 1 if fresh_oranges == 0 else -1
                
                    
                    
                