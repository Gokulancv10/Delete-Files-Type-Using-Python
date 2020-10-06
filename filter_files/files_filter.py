
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

obj = Files(copy the dir path and replace all '/' to '\' , (file types with comma separated))
obj.remove_files()
