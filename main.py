import sys

def has_one_one_mapping(s1, s2):
     if len(s1) <= len(s2):
         d = {}
         for i in range(len(s1)):
             if s1[i] not in d:
                 d[s1[i]] = s2[i]
             if d[s1[i]] != s2[i]:
                 return False
         return True
     return False

def len_different_one_one_mapping(s1, s2):
     set1 = set()
     set2 = set()
     for c in s1:
         set1.add(c)
     for c in s2:
         set2.add(c)
     if len(set1) >= len(set2):
         return True
     else:
         return False

def main():
     if len(sys.argv) != 3:
         return False
     s1 = sys.argv[1]
     s2 = sys.argv[2]
     str1_length = len(s1)
     str2_length = len(s2)
     if str1_length == str2_length:
         print(has_one_one_mapping(s1, s2))
     else:
         print(len_different_one_one_mapping(s1, s2))
main()
