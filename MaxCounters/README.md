
# MaxCounters

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

You are given N counters, initially set to 0, and you have two possible operations on them:
<ul style="margin: 10px;padding: 0px;"><li><i>increase(X)</i> − counter X is increased by 1,</li>
<li><i>max counter</i> − all counters are set to the maximum value of any counter.</li>
</ul>

A non-empty array A of M integers is given. This array represents consecutive operations:
<ul style="margin: 10px;padding: 0px;"><li>if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),</li>
<li>if A[K] = N + 1 then operation K is max counter.</li>
</ul>

For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.
Write a function:
<p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(N, A)</tt></p>
that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.
Result array should be returned as an array of integers.
For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.
Write an <b><b>efficient</b></b> algorithm for the following assumptions:
<ul style="margin: 10px;padding: 0px;"><li>N and M are integers within the range [<span class="number">1</span>..<span class="number">100,000</span>];</li>
<li>each element of array A is an integer within the range [<span class="number">1</span>..<span class="number"><tt style="white-space:pre-wrap">N + 1</tt></span>].</li>
</ul>


