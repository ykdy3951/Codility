
# Triangle

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-green)

An array A consisting of N integers is given. A triplet (P, Q, R) is <i>triangular</i> if 0 ≤ P &lt; Q &lt; R &lt; N and:
<ul style="margin: 10px;padding: 0px;"><li>A[P] + A[Q] &gt; A[R],</li>
<li>A[Q] + A[R] &gt; A[P],</li>
<li>A[R] + A[P] &gt; A[Q].</li>
</ul>

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.
Write a function:
<p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(A)</tt></p>
that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.
For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.
Write an <b><b>efficient</b></b> algorithm for the following assumptions:
<ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">0</span>..<span class="number">100,000</span>];</li>
<li>each element of array A is an integer within the range [<span class="number">−2,147,483,648</span>..<span class="number">2,147,483,647</span>].</li>
</ul>


