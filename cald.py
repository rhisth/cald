from importlib.util import spec_from_file_location as sffl
from importlib.util import module_from_spec as mfs
from os import listdir
from config import infpath

def read(path):
    with open(path, encoding="UTF-8") as file:
        return file.read()

def getmodule(path):
    spec = sffl("", path)
    module = mfs(spec)
    spec.loader.exec_module(module)
    return module

def getday(id, year):
    basepath = f"{infpath}/{id}/{id}"
    result = getmodule(f"{basepath}.py")
    return (read(f"{basepath}.inf"), result.value(year))

def getdays(year):
    return [getday(day, year) for day in listdir(infpath)]