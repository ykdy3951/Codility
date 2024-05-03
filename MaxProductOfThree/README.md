
# MaxProductOfThree

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-green)

A non-empty array A consisting of N integers is given. The <i>product</i> of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P &lt; Q &lt; R &lt; N).
For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:
<ul style="margin: 10px;padding: 0px;"><li>(0, 1, 2), product is −3 * 1 * 2 = −6</li>
<li>(1, 2, 4), product is  1 * 2 * 5 = 10</li>
<li>(2, 4, 5), product is  2 * 5 * 6 = 60</li>
</ul>

Your goal is to find the maximal product of any triplet.
Write a function:
<p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(A)</tt></p>
that, given a non-empty array A, returns the value of the maximal product of any triplet.
For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.
Write an <b><b>efficient</b></b> algorithm for the following assumptions:
<ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">3</span>..<span class="number">100,000</span>];</li>
<li>each element of array A is an integer within the range [<span class="number">−1,000</span>..<span class="number">1,000</span>].</li>
</ul>


