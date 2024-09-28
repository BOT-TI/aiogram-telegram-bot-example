import os, json

# Open the 'config.json' file
with open(os.path.abspath('config.json'), 'r') as config_file:
    # Load the JSON data from the file
    config = json.load(config_file)