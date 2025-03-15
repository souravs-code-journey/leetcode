from typing import  List

class Solutions:
    def first_letter_to_appear_twice(self,s:str) -> str:
        """
        Iterate through the list if elemt is in the hasset then return the character
        else add it to the hashset
        """
        hashset = set()

        for i in s:
            if i in hashset:
                return i
            hashset.add(i)
        return " "



if __name__ == '__main__':
    s = "abcdefadb"
    sol = Solutions()
    val = sol.first_letter_to_appear_twice(s)
    print(val)

