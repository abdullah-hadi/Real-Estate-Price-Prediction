import json
import pickle
import numpy as np
__location = None
__data_columns = None
__model = None


def price_prediction(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower)

    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location():
    return __location


def load_file():
    print('loading File ....... start')

    global __location
    global __model
    global __data_columns

    with open("./File/columns.json", 'r') as f:

        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open("./File/Bangladesh_home_price.pickle", 'rb') as f:

        __model = pickle.load(f)

    print('loading File ....... done')


if __name__ == '__main__':
    load_file()
    print(get_location())
    print(price_prediction('kaharole', 1000, 2, 3))
