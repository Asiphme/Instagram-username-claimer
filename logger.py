import logging

def setup_logger():
    logger = logging.getLogger("claimer")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler("claimer.log")
    eh = logging.FileHandler("error.log")
    ch = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    eh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.addHandler(eh)

    return logger

logger = setup_logger()
