import pathlib

def get_root():
    root = pathlib.PurePath(
        input("What's the full path where you'd like the project? ")
    )
    if not root.is_absolute():
        return get_root()
    return root


def main():
    project_root = get_root()
    project_name = None
    while not project_name:
        project_name = input("What's the full name for the project? ").strip()
    print("Creatin {} in {}".format(project_name, project_root))


if __name__ == '__main__'
main()
