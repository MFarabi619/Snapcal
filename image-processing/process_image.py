import easyocr
import os
import time
from pprint import pprint
import re
import copy

# TODO:
# - we now have a function that can process and image and return the text with bounding boxes.
# start with event_name and date and time
# only focus on events with starting and ending time.

# - [ ] parse date time.

DEBUG = True

def dbg(*args, **kwargs):
    if DEBUG:
        pprint(*args, **kwargs)


print(os.getcwd())

test_lines = [([[31, 10], [742, 10], [742, 84], [31, 84]],
  'Games Night @ The Loft',
  0.9909720987755923),
 ([[29, 95], [687, 95], [687, 131], [29, 131]],
  'Join us to play some fun board games and make new friends:',
  0.5558608794319378),
 ([[32, 162], [237, 162], [237, 200], [32, 200]],
  'Sept 15th, 6.30 -',
  0.46984423191912145),
 ([[248, 164], [406, 164], [406, 194], [248, 194]],
  '8.30 PM EST',
  0.9848330215778436)]

# @returns a list of [x,y], text and model confident level,
def extract_text(image_name):
    start_time = time.time()

    # Change to accept image as bytes bc it will come over the network
    reader = easyocr.Reader(['en']) 
    result = reader.readtext('./sample-set/' + image_name)

    end_time = time.time()
    runtime = end_time - start_time

    print(f"{image_name} took:  {runtime:.6f}")

    return result

# Merge all the text into one and use language processing to detect a date embedded.
def extract_date_and_time(text_lines):
    # Only lines with date info
    filtered_text = ''
    consumed_indices = []

    matcher = ['']

    # Try a regex detector to find lines relevant to date and time to reduce the list of items
    patterns = [ 
        r'(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)'
        ,r'\b(?:1[0-2]|0?[1-9])(:|.)[0-5][0-9](?:\s?[APap][Mm])?\b|\b2[0-3]:[0-5][0-9]\b'

    ]

    for l_index in range(len(text_lines)):

        # stop searching if we already found a match.
        found = False


        text = text_lines[l_index][1]
        dbg("checking: " + text)

        for i in range(len(patterns)):
            if not found:
                pattern = patterns[i]
                matches = re.findall(pattern, text)
                if matches:
                    found = True
                    filtered_text += text
                    consumed_indices.append(l_index)
                    dbg("matched on pattern: " + str(i))
                    dbg('matches:')
                    dbg(matches)

    # TODO: parse this into an actual date time.
    return { 
        'date_time_text': filtered_text,
        # report which pieces of the text were date time so we can consider that when looking for other 
        # parts such as heading and description.
        'consumed_indices' : consumed_indices
    }
    
def construct_event(text_lines):
    pprint(text_lines)

    results = extract_date_and_time(text_lines)
    pprint (results)

    # remove consumed lines
    new_list = []

    for i in range(len(text_lines)):
        if not (i in results['consumed_indices']):
            new_list += text_lines[i]
            
    dbg("filtered list: ")
    dbg(new_list)


# Record the start time
# text_lines = extract_text('games_night.png')
event = construct_event(test_lines)




# Calculate the runtime

# pprint.pprint(text_lines)
