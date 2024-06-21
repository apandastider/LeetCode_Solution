'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

'''


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        if len(citations) == 1 and citations[0] != 0:
            return 1
        if len(citations) == 1 and citations[0] == 0:
            return 0

        def paperswithHindex(h, citations):
            return sum(cite_count >= h for cite_count in citations) >= h

        low = 0
        high = len(citations) - 1

        while low <= high:
            mid = (low + high) // 2

            if paperswithHindex(mid, citations):
                low = mid + 1
            else:
                high = mid - 1

        return high
