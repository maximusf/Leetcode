class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict where 
        # keys are tuples representing counts of characters in anagrams and 
        # values are list of anagrams with the same character counts
        ans = collections.defaultdict(list)

        for s in strs: # iterates through each string in the list
            # initialize a list of 26 zeros 
            # representing count of each char in s (26 letters in alphabet)
            count = [0] * 26
            # iterate through each character in the current string
            for c in s:
                # increment the count of the current character by 1
                # use ASCII values of characters to determine the index in the 'count' list
                # subtract the value of 'a' to map each character to a zero-based index
                # (e.g., 'a' maps to 0, 'b' maps to 1, and so on)
                count[ord(c) - ord("a")] += 1
            # convert the 'count' list to a tuple and use it as a key in the 'ans' dictionary
            # append the current string 's' to the list associated with that key
            # this will group anagrams t ogether based on their character counts
            ans[tuple(count)].append(s)
        # return the values of the 'ans' dictionary, which are the lists of grouped anagrams
        return ans.values()
