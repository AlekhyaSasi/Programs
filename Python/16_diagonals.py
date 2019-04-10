#IN 5*5 Grid, draw 16 diagonals that do not touch each other
#fill in the grid gradually (say from bottom to top, from left to right)
#for each cell consider three possibilities
#bottom - B, top - T, right - R, Left - L
#1. diagonal from BL corner to TR corner
#2. diagonal from BR corner to TL corner
#3. No diagonal
# each time when a new diagonal is placed, checke whether it conflicts with other diagonals. If it does, backtrack
#https://gist.github.com/msarvar/b1ada757e2ef2c69fae98d5325db38ff
