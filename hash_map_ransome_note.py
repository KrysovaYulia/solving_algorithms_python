class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = dict()
        magazine_dict = dict()
        c = 0

        for i in magazine:
            magazine_dict[i] =  magazine_dict.get(i, 0) + 1

        for j in ransomNote:
            ransomNote_dict[j] =  ransomNote_dict.get(j, 0) + 1
      

        for k in ransomNote_dict:
  
            if k in magazine_dict and ransomNote_dict[k] <= magazine_dict[k]:
                c += 1

            else:
                c = 0
                break

        if c != 0:
            return True

        else:
            return False
