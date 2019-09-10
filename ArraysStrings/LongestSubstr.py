"""Given a string, find the length of the longest substring without repeating characters.
Example 1: Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2: Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3: Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring."""


def longestsubstr(s): # Longest substring without repetitions.
    if len(s) < 1:
        return s
    currlen = 1
    maxlen = 1
    start = 0
    visited = [-1]*256
    visited[ord(s[0])] = 0  # set the 0th index from string in visited array

    for i in range(1, len(s)):
        prev_index = visited[ord(s[i])]

        # If the current character is not present in the already processed substring or it is not part
        # of the current NRCS, then do cur_len++
        if prev_index == -1 or (prev_index < i-currlen):
            currlen += 1
        else:
            # Also, when we are changing the NRCS, we should also check whether length of the previous
            # NRCS was greater than max_len or not.
            maxlen = max(maxlen, currlen)
            currlen = i - prev_index

        visited[ord(s[i])] = i
    print(maxlen)
    return max(currlen,maxlen)


s = "adobecodebanc"
longestsubstr(s)
s = "aaaaaaaa"
longestsubstr(s)
