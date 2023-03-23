import PySimpleGUI as sg

# https://github.com/PySimpleGUI/PySimpleGUI/issues/3772

sg.set_options(font=("Arial Bold",14))


data = [
   ["","BIO", "Biology", "", "", ""],
   ["BIO", "ADR-BIO", "Adrian", 97, 83, 92],
   ["BIO", "LIA-BIO", "Liam", 89, 91, 101],
   ["BIO", "CEL-BIO", "Celia", 101, 95, 102],
   ["","CHM", "Chemistry", "", "", ""],
   ["CHM", "ADR-CHM", "Adriam", 85, 91, 99],
   ["CHM", "LIA-CHM", "Liam", 86, 100, 92],
   ["CHM", "CEL-CHM", "Celia", 99, 101, 98]
]

headings = ['Quiz 1','Homework 1','Quiz 2']

def generate_tree_data_object(data):
    tree_data = sg.TreeData()
    for row in data:
        tree_data.Insert(row[0], row[1], row[2], row[3:])
    return tree_data   

def extract_subjects(data):
    subjects = []
    for i in range(len(data)):
        if data[i][0] == "":
            subjects.append(data[i][1])
    return subjects

subject_list = extract_subjects(data)

layout = [
   [sg.Tree(
        data=generate_tree_data_object(data),
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
    [sg.Text('Subject:'), sg.Combo(subject_list, default_value=subject_list[0], key='-SUBJECT-', font=('Arial Bold', 14), enable_events=True,  readonly=False)],
    [sg.Text('Name:'), sg.Input('', enable_events=True, size=(10, 1), key='-NAME-', font=('Arial Bold', 20), justification='right')],
    [sg.Text('Quiz 1:'), sg.Input('', enable_events=True, size=(2,1), key='-QUIZ_1-', font=('Arial Bold', 20), justification='right')],
    [sg.Text('Assignment 1:'), sg.Input('', enable_events=True, size=(2,1), key='-ASSIGN_1-', font=('Arial Bold', 20), justification='right')],
    [sg.Text('Quiz 2:'), sg.Input('', enable_events=True, size=(2,1), key='-QUIZ_2-', font=('Arial Bold', 20), justification='right')],
    [sg.Button('Insert'), sg.Button('Delete')]
]

window=sg.Window("Gradebook", layout, size=(600, 600), resizable=True)

def insert_record(subject, name, scores, tree_element):
    for i in range(len(data)):
       if data[i][0] == "" and data[i][1] == subject:
            j = i + 1
            while (j < len(data)) and (data[j][0] == data[i][1]):
                j += 1
            data.insert(j, [subject, name[0:2], name, scores[0], scores[1], scores[2]])
            tree_data = generate_tree_data_object(data)
            tree_element.update(tree_data)

def delete_record(selected_row_code, tree_element):
    for row in data:
        if selected_row_code == row[1]:
            data.remove(row)
    tree_data = generate_tree_data_object(data)
    tree_element.update(tree_data)
   
   
selected_row_code = ""
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == 'Insert':
        tree_element = window['-TREE-']
        insert_record(values['-SUBJECT-'], values['-NAME-'], [values['-QUIZ_1-'], values['-ASSIGN_1-'], values['-QUIZ_2-']], tree_element)
    elif event == '-TREE-':
        selected_row_code = values['-TREE-'][0]
    elif event == 'Delete':
        tree_element = window['-TREE-']
        delete_record(selected_row_code, tree_element)
    
window.close()