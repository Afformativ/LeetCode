class Solution:
    def closeStrings(self, first_word: str, second_word: str) -> bool:
       first_counter= collections.Counter(first_word)
       second_counter=collections.Counter(second_word)
       return (first_counter.keys()==second_counter.keys() and
           collections.Counter(first_counter.values())==
           collections.Counter(second_counter.values()))
      
      #Second
class Solution:
    def invariant(self,word:str):
        return set(word),collections.Counter(collections.Counter(word).values())
    def closeStrings(self, first_word: str, second_word: str) -> bool:
       return self.invariant(first_word)==self.invariant(second_word)
