Problem statement
You are given an array of ‘N’ integers where each integer value is between ‘1’ and ‘N’.



Each integer appears exactly once except for ‘P’, which appears exactly twice, and ‘Q’, which is missing.



Your task is to find ‘P’ and ‘Q’ and return them respectively.



Example:
Input: ‘N’ = 4
‘A’ = [1, 2, 3, 2]

Output: {2, 4}

Explanation: The integer appearing twice is ‘2’, and the integer missing is ‘4’.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
4
1 2 3 2
Sample Output 1:
2 4
Explanation Of Sample Input 1:
Input: ‘N’ = 5
‘A’ = [1, 2, 3, 2]

Output: {2, 4}

Explanation: The integer appearing twice is ‘2’, and the integer missing is ‘4’.
Sample Input 2:
3
1 2 1
Sample Output 2:
1 3
Constraints:
2 <= N <= 10^5
1 <= A[i] <= N

Time Limit: 1-sec
--------------------------------------
from typing import List

def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n = len(a) # size of the array
    hash = [0] * (n + 1) # hash array

    #update the hash array:
    for i in range(n):
        hash[a[i]] += 1

    #Find the repeating and missing number:
    repeating, missing = -1, -1
    for i in range(1, n + 1):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

if __name__ == '__main__':
    a = [3, 1, 2, 5, 4, 6, 7, 5]
    ans = findMissingRepeatingNumbers(a)
    print("The repeating and missing numbers are: {", ans[0], ", ", ans[1], "}\n")
