import os, sys, subprocess, time, importlib

choice = input('Would you like to create a new Python Project? ')

if choice == 'yes':
    print(' ')
    name = input('Enter the name of the folder: ')
    print(' ')
    print('Creating Python Project in current directory...')
    
    os.mkdir(os.path.join(os.getcwd(), name))
    with open(os.path.join(os.path.join(os.getcwd(), name), name[0].lower() + name[1::] + '.py'), 'w') as f:
            # File Customisation
            import_type = input('Enter library import type (adv, util, basic): ')
            import_text = ''
            if import_type == 'adv':
                import_text = 'import os, sys, subprocess, time, datetime, calendar, pprint, pandas, numpy, random'
            elif import_type == 'util':
                import_text = 'import os, sys, subproces, time, random'
            elif import_type == 'basic':
                import_text = 'import os, time, random'
            else:
                print('Invalid import type. Program failed.')
                exit()
            printText = input('Enter print text: ')

            # Collating file code
            fileCode = import_text + '\n' + 'print({})'.format(printText)
                
            f.write(fileCode)

    print(' ')
    print('Project created!')
else:
    print('OK!')

    
