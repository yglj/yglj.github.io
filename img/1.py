
import os

l = os.listdir()

with open('q.txt', 'w') as f:
    for i in l:
         f.write('- /img/' +str(i) + '\n')
