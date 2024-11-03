def groupAnagrams(strs):
    strs_sorted = strs.copy()
    sorted_strs_list = []

    for i in range(len(strs_sorted)):
        str = strs_sorted[i]
        chars = []

        for char in str:
            chars.append(char)

        chars.sort()
        str = ''.join(chars)

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]

    groupAnagrams(strs)