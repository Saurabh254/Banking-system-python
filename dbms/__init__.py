import logging
logging.basicConfig(filename='example.log', filemode='a+', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

__all__ = [logging]