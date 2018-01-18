# class Open_file():
#     def __enter__(self):
#         self.file = open(self.filename,self.mode)
#         print('in enter function')
#         return  self.file
#     def __init__(self,filename,mode):
#         self.filename = filename
#         self.mode = mode
#         print('in init function')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('in exit function')
#         self.file.close()
#
# with Open_file('sample.txt', 'w') as f:
#     f.write('with syntax testing')
#     print('writing to the txt file')
#
# print(f.closed)



from contextlib import contextmanager
@contextmanager
def open_file(file,mode):
    try:
        f = open(file,mode)
        yield f
    finally:
        f.close()

with open_file('sample.txt', 'w') as f:
    f.write('with syntax testing in function')
    print('writing to the txt file')

print(f.closed)
