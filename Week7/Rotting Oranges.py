class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue and fresh_count > 0:
            minutes += 1
            
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for dir_row, dir_col in directions:
                    row, col = row + dir_row, col + dir_col
                    
                    if (0 <= row < rows and 0 <= col < cols and
                        grid[row][col] == 1):
                        
                        grid[row][col] = 2
                        fresh_count -= 1
                        queue.append((row, col))
        
        return minutes if fresh_count == 0 else -1