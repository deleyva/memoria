import sys, os, decorator

# Load Anki library
sys.path.append("anki") 
from anki.storage import Collection

# Define the path to the Anki SQLite collection
PROFILE_HOME = os.path.expanduser("/Users/Jesus/Documents/anki/Usuario 1") 
cpath = os.path.join(PROFILE_HOME, "collection.anki2")

# Load the Collection
col = Collection(cpath, log=True) # Entry point to the API

# Use the available methods to list the notes
for cid in col.findNotes("tag:Vocabulary"): 
    note = col.getNote(cid)
    front =  note.fields[0] # "Front" is the first field of these cards
    print(front)