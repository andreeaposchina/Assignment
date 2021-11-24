
# Define a function that receive as a single argument a list of strings like the below variable and
# return a dictionary that contains as keys “Video”, “Audio”, “Other” and as values a list with the
# entries specific for that key.
# e.g. results = ["Entry One.mp4", "Entry Two.wav", "Entry Three.jpg", "Entry Four.mng",
# "Entry Five.png", "Entry Six.csv"]

from pprint import pprint


def return_format(list_of_files: list) -> dict:

    extensions_dictionary = {'Video': ['.mng', '.mkv', '.avi', '.mp4', 'mpg', '.flv'],
                             'Audio': ['.mp3', '.wav']
                             }

    returned_dict = {'Video': [],
                     'Audio': [],
                     'Other': []
                     }

    for element in list_of_files:
        if element[-4:] in extensions_dictionary['Video']:
            returned_dict['Video'].append(element)
        elif element[-4:] in extensions_dictionary['Audio']:
            returned_dict['Audio'].append(element)
        else:
            returned_dict['Other'].append(element)

    return returned_dict


pprint(return_format(["Entry One.mp4", "Entry Two.wav", "Entry Three.jpg",
                      "Entry Four.mng", "Entry Five.png", "Entry Six.csv"]))
