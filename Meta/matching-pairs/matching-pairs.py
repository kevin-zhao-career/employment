import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def has_valid_input(first_string : str, second_string : str) -> bool:
  return (len(first_string) == len(second_string)) and (len(first_string) >= 2)

def get_has_unique_characters(string : str) -> bool:
  return (len(string) <= 256) and (len(set(string)) == len(string))

def get_matching_pair_count_perfect_match_partial_match_tuple(first_string : str, second_string : str):
  matching_pair_count = 0
  has_perfect_match = False
  has_partial_match = False
  
  unmatched_pairs = set()
  first_string_unmatched_set = set()
  second_string_unmatched_set = set()
  
  for first_string_character, second_string_character in zip(first_string, second_string):  
    if (first_string_character == second_string_character):
      matching_pair_count += 1
      continue
    
    if has_perfect_match:
      continue

    unmatched_pairs.add((first_string_character, second_string_character))
    first_string_unmatched_set.add(first_string_character)
    first_string_unmatched_set.add(second_string_character)
    
    has_perfect_match |= ((second_string_character, first_string_character) in unmatched_pairs)
    has_partial_match |= (((second_string_character) in first_string_unmatched_set) or ((first_string_character) in second_string_unmatched_set))
    
  return (matching_pair_count, has_perfect_match, has_partial_match)  

def get_matching_pair_count(first_string : str, second_string : str, matching_pair_count : int, has_perfect_match : bool, has_partial_match : bool) -> bool:
    if matching_pair_count == len(first_string):
      has_unique_characters = get_has_unique_characters(first_string)
      return (matching_pair_count - 2) if has_unique_characters else matching_pair_count
  
    if has_perfect_match:
      return matching_pair_count + 2
  
    if has_partial_match:
      return matching_pair_count + 1
    
    return matching_pair_count
  

def matching_pairs(first_string : str, second_string : str):
  if not has_valid_input(first_string, second_string):
    raise ValueErrror("Invalid Input Detected")
  
  (matching_pair_count, has_perfect_match, has_partial_match) = get_matching_pair_count_perfect_match_partial_match_tuple(first_string, second_string)
  
  return get_matching_pair_count(first_string, second_string, matching_pair_count, has_perfect_match, has_partial_match)




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
    print()
  test_case_number += 1

if __name__ == "__main__":
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
