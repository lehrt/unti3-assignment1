# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T', ' '],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def transform(old_dictionary):
    new_point_structure = {}
    for point in old_dictionary:
        for letter in old_dictionary[point]:
            new_point_structure[letter] = point
    return new_point_structure

def initial_prompt():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    user_input = input("Let's play some Scrabble!\n")

    for char in user_input:
        if char.upper() not in letters: 
            print("\nEnter a real word please. Try again.\n")
            user_input = initial_prompt()
            break
    return user_input

def scorer_prompt():
    user_input = 0
    try:
        user_input = int(input("Which scoring algorithm would you like to use?\n\n0 - Simple: One point per character\n1 - Vowel Bonus: Vowels are worth 3 points\n2 - Scrabble: Uses scrabble point system\nEnter 0, 1, or 2:"))
    except:
        print("Enter only 0, 1, or 2!\n\n")
        scorer_prompt()

    return user_input

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""
    total_points = 0

    for char in word:
        for point_value in old_point_structure:
            if char in old_point_structure[point_value]:
                if char == " ":
                    letterPoints += 'Points for  : 0\n'
                else: 
                    letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
                    total_points += point_value
    return (f"{letterPoints} \nTotal points: {total_points}")

def simple_scorer(word):
    word = word.upper()
    letterPoints = ""
    total_points = 0

    for char in word:
        if char == " ":
            letterPoints += 'Points for  : 0\n'
        else:
            letterPoints += f'Points for {char}: 1\n'
            total_points += 1
    return (f"{letterPoints} \nTotal points: {total_points}")

def vowel_bonus_scorer(word):
    word = word.upper()
    letterPoints = ""
    total_points = 0
    vowels = "AEIOUY"

    for char in word:
            if char in vowels:
                letterPoints += f'Points for {char}: 3\n'
                total_points += 3
            else:
                if char == ' ':
                    letterPoints += 'Points for  : 0\n'
                else:
                    letterPoints += f'Points for {char}: 1\n'
                    total_points += 1
    return (f"{letterPoints} \nTotal points: {total_points}")

def scrabble_scorer():
    return

def run_program():
    word = initial_prompt()
    answer = ""
    type_of_score = scorer_prompt()
    if type_of_score == 0:
        answer = simple_scorer(word)
    if type_of_score == 1:
        answer = vowel_bonus_scorer(word)
    if type_of_score == 2:
        answer = old_scrabble_scorer(word)
    return answer

