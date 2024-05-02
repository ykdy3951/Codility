
# TapeEquilibrium

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-green)

A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 &lt; P &lt; N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The <i>difference</i> between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:
<ul style="margin: 10px;padding: 0px;"><li>P = 1, difference = |3 − 10| = 7 <br>
</li>
<li>P = 2, difference = |4 − 9| = 5  <br>
</li>
<li>P = 3, difference = |6 − 7| = 1  <br>
</li>
<li>P = 4, difference = |10 − 3| = 7  <br>
</li>
</ul>

Write a function:
<p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(A)</tt></p>
that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.
Write an <b><b>efficient</b></b> algorithm for the following assumptions:
<ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">2</span>..<span class="number">100,000</span>];</li>
<li>each element of array A is an integer within the range [<span class="number">−1,000</span>..<span class="number">1,000</span>].</li>
</ul>


