# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
def arrayStringsAreEqual(word1, word2):
		i = j = ii = jj = 0
		while i < len(word1) and j < len(word2):
			if word1[i][ii] != word2[j][jj]:
				return False
			ii += 1
			jj += 1
			if ii == len(word1[i]):
				i += 1
				ii = 0
			if jj == len(word2[j]):
				jj = 0
				j += 1
		return i == len(word1) and j == len(word2)



if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(arrayStringsAreEqual(word1, word2))
