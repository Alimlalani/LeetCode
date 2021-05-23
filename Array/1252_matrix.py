class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        
        cellValues = {}
        
        # Used to keep track of individual cells
        cellNum = 0
        
        # Visit each cell
        for i in range(m):
            for j in range(n):
                
                # Give cell default value
                cellValues[cellNum] = 0
                
                # Visit each index pair for increment
                for index in indices:
                    
                    # Update the dictionary of values if a cell is in the index row or col
                    if index[0] == i:
                        cellValues[cellNum] += 1
                    if index[1] == j:
                        cellValues[cellNum] += 1
                
                # Move to the next cell
                cellNum+=1

        # Count all odd cells using our map
        counter = 0
        for value in cellValues.values():
            if value % 2 == 1:
                counter+=1
        return counter


'''


'''