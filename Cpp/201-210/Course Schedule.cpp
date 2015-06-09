class Solution {
public:
    set<int> path;
    bool DFS(int cnum,vector<int >&base,vector<vector<int> >& myVec){
        if(base[cnum]==1||myVec[cnum].size()==0){
            base[cnum]=1;
            return true;
        }

        path.insert(cnum);
        for(int i=0; i<(myVec[cnum]).size(); i++){
            int c = myVec[cnum][i];
            if(path.count(c)!=0||!DFS(c,base,myVec))
                return false;
        }
        path.erase(cnum);
        base[cnum]=1;
        return true;
    }

    bool checkCycle(int cnum, vector<int >&base,vector<vector<int> >& myVec){
        return DFS(cnum,base,myVec);
    }

    bool canFinish(int numCourses, vector<pair<int, int> >& prerequisites) {
        if(numCourses<2)
            return true;
        vector<int> base(numCourses,0);
        vector<vector<int> > myVec(numCourses);
        for(size_t i=0; i<prerequisites.size(); i++){
            pair<int,int> p = prerequisites[i];
            myVec[p.second].push_back(p.first);
        }

        for(int i=0; i<numCourses; i++){
            //be checked or be required
            if(base[i]==1)
                continue;
            if(!checkCycle(i,base,myVec))
                return false;
        }
        return true;
    }
};
