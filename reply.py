import random

def reply():
    replies = [
        'Yeh! Copied to ClipBoard!',
        'Hurray! PWD copied',
        'Password is on ClipBoard',
        'Ctrl+V to see your pwd']
    
    return random.choice(replies)
