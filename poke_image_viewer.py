"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import poke_api
import image_lib
import ctypes
import inspect

# Get the script and images directory
script_name = inspect.getframeinfo(inspect.currentframe()).filename
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.isdir(images_dir):
  os.makedirs(images_dir)


# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.geometry('600x600')
root.minsize(500,600)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# TODO: Set the icon
api_id = 'COMP593.PokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(api_id)
root.iconbitmap(os.path.join(script_dir,'poke_ball.ico'))

# TODO: Create frames
frm = ttk.Frame(root)
frm.columnfigure(0,weight=1)
frm.rowconfigure(0, weight=1)
frm.grid(sticy=NSEW)

#create the button of setting the desktop BG
def handle_set_desktop():
  """

  Event handler called when user clicks the "Set as desktop Image" button.
  Sets the desktop bg image to the current Pokemon Display

  """
image_lib.set_desktop_background_image(image_path)

btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image', command=handle_set_desktop)
btn_set_desktop.state('Disable')
btn_set_desktop.grid(row=1, column=0,padx=0,pady=(10,20))

#create ist of pul down pokemon names 
pokemon_list = poke_api.get_pokemon_names()
pokemon_list.sort()
cbox_poke_sel = ttk.Combobox(frm, values=pokemon_list, state = 'readonly')
cbox_poke_sel.set("Select a pokemon")

def handle_poke_sel(event):
  global image_path

  current_sel = cbox_poke_sel.get()
  image_path =poke_api.download_pokemon_artwork(current_sel, images_dir)
  if image_path:
      lbl_image['text'] = None
      photo['file'] = image_path




      else

      

# TODO: Populate frames with widgets and define event handler functions

cbox_poke_sel.bind('<<ComboboxSelected>>', handle_poke_sel)

root.mainloop()