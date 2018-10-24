# Coding practice
Simple practice problems: data structures and algorithms. This is a compilation of problems that I have found on line or collected from my experience.

### Parenthesis checker

Use a stack.

### Reverse LinkedList

Store values and recreate linked list after transversal or create list online.

### Get middle element of LinkedList

Traverse linked list to get length (if not implemented). Store values or traverse again to get middle.

### Print Left View of Binary Tree

I use my implementation of BinaryTree.

### Search array
Given a (m x n) 2D-array of integers with ordered lines and columns (e.g. [[1,2,3], [2,3,4]]), find a given element a.

Ideas:
- Use the ordered structure to implement a recursive algorithm.
- First notice: the bottom right element is the maximal element of the array.
- If this element is smaller than a, a is not in the array.
- If this element is equal to a, we are done and we can return True.
- If this element is greater than a, we can check the next element on the diagonal, i.e. the element at indices [m-1, n-1] and notice that: 1) if it is equal to a, we can terminate. 2) if it is smaller than a, we know that a is not in the last line or the last column and we can keep checking the elements diagonal.
- If no elements checked on the diagonal (completed by the end of the first line if n > m and the end of the first column if m > n) are smaller than a, then all the elements in the array are greater than a, and we return False.
- If at some indices (b, r) we stopped, because we found an element smaller than a, then we only have to check if a is in the top right and bottom left corners defined by those indices (all the elements in the top left corner are too small, all the elements in the bottom right are too large).

This can be implemented easily. The tricky part is mainly to get the indices right and not to forget to check a last line / column when the diagonal has been fully checked (the matrix is not necessarily squared!).

Complexity analysis:
- Assume for simplicity m=n and m=2^r
- Checking the elements on the diagonal of an array of size m takes O(m) operations.
- The worst case scenario is if we cut the array in half at every recursion. Every recursion that does not terminate calls 2 new recursions. We have to check one array of size 2^r, then 2 arrays of size 2^{r-1}, 4 arrays of size 2^{r-2}, etc.
- This takes O(2^r + 2 x 2^{r-1} + 4 x 2^{r-1} + ... + 2^{r} x 1) operations, i.e. O(r 2^r) = 0(m log m).
