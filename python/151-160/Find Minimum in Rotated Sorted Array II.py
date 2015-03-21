    def findMin(self, num):
        size=len(num)
        if size==0:
            return 0
        Min=num[0]
        low,high=0,size-1
        while low<=high:
            mid = (low+high)//2
            if num[mid]<Min:
                Min=num[mid]
                if num[mid-1]<=num[mid]:
                    high=mid-1
                else:
                    break
            elif num[mid]>Min: 
                low=mid+1
            else:
                if num[mid]<num[size-1]:
                    high=mid-1
                elif num[mid]>num[size-1]:
                    low=mid+1
                else:
                    if mid==size-1 or mid==0:
                        break
                    Min=min(self.findMin(num[:mid]),self.findMin(num[mid+1:]))
                    break
        return Min
