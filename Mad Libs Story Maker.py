##Readme
# Story with selected lexical categories isolated
# way to traverse story and pull out required lexical categories and assign them an order of occurance and the user input variable
# append the list to the story in the correct order and print out new story

# account for capatalization in names
# change "a" to "an" when the following word in the sentence begins with a vowel

story = """Pizza was invented by a [adjective] [nationality] chef named [person].
To make a pizza, you need to take a lump of [noun], and make a thin, round [adjective] [noun]. Then
you cover it with [adjective] sauce, [adjective] cheese, and fresh chopped [plural noun]. Next you have
to bake it in a very hot [noun]. When it is done, cut it into [number] [plural shape]. Some kids like [food] pizza the best,
but my favourite is the [food] pizza. If I could, I would eat pizza [number] times a day!"""

story_test = """Pizza was invented by a [adjective] [nationality] chef named [person]."""

def ml_maker_while(story):
    modified_story = list(story)
    vowels = 'aeiou'
    title_words = ["person", "nationality"]
    try:
        while modified_story.index("]"):
            start_point = modified_story.index("[")
            end_point = modified_story.index("]")
            lexical_cat = "".join(modified_story[start_point+1:end_point])
            determiner = 'an' if modified_story[start_point + 1] in vowels else 'a'
            user_input = input("Please enter {} {}: ".format(determiner, lexical_cat))
            modified_story[start_point:end_point+1] = user_input if lexical_cat not in title_words else user_input.title()
            if user_input[0] in vowels and "".join(modified_story[start_point-3:start_point]) == ' a ':
                modified_story[start_point-3:start_point] = " an "
    except:
        pass
    return "\nYour new story is:\n{}".format("".join(modified_story))

def ml_maker(story):
    modified_story = story.split()
    vowels = 'aeiou'
    punctuation_marks = '.,;:?!'
    for index, word in enumerate(modified_story):
        if word[0] == "[":
            determiner = 'an' if word[1] in vowels else 'a'
            if word[-1] in punctuation_marks:
                user_input = input("Please enter {} {}: ".format(determiner, "".join(word[1:-2])))
                modified_story[index] = user_input + word[-1]
            else:
                user_input = input("Please enter {} {}: ".format(determiner, "".join(word[1:-1])))
                modified_story[index] = user_input
            try:
                if user_input[0] in vowels and modified_story[index-1] == 'a':
                    modified_story[index-1] = 'an'
            except:
                pass
    return "\nYour new story is:\n{}".format(" ".join(modified_story))

print(ml_maker_while(story))
