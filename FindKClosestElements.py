# https://leetcode.com/problems/find-k-closest-elements/

def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr) - 1
        while(r - l >= k):
            if(abs(x - arr[l] <= abs(x - arr[r]))):
                r -= 1 # element at r is higher compare to element at l. Exclude r
            else:
                l += 1 # element at l is higher compare to element at r. Exclude l
        
        result = []
        for i in range(l, r + 1):
            result.append(arr[l])
            l += 1
        return result