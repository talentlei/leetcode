/**
 * runtime: 16ms
 * error: 1
 * 
 */ 

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> myStack;
        if(tokens.size()==0) return 0;
        for(int i=0; i<tokens.size(); i++){
            if(tokens[i]=="+"||tokens[i]=="-"||tokens[i]=="*"||tokens[i]=="/"){
                int a = myStack.top();
                myStack.pop();
                int b=  myStack.top();
                myStack.pop();
                int temp;
                if(tokens[i]=="+")
                    temp = a+b;
                else if(tokens[i]=="*")
                    temp = a*b;
                else  if(tokens[i]=="-")
                    temp = b-a;
                else temp = b/a;
                myStack.push(temp);
            }
            else myStack.push(atoi(tokens[i].c_str()));
        }
        return myStack.top();
    }
};
