import random

no_of_turns = 6

words_list = ['apple', 'banana', 'rainbow', 'python', 'laptop',
              'gender', 'hand', 'leg', 'infinite', 'love', 'friend', 'frienship']

guess_string = random.choice(words_list)

display_string = "_" * len(guess_string)

while no_of_turns > 0:
  print(display_string)
  guess_char = raw_input('Guess the character: ')

  temp_str = ""
  index = 0

  if guess_char in guess_string:

    for char in display_string:
      if (guess_string[index] == guess_char):
        temp_str = temp_str + guess_char
      else:
        temp_str = temp_str + char
      index += 1
      display_string = temp_str

  else:
    no_of_turns = no_of_turns - 1

  if no_of_turns == 0:
    print('|' '------------------''\n'
          '|' '                 ''|''\n'
          '|' '                 ''O''\n'
          '|' '                ''\|/''\n'
          '|' '                 ''|''\n'
          '|' '                 ''|''\n'
          '|' '                ''/|\ ''\n'
          '|' '\n'
          '|' '\n'
          '|' '\n')

  elif no_of_turns == 1:
    print('|' '------------------''\n'
          '|' '                 ''|''\n'
          '|' '                 ''O''\n'
          '|' '                ''\|/''\n'
          '|' '                 ''|''\n'
          '|' '                 ''|''\n'
          '|' '                ''/|''\n'
          '|' '\n'
          '|' '\n')

  elif no_of_turns == 2:
    print('|' '------------------''\n'
          '|' '                 ''|''\n'
          '|' '                 ''O''\n'
          '|' '                ''\|/''\n'
          '|' '                 ''|''\n'
          '|' '                 ''|''\n'
          '|' '                 ''|''\n'
          '|' '\n'
          '|' '\n')

  elif no_of_turns == 3:
    print('|' '------------------''\n'
          '|' '                 ''|''\n'
          '|' '                 ''O''\n'
          '|' '                ''\|''\n'
          '|' '                 ''|''\n'
          '|' '                 ''|''\n'
          '|' '                 ''|''\n'
          '|' '\n'
          '|' '\n')

  elif no_of_turns == 4:
    print('|' '------------------''\n'
          '|' '                 ''|''\n'
          '|' '                 ''O''\n'
          '|' '                 ''|''\n'
          '|' '                 ''|''\n'
          '|' '                 ''|''\n'
          '|' '                 ''|''\n'
          '|' '\n'
          '|' '\n')

  else:
    print('|' '------------------''\n'
          '|' '                 ''|''\n'
          '|' '                 ''O''\n'
          '|' '\n'
          '|' '\n'
          '|' '\n'
          '|' '\n'
          '|' '\n'
          '|' '\n')

  if display_string == guess_string:
   print('CONGRATULATIONS! you guesses it correct')
   print('The secret word was {}'.format(guess_string))
  elif no_of_turns == 0:
   print('Game Over.YOU LOST')

  else:
   print("turns left: " + str(no_of_turns))
