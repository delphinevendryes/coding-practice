# coding-practice
Simple practice problems: data structures and algorithms

## Search array
Given a (m x n) 2D-array of integers with ordered lines and columns (e.g. [[1,2,3], [2,3,4]]), find a given element a.

Ideas:
- Use the ordered structure to implement a recursive algorithm.
- First notice: the bottom right element is the maximal element of the array.
- If this element is smaller than a, a is not in the array.
- If this element is equal to a, we are done and we can return True.
- If this element is greater than a, we can check the next element on the diagonal, i.e. the element at indices [m-1, n-1] and notice that:

This can be implemented easily. The tricky part is mainly to get the indices right and not to forget to check a last line / column when the diagonal has been fully checked (the matrix is not necessarily squared!).


Complexity analysis
