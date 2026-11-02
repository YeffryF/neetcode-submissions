class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        obj_1 = {}
        obj_2 = {}

        for char in s:
            if char in obj_1:
                obj_1[char] +=1
            else:
                obj_1[char] = 1

        for char in t:
            if char in obj_2:
                obj_2[char] +=1
            else:
                obj_2[char] = 1

        for key in obj_1:
            if obj_1[key] == obj_2[key]:
                return True




