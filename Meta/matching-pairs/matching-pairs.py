import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def has_valid_input(string_1 : str, string_2 : str) -> bool:
  return (len(string_1) == len(string_2)) and (len(string_1) >= 2)

def get_has_unique_characters(string : str) -> bool:
  return (len(string) <= 256) and (len(set(string)) == len(string)) 

def get_has_partial_match_perfect_match_tuple(string_1 : str, string_2 : str):
  has_partial_match = False
  has_perfect_match = False
  
  unmatched_pairs = set()
  string_1_unmatched_set = set()
  string_2_unmatched_set = set()
  
  for string_1_character, string_2_character in zip(string_1, string_2):
    if (string_1_character == string_2_character):
      continue
    
    unmatched_pairs.add((string_1_character, string_2_character))
    string_1_unmatched_set.add(string_1_character)
    string_2_unmatched_set.add(string_2_character)
    
    has_partial_match |= (((string_2_character) in string_1_unmatched_set) or ((string_1_character) in string_2_unmatched_set))
    has_perfect_match |= ((string_2_character, string_1_character) in unmatched_pairs)
  
  return (has_partial_match, has_perfect_match)

def get_matching_pair_count_perfect_match_partial_match_tuple(string_1 : str, string_2 : str):
  matching_pair_count = 0
  
  (has_partial_match, has_perfect_match) = get_has_partial_match_perfect_match_tuple(string_1, string_2)
  
  for string_1_character, string_2_character in zip(string_1, string_2):  
    if (string_1_character == string_2_character):
      matching_pair_count += 1
    
  return (matching_pair_count, has_perfect_match, has_partial_match)  

def get_matching_pair_count(string_1 : str, string_2 : str, matching_pair_count : int, has_perfect_match : bool, has_partial_match : bool) -> bool:
    if not has_valid_input(string_1, string_2):
      raise ValueErrror("Invalid Input Detected")   
    
    string_1_has_unique_characters = get_has_unique_characters(string_1)
    string_2_has_unique_characters = get_has_unique_characters(string_2)
    
    if ((matching_pair_count == len(string_1)) or (matching_pair_count == len(string_2))):
      return (matching_pair_count - 2) if (string_1_has_unique_characters or string_2_has_unique_characters) else (matching_pair_count)
  
    unmatched_pair_count = len(string_1) - matching_pair_count
  
    if has_perfect_match:
      return matching_pair_count + 2
  
    if has_partial_match:
      return (matching_pair_count + 1) if (unmatched_pair_count > 1) else (matching_pair_count - 1)
    
    return matching_pair_count if ((unmatched_pair_count > 1) or (not string_1_has_unique_characters) or (not string_2_has_unique_characters)) else (matching_pair_count - 1)
  

def matching_pairs(string_1 : str, string_2 : str):
  if not has_valid_input(string_1, string_2):
    raise ValueErrror("Invalid Input Detected")
  
  (matching_pair_count, has_perfect_match, has_partial_match) = get_matching_pair_count_perfect_match_partial_match_tuple(string_1, string_2)
  
  return get_matching_pair_count(string_1, string_2, matching_pair_count, has_perfect_match, has_partial_match)

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
  test_case_number += 1
  #print("\n")
  
def advanced_check(string_1, string_2, expected_output):
  actual_output = matching_pairs(string_1, string_2)
  print("String 1: ", string_1, " String 2: ", string_2)
  check(expected_output, actual_output)

if __name__ == "__main__":
  advanced_check("abcde", "adcbe", 5)
  advanced_check("abcd", "abcd", 2)

  # Add your own test cases here
  advanced_check('abcd', 'abcd', 2)
  advanced_check('abcde', 'adcbe', 5)

  advanced_check('aa', 'aa', 2)
  advanced_check('aa', 'bb', 0)

  advanced_check('at', 'at', 0)
  advanced_check('at', 'ta', 2)
  advanced_check('ax', 'ya', 1)

  advanced_check('ax', 'aa', 1)
  advanced_check('aa', 'ax', 1)

  advanced_check('abx', 'abb', 2)
  advanced_check('abb', 'axb', 2)

  advanced_check('ax', 'ay', 0)
  advanced_check('axb', 'ayb', 1)

  advanced_check('ABC', 'ADB', 2)
  advanced_check('abcde', 'axcbe', 4)
  advanced_check('docomo', 'docomo', 6)

  advanced_check('abcdc', 'baccd', 3)
  advanced_check('abcdx', 'abxcc', 4)

  advanced_check('abcd', 'adcb', 4)
  advanced_check('mno', 'mno', 1)
  advanced_check('abcde', 'adcbe', 5)

  advanced_check('abcd', 'abcd', 2)
  advanced_check('abcd', 'efgh', 0)
  advanced_check('abcd', 'abce', 2)
  advanced_check('abczz', 'abcee', 3)
  advanced_check('abc', 'abd', 1)
  advanced_check('mnode', 'mnoef', 4)

  advanced_check('abxce', 'abcdx', 3)
  advanced_check('dd', 'dd', 2)
  
