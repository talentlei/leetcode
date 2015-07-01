/*
    runtime:0ms
    error:1
    匹配右括号时忘记检查stack是否为空
*/
class Solution {
public:
    bool isValid(string s) {
        stack<char> myStack;
        map<char,char> myMap;
        myMap[')']='(';
        myMap[']']='[';
        myMap['}']='{';
        for(int i=0; i<s.size(); i++){
            char ch = s[i];
            if(ch =='('||ch =='['||ch =='{')
                myStack.push(ch);
            else if(!myStack.empty()&&myStack.top()==myMap[ch])
                myStack.pop();
            else return false;
        }
        return myStack.empty();
    }
};
