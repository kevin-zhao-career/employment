import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
OrdinalConstants = {
  'Zero' : ord('0'),
  'LowerCaseA' : ord('a'),
  'UpperCaseA' : ord('A')
}

Range = {
  'Digit' : ord('9') - ord('0') + 1,
  'Alphabet' : ord('z') - ord('a') + 1
}

def rotationalCharacter(character : chr, rotation_factor : int):
  ordinal = ord(character)
  if character.isdigit():
    digit_rotation_factor = ((ordinal + rotation_factor) - OrdinalConstants['Zero']) % Range['Digit']
    return chr(OrdinalConstants['Zero'] + digit_rotation_factor)
  elif character.isalpha():
    alphabet_ordinal_constant = (OrdinalConstants['LowerCaseA'] if character.islower() else OrdinalConstants['UpperCaseA'])
    alphabet_rotation_factor = ((ordinal + rotation_factor) - alphabet_ordinal_constant) % Range['Alphabet']
    return chr(alphabet_ordinal_constant + alphabet_rotation_factor)
  
  return character

def rotationalCipher(input_string : str, rotation_factor : int):
  cipher_array = [(rotationalCharacter(character, rotation_factor) if character.isalnum() else character) for character in input_string]
  return "".join(cipher_array)

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
