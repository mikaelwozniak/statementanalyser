import re

def is_match(pattern,content):
    matchObj = re.match(pattern, content, re.I )
    return matchObj!=None
    
def get_match_groups(pattern,content):
    matchObj = re.match(pattern, content, re.I )
    if matchObj:
        result = []
        for i in range(matchObj.lastindex):
            result.append(matchObj.group(i+1))
        return result
    else:
        None