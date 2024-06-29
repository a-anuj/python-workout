import zipfile
import pathlib


def make_archive(filepaths, dstn_dir):
    dstn_path = pathlib.Path(dstn_dir, "result.zip")
    with zipfile.ZipFile(dstn_path, "w") as f:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            f.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    filepaths = ["file_compress.py", "make_archive_function.py"]
    dstn_dir = ""
    make_archive(filepaths, dstn_dir)
