"""
Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
"""

def wiggleMaxLength(L):
    if len(L)<2:
        return len(L)
    down , up = 1, 1
    for i in range(1, len(L)):
        if L[i] > L[i-1]:
            up = down + 1
        elif L[i] < L[i-1]:
            down = up + 1
    return max(down, up)
    
    
if __name__ == "__main__":
    L = [1,7,4,9,2,5]
    result = wiggleMaxLength(L)
    print(result)
