def editDistance(str1, str2, m, n):
 
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    ans1 = editDistance(str1, str2, m, n-1) + 1# Insert
    ans2 = editDistance(str1, str2, m-1, n) + 1# Delete
    ans3 = editDistance(str1, str2, m-1, n-1) + 1# Substitute
    return min(ans1,ans2,ans3)


if __name__ == '__main__':
	str1 = "CCUAUGC"
	str2 = "CUAUGGC"
	print (editDistance(str1, str2, len(str1), len(str2)))