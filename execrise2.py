# Define a function that takes a list of strings and prints them, one per line, in a rectangular frame.
# For example, the list ["Hello", "World", "in", "a", "frame"] gets printed as:
# *********
# * Hello *
# * World *
# * in    *
# * a     *
# * frame *
# *********


def frame_words(list_of_words: list) -> str:
    """
    This method takes a list of strings and prints the one by line in a rectangular frame
    :param list_of_words: The list of words that should be framed
    :return: A string which represents the framed words for the given list
    """

    frame_length = max([len(word) for word in list_of_words])
    framed_words = '*' * (frame_length + 4) + '\n'
    for word in list_of_words:
        framed_words += '* ' + word + ' ' * (frame_length - len(word)) + ' *\n'
    framed_words += '*' * (frame_length + 4) + '\n'

    return framed_words


print(frame_words(["Hello", "World", "in", "a", "frame"]))

print(frame_words([""]))

print(frame_words(["I", "Framed", "all", "words", "from", "this", "list"]))
