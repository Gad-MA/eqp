import pathlib

def Path(path:str):
    if(path.startswith("f")):
        pathlib.path("M1001.png")
    else:
        return pathlib.Path(path)