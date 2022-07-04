## This code is from Yagisanatode's git, but i didn't know how to clone

###Changing the colour of selected text in Tkinter Text wiget###

from tkinter import *
from tkinter import ttk

root = Tk(  )




# fill rest of root with a Text and put some text there
BotInput = "This usually links to a database dictionary of responses."


###This is were the magic happens###
# action-function for the Button: highlight all occurrences of string
def find(  ):
    
    # get string to look for (if empty, no searching)
    s = "Bottity Bottity Bot Bot:"
    if s:
        # start from the beginning (and when we come to the end, stop)
        idx = '1.0'
        
        
        while 1:
            # find next occurrence, exit loop if no more
            idx = text.search(s, idx, nocase=1, stopindex=END)
            if not idx: break
            # index right after the end of the occurrence
            
            lastidx = '%s+%dc' % (idx, len(s))
           
            
            # tag the whole occurrence (start included, stop excluded)
            text.tag_add('found', idx, lastidx)
            # prepare to search for next occurrence
            idx = lastidx
        # use a red foreground for all the tagged occurrences
        text.tag_config('found', foreground='red')

# This displays the entries from the Bot and the User in the text    
def display_entry(*args):
    UserInput = Comment.get()
    text.insert(END,
    'Bottity Bottity Bot Bot: '+ BotInput + '\n')
    text.insert(END,
    'User: ' +UserInput +'\n')
    Comment.delete(0,END)
    #Runs the function
    find()

#Creat text wiget
text = Text(root)

text.pack()

#Entry field to add content to text wiget.
Comment_Lbl = ttk.Label(root, text="Comment here:")
Comment_Lbl.pack()

Comment = ttk.Entry(root)
Comment.pack()
Comment.bind("<Return>", display_entry)
Comment.focus()
Comment_Button = ttk.Button(root, text="Enter", command = lambda:display_entry(None))
        
Comment_Button.pack()

root.mainloop(  )