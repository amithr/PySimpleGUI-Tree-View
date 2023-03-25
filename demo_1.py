import PySimpleGUI as sg

# https://github.com/PySimpleGUI/PySimpleGUI/issues/3772

tree_data = sg.TreeData()

sg.set_options(font=("Arial Bold",14))

data = [
   ["","BIO", "Biology", "", "", ""],
   ["BIO", "ADR", "Adrian", 97, 83, 92],
   ["BIO", "LIA", "Liam", 89, 91, 101],
   ["BIO", "CEL", "Celia", 101, 95, 102],
   ["","CHM", "Chemistry", "", "", ""],
   ["CHM", "ADR", "Adriam", 85, 91, 99],
   ["CHM", "LIA", "Liam", 86, 100, 92],
   ["CHM", "CEL", "Celia", 99, 101, 98]
]

headings = ['Quiz 1','Homework 1','Quiz 2']

for row in data:
   tree_data.Insert(row[0], row[1], row[2], row[3:])

layout = [
   [sg.Tree(
        data=tree_data,
        headings=headings,
        auto_size_columns=True,
        select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
        num_rows=10,
        col0_width=5,
        key='-TREE-',
        show_expanded=True, # Shows already expanded out
        enable_events=True,
        expand_x=True,
        expand_y=True,
    )],
    [sg.Button('Insert')]
]

window=sg.Window("Gradebook", layout, size=(600, 300), resizable=True)

while True:
   event, values = window.read()
   print ("event:",event, "values:",values)
   if event == sg.WIN_CLOSED:
      break
window.close()