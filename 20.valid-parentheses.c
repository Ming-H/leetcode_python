/*
 * @lc app=leetcode id=20 lang=c
 *
 * [20] Valid Parentheses
 */



bool isValid(string s) {
stack<char> stk;
for(const char& ch: s){
    //Handle left characters
    if(ch=='('||ch=='{'||ch=='[') {
        stk.push(ch);
        continue;
    }
    //Handle right characters
    
    if(stk.empty()) return false; //our right character has no corresponding left.
    char lastPushedLeft=stk.top();
    
    switch(ch){
        case ')':
            if(lastPushedLeft!='(') return false;break;
        case '}':
            if(lastPushedLeft!='{') return false;break;
        case ']':
            if(lastPushedLeft!='[') return false;break;
            
        default:
            //ignore any other char which is not a parenthesis
            ;
    }
    //our right had a corresponding left so let's pop it.
    stk.pop();
}
    //if we have traversed the string and not returned false yet
    //it means either all rights found their lefts
    //or there was no right and our lefts are still in stack!
    //a non-empty stack is false
    return stk.empty();

}



