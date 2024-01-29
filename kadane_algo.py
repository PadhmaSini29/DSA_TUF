Problem statement
You are given an array 'arr' of length 'n', consisting of integers.
A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.
Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.
The sum of an empty subarray is 0.

Example :
Input: 'arr' = [1, 2, 7, -4, 3, 2, -10, 9, 1]
Output: 11

Explanation: The subarray yielding the maximum sum is [1, 2, 7, -4, 3, 2].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
9
1 2 7 -4 3 2 -10 9 1

Sample Output 1 :
11


Explanation for Sample 1 :
The subarray yielding the maximum sum is [1, 2, 7, -4, 3, 2].

Sample Input 2 :
6
10 20 -30 40 -50 60


Sample Output 2 :
60


Sample Input 3 :
3
-3 -5 -6


Sample Output 3 :
0


Expected time complexity :
The expected time complexity is O(n).


Constraints :
1 <= 'n' <= 10 ^ 6
-10 ^ 6 <= 'arr[i]' <= 10 ^ 6

Time limit: 1sec
------------------------------------------------------------
def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum

    for i in range(n):
        for j in range(i, n):
            # subarray = arr[i.....j]
            summ = 0

            # add all the elements of subarray:
            for k in range(i, j+1):
                summ += arr[k]

            maxi = max(maxi, summ)

    return maxi

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(arr)
    maxSum = maxSubarraySum(arr, n)
    print("The maximum subarray sum is:", maxSum)

Absolutely, let's break it down in simpler terms:

1. **Selecting Starting Index (Outer Loop):**
   - We start by choosing a starting point for our subarray. We'll call this point "i."
   - We use a loop (let's call it the outer loop) that goes through all possible starting indices of the subarray.
   - The starting indices can be any position from the beginning (index 0) to the end (index n-1, where n is the size of the array).

2. **Selecting Ending Index (Inner Loop):**
   - For each chosen starting index (i), we run another loop (let's call it the inner loop).
   - This inner loop helps us explore all possible ending indices for the subarray that starts at index i.
   - The ending indices can be any position from i to the end of the array (index n-1).

3. **Calculating Sum for Each Subarray:**
   - Once we've selected a starting index (i) and an ending index (j), we have a subarray (arr[i...j]).
   - Now, we run yet another loop inside (let's call it the sum loop) to calculate the sum of all elements in this particular subarray.
   - This involves adding up all the numbers from the starting index i to the ending index j.

In summary, these nested loops help us explore all possible subarrays by iterating through all starting indices, all ending indices for each starting index, and calculating the sum of each subarray. This process is a part of a common approach to solve problems related to subarrays and subsequences
