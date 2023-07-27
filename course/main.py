from utils.utils import read_file, transfer_date


# import datetime


def main():
    path = "./data/operations.json"
    operations = read_file(path)
    date_ = transfer_date(operations)

    print(date_)


if __name__ == "__main__":
    main()
