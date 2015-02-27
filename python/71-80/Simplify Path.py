# @param path, a string
    # @return a string
    def simplifyPath(self, path):
        path = path.strip()
        dirs = path.split('/')
        pos=0
        while pos <len(dirs):
            if dirs[pos]=='' or dirs[pos]=='.':
                del dirs[pos]
            elif dirs[pos]=='..':
                del dirs[pos]
                if pos!=0:
                    del dirs[pos-1]
                    pos-=1
            else:
                pos+=1
        return '/'+'/'.join(dirs)
