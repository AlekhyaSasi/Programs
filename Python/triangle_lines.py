#several straight lines (at least 3) cut a plane into pieces. Each line intersects with every other line, & all the intersection pts r different
#prove that there is at least 1 triangular piece
#each line intersects with every other line. so they are not parallel
#all intersection pts r different so no 3 intersect at 1 pt
#there will be 1 triangular piece
#when we add more lines
# either the same triangle remains or it forms new triangle
#if a line intersects triangle it intersects it in 2 pts n it intersects 2 of the sides

#THEROEM: For any n >/3 and any n straight lines on a plane, if every 2 lines intersect, n all the intersection poiints r different, there is a triangular piece among the pieces into which these lines cut the plane
#PROOF -
#induction base n = 3, three lines form a triangle
#induction step from n to n+1 - add one more line in general case


#THEOREM - The no.of odd points is aleays even, regardless of how many points and segments are there and which pairs of points are connected by segments.
#PROOF
#When there are no segments, there are no odd points, so the number of odd points is indeed even.
#when we add segments one by one, the number of odd points either doesnt change, increase by 2 or decreases by 2. thus the number of odd points stay even.

#EASY CASE : No segments
#when there are no segments, each pt has 0 neighbors, so there are no odd points. the number of of odd points is zero which is even

#adding a SEGMENT:
#segment AB adds 2 odd points A and B
#segment HI adds 2 odd points H and I
# so for 0 segements the no.of odd points is even
# for 1 swgment the no.of odd points is even
# so for k odd points is even, k+1 is also even
# 
