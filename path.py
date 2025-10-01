import pathlib

def Path(path:str):
    if(path.startswith("f")):
        return pathlib.Path("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/hub/parrots.png")

    else:
        return pathlib.Path(path)