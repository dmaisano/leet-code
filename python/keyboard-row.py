'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
'''

# Using the sets makes life easier
def findWords(words):
  res = []  # store the resulting words in a list

  lines = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]

  for word in words:
    char = set(word.lower()) # converts the word to a set of characters/letters

    for line in lines:

      # if the set of letters (char) is a subset of a line
      # then it can be typed using the characters of that line
      if(char.issubset(line)):
        res.append(word)
        # append the word to the result list

  return res;


test = ["Hello","Alaska","Dad","Peace"]

test = findWords(test)

for t in test:
  print(t, '\n')
