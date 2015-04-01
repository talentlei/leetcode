    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        vstr1=version1.split('.')
        vstr2=version2.split('.')
        i=0
        while i<len(vstr1) and i<len(vstr2):
            if int(vstr1[i])>int(vstr2[i]):
                return 1
            elif int(vstr1[i])<int(vstr2[i]):
                return -1
            i+=1
        if i!=len(vstr1):
            if int(''.join(vstr1[i:]))>0:
                return 1
        if i!=len(vstr2):
            if int(''.join(vstr2[i:]))>0:
                return -1
        return 0
