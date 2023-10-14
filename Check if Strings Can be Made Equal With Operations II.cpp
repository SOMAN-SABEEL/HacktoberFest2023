class Solution {
public:
    bool checkStrings(string s1, string s2) {
        multiset<int> st,st1,st2,st3;
        for(int i=0;i<s1.size();i++){
            if(i%2) st1.insert(s1[i]);
            else st.insert(s1[i]);
        }
        for(int i=0;i<s2.size();i++){
            if(i%2) st3.insert(s2[i]);
            else st2.insert(s2[i]);
        }
        if(st==st2 && st1==st3) return 1;
        else return 0;
    }
};
