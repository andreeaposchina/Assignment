
# Define a function that receive as a single argument a list of strings like the below variable and
# return a dictionary that contains as keys “Video”, “Audio”, “Other” and as values a list with the
# entries specific for that key.
# e.g. results = ["Entry One.mp4", "Entry Two.wav", "Entry Three.jpg", "Entry Four.mng",
# "Entry Five.png", "Entry Six.csv"]

from pprint import pprint


def return_format(list_of_files: list) -> dict:

    extensions_dictionary = {'Video': ['mng', 'mkv', 'avi', 'mp4', 'mpg', 'flv'],
                             'Audio': ['mp3', 'wav']
                             }

    returned_dict = {'Video': [],
                     'Audio': [],
                     'Other': []
                     }

    list_of_extensions = [elem.split('.') for elem in list_of_files]

    for i in range(len(list_of_files)):
        if list_of_extensions[i][1] in extensions_dictionary['Video']:
            returned_dict['Video'].append(list_of_files[i])
        elif list_of_extensions[i][1] in extensions_dictionary['Audio']:
            returned_dict['Audio'].append(list_of_files[i])
        else:
            returned_dict['Other'].append(list_of_files[i])

    return returned_dict


pprint(return_format(["Entry One.mp4", "Entry Two.wav", "Entry Three.jpg",
                      "Entry Four.mng", "Entry Five.png", "Entry Six.csv"]))

pprint(return_format(["Entry One.jpeg", "Entry Two.zip", "Entry Three.tar",
                      "Entry Four.flv", "Entry Five.mp3", "Entry Six.json"]))

