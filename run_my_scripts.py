"""
This is the main script that will run scripts sequentially.

Creating a script requirements:
- All images that are referenced in the script must be in the same directory name in images/
    Ex: creating a script foo.py, any image should be under the path images/foo/
"""
from util.script_queue import ScriptQueue

# TEMPLATE ADD YOUR SCRIPT NAMES HERE
scripts = [
    'open_sw', #This script gets you to the home and clicks through all events
]
queue = ScriptQueue(scripts)
queue.run()