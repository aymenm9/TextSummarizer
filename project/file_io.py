
def get_str_from_file(file_name:str)->str:
    content = ''
    with open(file_name,'r') as file:
        content = file.read()
    return content

def write_to_file(file_name:str = 'output.txt',content: tuple[str] = [''])-> bool:
    with open(file_name,'w') as file:
        for st in content:
            file.writelines(str(st) + '\n')