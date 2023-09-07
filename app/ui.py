import PySimpleGUI as sg
from PIL import Image

sg.set_options(element_padding=(0, 0))
image = Image.new('RGB', (600, 400))

# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Export', 'Exit']],
            ['Mode', ['Obfuscate', 'Watermark']],
            ['Help', ['About', 'Member List']]]

# ------ WaterMark Frame Defintion ------ #
watermark_frame = [[sg.Text("Press 'File > Open' select image to start.", size=(40, 1))],
                   [sg.Image(key='-IMAGE-', size=(600, 400),
                             background_color="#808080",
                             pad=(2, (2, 20)),
                             tooltip="Press 'File > Open' select image to start.")],
                   [sg.Text("Enter text:", size=(8, 1)),
                    sg.Input("", (48, 1), focus=True, tooltip="Enter text for watermark.", pad=((2, 5), 2)),
                    sg.Combo(["Mode A", "Mode B"], size=(9, 1)),
                    sg.Button("Apply", key="-APPLY-WATERMARK-", size=(8, 1), pad=((24, 0), 2))]]

# ------ Obfuscation Frame Defintion ------ #
obfuscation_frame = [[sg.Text("Press 'File > Open' select image to start.", size=(40, 1))],
                     [sg.Image(key='-IMAGE-', size=(600, 400),
                               background_color="#808080",
                               pad=(2, (2, 20)),
                               tooltip="Press 'File > Open' select image to start.")],
                     [sg.Text("Enter text:", size=(8, 1)),
                      sg.Input("", (48, 1), focus=True, tooltip="Enter text for obfuscation.", pad=((2, 5), 2)),
                      sg.Radio("Box", "obfus-type", True, size=(3, 1)),
                      sg.Radio("Blur", "obfus-type", size=(3, 1)),
                      sg.Button("Apply", key="-APPLY-WATERMARK-", size=(8, 1), pad=((5, 0), 2))]]

# ------ GUI Defintion ------ #
layout = [[sg.Menu(menu_def, )],
          [sg.Frame("Watermark", watermark_frame, size=(600, 500), key='-WATERMARK-'),
           sg.Frame("Obfuscation", obfuscation_frame, size=(600, 500), key='-OBFUSCATION-', visible=False)]]

window = sg.Window("Itinerant iterators v1.0(alpha)",
                   layout, default_element_size=(12, 1),
                   auto_size_text=False, auto_size_buttons=False,
                   default_button_element_size=(12, 1),
                   element_justification='c')

# ------ Loop & Process button menu choices ------ #
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    # ------ Process menu choices ------ #
    if event == 'About':
        # Pop up to show application description
        sg.popup('Itinerant iterators Version 1.0',
                 '--------------------------------------------------------------------',
                 'This is a GUI tool for obfuscation and steganography.',
                 'Power by PySimpleGUI',
                 title='About', line_width=500)
    elif event == 'Member List':
        # Pop up to show member list
        sg.popup('Memeber list',
                 '--------------------------------------------------------------------',
                 'smileyface12349\t\t',
                 'jj-style\t\t',
                 'HiPeople21\t\t',
                 'CactusBrothers\t\t',
                 'cloki0610',
                 title='Member List', line_width=500)
    elif event == 'Open':
        # Open a popup to select file
        filename = sg.popup_get_file('file to open', no_window=True)
        window['-IMAGE-'].update(filename)
        image = Image.open(filename)
    elif event == 'Save':
        # Open a popup to save image
        if image:
            filename = sg.popup_get_file('file to save', no_window=True, save_as=True, default_extension='.png')
            window.SaveToDisk(filename)
            image.save(filename)
    elif event == 'Watermark':
        # Switch to watermark frame
        window['-WATERMARK-'].update(visible=True)
        window['-OBFUSCATION-'].update(visible=False)
    elif event == 'Obfuscate':
        # Switch to Obfuscate frame
        window['-WATERMARK-'].update(visible=False)
        window['-OBFUSCATION-'].update(visible=True)
