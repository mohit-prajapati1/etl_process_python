from utils import setup_logger
from config import LOG_FILE
from etl import extract, transform, load

def main():
    setup_logger(LOG_FILE)

    data = extract()
    clean_data = transform(data)
    load(clean_data)

if __name__ == "__main__":
    main()