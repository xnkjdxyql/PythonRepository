import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Project Folder "+directory)
        os.makedirs(directory)


def create_data_files(project_name,base_url='Nothing Need To Be Write(default)'):
    queue = project_name + 'queue.txt'
    crawled = project_name + 'crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url+'\n')
    if not os.path.isfile(crawled):
        write_file(crawled,'')

def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')

def delete_file_content(path):
    with open(path,'w'):
        pass

#create_project_dir('d:/data/python')
#create_data_files('d:/data/python/')
#append_to_file('d:/data/python/queue.txt','I love you')
#delete_file_content('d:/data/python/queue.txt')

#create_project_dir('TheNewBoston')
#create_data_files('TheNewBoston/')

def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

def set_to_file(link,file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file,link)