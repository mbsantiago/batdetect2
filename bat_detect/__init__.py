import os

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(PACKAGE_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "Net2DFast_UK_same.pth.tar")

__all__ = [
    "MODEL_PATH",
]
