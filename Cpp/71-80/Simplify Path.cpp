/*
  runtime: 8ms
  error: 2
  path.find()
  dir==".."

*/

class Solution {
public:
    string simplifyPath(string path) {
        if(path.size()==0) return path;
        stack<string> myStack;
        path = path+"/";
        int ind,lastpos=0;
        while((ind=path.find("/",lastpos))!=-1){
            string dir = path.substr(lastpos,ind-lastpos);
            lastpos = ind+1;
            if(dir==""||dir==".")
                continue;
            if(dir==".."){
                if(!myStack.empty())
                    myStack.pop();
            }
            else myStack.push(dir);
            
        }string res="";
        while(!myStack.empty()){
            res = myStack.top()+"/"+res;
            myStack.pop();
        }
        res = "/"+res.substr(0,res.size()-1);
        return res;
    }
};
