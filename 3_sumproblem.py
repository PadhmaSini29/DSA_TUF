Problem statement
You are given an array ‘ARR’ containing ‘N’ integers.
Return all the unique triplets [ARR[i], ARR[j], ARR[k]] such that i != j, j != k and k != i and their sum is equal to zero.

Example:
Input: ‘N’ = 5 
'ARR' =  [-1, -1, 2, 0, 1] 

Output: 
-1 -1 2
-1 0 1

Explanation:
(-1 -1 +2) = (-1 +0 +1) = 0.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
5 
-1 -1 2 0 1
Sample Output 1 :
-1 -1 2
-1 0 1
Explanation Of Sample Input 1:
(-1 -1 +2) = (-1 +0 +1) = 0.
Sample Input 2:
4 
0 0 0 0
Sample Output 2 :
0 0 0
Constraints:
1  <= N <= 1000
1 <= ARR[i] <= 1000
Time Limit: 1 sec
--------------------------
def triplet(n, arr):
    st = set()

    # check all possible triplets:
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    st.add(tuple(temp))

    # store the set elements in the answer:
    ans = [list(item) for item in st]
    return ans


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    ans = triplet(n, arr)
    for it in ans:
        print("[", end="")
        for i in it:
            print(i, end=" ")
        print("]", end=" ")
    print("\n")

Certainly! Let's break down the explanation in simpler terms:

1. **First Loop (`i` loop):**
   - Imagine we have a list of numbers, and we want to check every possible combination of three numbers from this list.
   - The first loop, let's call it the `i` loop, goes through each number in the list, one by one, starting from the first (index 0) and going up to the second-to-last number (index n-1).

2. **Second Loop (`j` loop):**
   - Inside this `i` loop, there's another loop, let's call it the `j` loop. This loop starts from the next number after the current `i` (index i+1) and goes up to the last number in the list (index n-1).
   - This `j` loop helps us consider all pairs of numbers where the first number comes from the `i` loop, and the second number comes from the `j` loop.

3. **Third Loop (`k` loop):**
   - Inside the `j` loop, there's yet another loop, let's call it the `k` loop. This loop starts from the next number after the current `j` (index j+1) and goes up to the last number in the list (index n-1).
   - This `k` loop helps us consider all triplets of numbers where the first number comes from the `i` loop, the second number comes from the `j` loop, and the third number comes from the `k` loop.

4. **Checking the Sum:**
   - Now, inside these three nested loops, for each combination of `i`, `j`, and `k`, we calculate the sum of the corresponding numbers in the list: `arr[i] + arr[j] + arr[k]`.
   - We check if this sum is equal to a specific target, in this case, 0.

5. **Sorting and Inserting into a Set:**
   - If the sum is indeed 0, we have found a triplet that adds up to 0.
   - We take these three numbers, sort them in ascending order, and then insert them into a set.
   - Sorting is done to ensure that we store unique triplets in the set, as the order of numbers in a triplet doesn't matter.
   - Using a set ensures that we only store unique triplets, avoiding duplicates.

In summary, these nested loops help us explore all possible combinations of three numbers from the given list, and we store unique triplets whose sum is 0 in a set
