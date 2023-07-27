from utils.utils import read_file


def main():
    operations = read_file("./data/operations.json")
    print(operations)


if __name__ == "__main__":
    main()
