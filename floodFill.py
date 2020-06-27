class Solution:
    def floodFillUtility(self, screen, x, y, prev_color, new_color):
        if (x < 0 or y < 0 or
        x >= R or y >= C or
        screen[x][y] != prev_color or
        screen[x][y] == new_color):
            return False
        screen[x][y] = new_color
        self.floodFillUtility(screen, x+1, y, prev_color, new_color)
        self.floodFillUtility(screen, x-1, y, prev_color, new_color)
        self.floodFillUtility(screen, x, y+1, prev_color, new_color)
        self.floodFillUtility(screen, x, y-1, prev_color, new_color)
    
    def floodFill(self, screen, x, y, new_color):
        prev_color = screen[x][y]
        self.floodFillUtility(screen, x, y, prev_color, new_color)
    
# Main Program

screen = [
        [1,1,0],
        [1,1,1],
        [0,2,3],
        [3,1,0]
        ]

R = len(screen)
C = len(screen[0])
new_color = 2
x = 1
y = 1
s = Solution()
s.floodFill(screen, x, y, new_color)
for i in range(R):
    for j in range(C):
        print(screen[i][j], end = " ")
    print()


