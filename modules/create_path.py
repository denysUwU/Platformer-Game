import os

def create_path (img, folder) :
    path = os.path.abspath(os.path.join(__file__, "..", "..", "assets", folder, f"{img}"))
    return path