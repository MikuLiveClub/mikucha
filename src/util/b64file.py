import base64


def make_file_from_b64(path: str, b64: str):
    with open(path, "wb") as f:
        f.write(base64.b64decode(b64))
