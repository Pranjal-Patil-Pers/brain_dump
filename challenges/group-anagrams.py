class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for str1 in strs:
            temp_str = "".join(sorted(str1))
            if temp_str in dict1:
                dict1[temp_str].append(str1)
            else :
                dict1[temp_str] = [str1]
        return list(dict1.values())


if __name__ == "__main__":
  sol=Solution()
  print("output:",sol.groupAnagrams(["eat", "tea", "bat","tab","ate","rat"]))
