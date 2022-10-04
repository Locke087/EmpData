"""
Important info:
Code   |         Value passed
%d     |  A code indicating the action being attempted: 0 for delete,
       |  1 for insert, and -1 for other events. Note that this is passed as a string,
       |  and not as an integer.
       
%P     |  The proposed value that the field would have
       |  after the change (key events only).

%s     |  The value currently in the field (key events only).

%i     |  The index (from 0) of the text being inserted or deleted on key events,
       |  or -1 on non-key events. Note that this is passed as a string, not as an integer.

%S     |  For insertion or deletion, the text that is being inserted or deleted (key events only).

%v     |  The widget's validate value.

%V     |  The event that triggered validation: focusin, focusout, key, or forced
       |  (indicating the text variable was changed).

%W     |  The widget's name in Tcl/Tk, as a string.

From the internet or Alan Moore's Book


New updates for CWS Project CS2450
This will build an entry widget that no matter what you input
the maximum you can enter (press Tab) will be the first 5 keys
however you can enter any type of char
Do not make using .pack a habit
this puts the entry widget in the space of a resieble tk frame
of any size.
you will also want to alter the % values for self._validate
This only checks the value that was entered that is 5 chars or less

Note: If you want to use this type of widget control you will also want to use a
mixin wrapper which really wants you to use Multiple Inheritence. For this project
trys and catches may be a better choise. There are pleny of examples on the internet
which you can find using "validation of widget values". If you want to try this out
before you go on to Multiple Inheritance or multiple classes using something like what
you see below, check out https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry-validation.html
for starters.
"""

#you only need the next two import and from lines.
import tkinter as tk
from tkinter import ttk

#start coding here
#%P has no value because if the entry is correct no change is nessary but if it isn't cut the entry
class FiveCharEntry2(ttk.Entry):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(validate='focusout', validatecommand=(self.register(self._validate), '%P'),
                    invalidcommand=(self.register(self._on_invalid),))

    #limited test for 5 keys only
    def _validate(self,proposed_value):
        return len(proposed_value)<=5

    #delete all keys past 5 keys on loss of focus
    def _on_invalid(self):
        self.delete(5,tk.END)
        
if __name__ == "__main__":
    root=tk.Tk()
    entry=FiveCharEntry2(root)
    entry.pack()
    tk.Entry(root).pack()
    root.mainloop()