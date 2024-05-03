import random

word_list = ["Quark", "Ozean", "Rache", "Pizza", "Tasse", "Video", "Wurst", "Vater", "Pfad", "Nacht", "Insel", "Jacke", "Clown", "Adler"]
answer = random.choice(word_list)

def get_clue(ans, guess):
  clue = ""
  for idx, letter in enumerate(guess):
    if letter == ans[idx]:
      clue += "R"
    elif letter in ans:
      clue += "F"
    else:
      clue += "-"
  return clue

print("R steht für: Buchstabe richtig. F steht für: Buchstabe falsch.") 
for x in range(1,7):
  guess = input("Word? ")[0:5]
  print(get_clue(answer, guess), x)
  if answer == guess:
    break

input()