import logging

def setup_logger(log_file1):
    logging.basicConfig(
        filename=log_file1,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

setup_logger("etl.log")
logging.info("ETL Started")
logging.error("Something failed")