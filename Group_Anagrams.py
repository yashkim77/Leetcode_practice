def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = dict()
        for st in strs:
            sortedword="".join(sorted(st))
            
            if sortedword not in mapping:
                mapping[sortedword] = [st]
            else:
                mapping[sortedword] += [st]
        
        return mapping.values()
            
