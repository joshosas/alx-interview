#!/usr/bin/python3
"""
A file containing pascal_triangle function
"""
    
    
    def pascal_triangle(n):
        """
        Implements the Pascal Triangle Logic
        given an integer
        """
        if n <= 0:
            return []
        
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
