class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        if str == '':
            return 0
        #deal flag
        flag = 1
        if str[0]=='-':
            flag = -1
            str = str[1:]
        elif str[0] =='+':
            flag = 1
            str = str[1:]
        #get num
        for i in range(len(str)):
            if str[i] <='9' and str[i] >='0':
                continue
            else:
                if i==0:
                    return 0
                str = str[:i]
                break
        #deal overflow
        result = long(str)
        if flag==1 and result >2147483647:
            return 2147483647
        if flag ==-1 and result >2147483648:
            return -2147483648
        return int(result*flag)
