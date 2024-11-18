# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_words(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    for i in words:
      guesses += 1
      if (w+i == password):
        return True, guesses
  return False, guesses

def two_words_and_a_digit(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for n in range(10):
    for w in words:
      for i in words:
        guesses += 1
        if (w+i+str(n) == password):
          return True, guesses
        else:
          guesses += 1
          if (str(n)+w+i == password):
            return True, guesses
  return False, guesses

def one_word_random_capital(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    letterCount = list(w)
    for l in range(len(letterCount)):
      letter_list = list(w)
      guesses += 1
      lol = letter_list[l].upper()
      letter_list[l] = lol
      s = ""
      wordy = s.join(letter_list)
      if (wordy == password):
        return True, guesses
  return False, guesses