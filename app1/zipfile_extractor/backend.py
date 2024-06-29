import zipfile


def unzip_file(filepath, dstn_dir):
    with zipfile.ZipFile(filepath, "r") as f:
        f.extractall(dstn_dir)


if __name__ == "__main__":
    unzip_file(r"/app1/b_examples/result.zip",
               r"C:\Users\Anuj\Desktop\Python\b_examples")
