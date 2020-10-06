import os

"""
d = "D:/Courses/The Complete Networking Fundamentals Course/2. Basic Networking Terms"

# Return all files in dir, and all its subdirectories, ending in pattern
def gen_files(dir, pattern):
   for dirname, subdirs, files in os.walk(dir):
      for f in files:
         if f.endswith(pattern):
            yield os.path.join(dirname, f)


# Remove all files in the current dir matching *.config
pattern = ('.srt', '.vtt')
for f in gen_files(d, pattern):
   os.remove(f)
"""

import os
class Files:

    def __init__(self, dir, pattern):
        self.dir = dir
        self.pattern = pattern

    def gen_files(self, dir, pattern):
        for dirname, subdirs, files in os.walk(self.dir):
            for f in files:
                if f.endswith(self.pattern):
                    yield os.path.join(dirname, f)

    def remove_files(self):

        for f in self.gen_files(self.dir, self.pattern):
            os.remove(f)

obj = Files("D:/Courses/The Complete Networking Fundamentals Course/3. OSI Model", (".srt", ".vtt"))
obj.remove_files()
