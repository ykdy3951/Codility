
# NumberOfDiscIntersections

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].
We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).
The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0
<img class="inline-description-image" src="https://codility-frontend-prod.s3.amazonaws.com/media/task_static/number_of_disc_intersections/static/images/auto/0eed8918b13a735f4e396c9a87182a38.png" alt="">
There are eleven (unordered) pairs of discs that intersect, namely:
<ul style="margin: 10px;padding: 0px;"><li>discs 1 and 4 intersect, and both intersect with all the other discs;</li>
<li>disc 2 also intersects with discs 0 and 3.</li>
</ul>

Write a function:
<p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(A)</tt></p>
that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
Given array A shown above, the function should return 11, as explained above.
Write an <b><b>efficient</b></b> algorithm for the following assumptions:
<ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">0</span>..<span class="number">100,000</span>];</li>
<li>each element of array A is an integer within the range [<span class="number">0</span>..<span class="number">2,147,483,647</span>].</li>
</ul>


