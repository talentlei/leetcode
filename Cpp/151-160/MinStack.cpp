/*
    runtime: 40ms
    error : 0
*/

class MinStack {
public:
    
    void push(int x) {
        myStack.push_back(x);
        pos++;
        if(pos>0&&x<Min[pos-1]||pos==0)
            Min.push_back(x);
        else
            Min.push_back(Min[pos-1]);
    }

    void pop() {
        if(pos==-1) return;
        myStack.pop_back();
        Min.pop_back();
        pos--;
    }

    int top() {
        if(pos==-1) return -1;
        return myStack[pos];
    }

    int getMin() {
        if(pos==-1) return -1;
        return Min[pos];
    }
private:
    vector<int> myStack;
    vector<int> Min;
    int pos = -1;
};
