"""
Quote Loader Program ver.1.0.

This program loads a quote from an external file into a tkinter window.

In the external text file every new line is a different quote.
"""

# importing modules
from tkinter import Tk, Label, mainloop, Button
import time, random


def quote_change():														# define function
	quotetext = realquotes[random.randint(0,len(realquotes)-1)]			# selects a random line from the text
	quote_label.config(text=quotetext)									# loads text into label
	quote_label.after(25000,quote_change)								# reloads the whole label element

if __name__ == '__main__':
	realquotes = open('quotes.text','r', encoding = 'utf-8').readlines()	# open external file; encoded with utf-8

	root = Tk()																		# initiate Tk module, title and dimensions, background color
	root.wm_title("Quotes")
	root.geometry("350x160+0+0")
	root.configure(background="black")

	quote_label = Label(master=root,font=("Arial",12),fg="white",bg="black",justify='left',wraplength=300)	# initiate label widget, dinamically expandable
	quote_label.pack(expand=1)

	quote_change()				# reload after 25 seconds
	root.mainloop()				# run mainloop