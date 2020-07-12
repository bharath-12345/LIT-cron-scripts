import yaml
from constants import *


if __name__ == "__main__":
    with open(CONF_FILE) as fp:
        conf = yaml.load(fp, Loader=yaml.FullLoader)

    # connect to the db
    #con = db.connect(DB_URL)

    for i in range(1000):
        print(i)
