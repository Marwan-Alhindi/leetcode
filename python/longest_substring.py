"""
This solves the issue of how many seuqence are there
"""
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

#         start_char = s[0]
#         sequence_init = f'{s[0]}'
#         sequence_tracker = ''
#         count = 0

#         i = 1
#         while i < len(s):
#             if s[i] == start_char:
#                 sequence_tracker += s[i]
#                 count_sequence = 1
#                 for j in range(i, i+len(sequence_init)):
#                     if s[j] == s[count_sequence]:
#                         sequence_tracker += s[j]
#                         count_sequence += 1
#                 if sequence_init == sequence_tracker:
#                     count += 1
#                     i += len(sequence_init)
#                     len_sequence = len(sequence_tracker)
#                     sequence_tracker = '' 
#                     continue  
                
#             else:
#                 sequence_init += s[i]
            
#             i += 1
        
#         return count

# x = Solution()
# print(x.lengthOfLongestSubstring('abcabcabc'))

