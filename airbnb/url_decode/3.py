target=''
def helper(s, idx):
    if idx==len(s):
        return s==target
    if s[idx].isalpha():
        uid=helper(s.substr(0, idx)+s[idx].upper()+s[idx+1], idx+1)
        lid=helper(s.substr(0, idx)+s[idx].lower()+s[idx+1], idx+1)
    else:
        return helper(s, idx+1)