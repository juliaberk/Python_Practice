import re
import math

def num_needed(phrase):
""" Check how many anomaly stickers you need to build phrase"""

  # empty dict to track number of letters
      insta_dict = {'a' : 0, 'n' : 0, 'o' : 0, 'm' : 0, 'l' : 0, 'y' : 0 }

  # take out the extra "a" in "anomaly" so we don't double-count
      for letter in "anomaly":
          if letter in phrase:
              insta_dict[letter] = len(re.findall(letter, phrase))

      insta_dict['a'] = insta_dict['a'] / 2

      max_value = max(insta_dict.values())
      
      return max_value
