import random 

words = {'apple', 'orange', 'banana', 'coconut', 'watermelon'}

Hangman_art = {0:('   ',
                 '   ',
                 '   '),
               1:(' O ',
                 '   ',
                 '   '),
               2:(' O ',
                 ' | ',
                 '   '),
               3:(' O ',
                  '/| ',
                 '   '),
               4:(' O ',
                  '/|\\',
                 '    '), 
               5:(' O ',
                  '/|\\',
                  '  \\'), 
               6:('  O ',
                 ' /|\\',
                 ' / \\')}

for line in Hangman_art[1]:
    print(line)