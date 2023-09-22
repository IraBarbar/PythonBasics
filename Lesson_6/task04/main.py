import mystery

COUNT_ = 2
puzzles = mystery.dict_puzzles()
for key, val in puzzles.items():
    attempt = mystery.mistery_guesses(key, val, COUNT_)
    mystery.dict_count_attempts(key, attempt)

mystery.read_dict_count_attempts()


                                                   