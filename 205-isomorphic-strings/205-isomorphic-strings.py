class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_mapping_s_t = {}
        dic_mapping_t_s = {}
        
        for c1, c2 in zip(s, t):            
            if (c1 not in dic_mapping_s_t) and (c2 not in dic_mapping_t_s):
                dic_mapping_s_t[c1] = c2
                dic_mapping_t_s[c2] = c1
                        
            elif dic_mapping_s_t.get(c1) != c2 or dic_mapping_t_s.get(c2) != c1:
                return False
            
        return True