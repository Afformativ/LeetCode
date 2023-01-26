import functools

class Solution:
    def frequencySort(self, s: str) -> str:
        @functools.cache
        def count_of(char:str)->int:
            return s.count(char)
        key=lambda char:(count_of(char),char)
        return ''.join(sorted(s,key=key,reverse=True))
      
      #Second
    class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_table=collections.Counter(s)
        key=lambda char:(frequency_table[char],char)
        return ''.join(sorted(s,key=key,reverse=True))
      
      #third
      class Solution:
    def frequencySort(self, s: str) -> str:    
        return ''.join(c*f for c , f in Counter(s).most_common())
