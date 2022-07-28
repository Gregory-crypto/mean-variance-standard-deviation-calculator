import numpy as np

test = dict()

def calculate(list):
    calculations = {
        'mean': [[], [], 0],
        'variance': [[], [], 0],
        'standard deviation': [[], [], 0],
        'max': [[], [], 0],
        'min': [[], [], 0],
        'sum': [[], [], 0]
        }

    if len(list) <9:
        raise ValueError('List must contain nine numbers.')
    
    array = np.array(list).reshape(3, 3)
    
    
    for j in range(3):
            calculations['mean'][1].append(array[j, ].mean())
            calculations['variance'][1].append(array[j, ].var())
            calculations['standard deviation'][1].append(array[j, ].std())
            calculations['max'][1].append(array[j, ].max())
            calculations['min'][1].append(array[j, ].min())
            calculations['sum'][1].append(array[j, ].sum())
            calculations['mean'][0].append(array[:, j].mean())
            calculations['variance'][0].append(array[:, j].var())
            calculations['standard deviation'][0].append(array[:, j].std())
            calculations['max'][0].append(array[:, j].max())
            calculations['min'][0].append(array[:, j].min())
            calculations['sum'][0].append(array[:, j].sum())

    calculations['mean'][2] = array.mean()
    calculations['variance'][2] = array.var()
    calculations['standard deviation'][2] = array.std()
    calculations['max'][2] = array.max()
    calculations['min'][2] = array.min()
    calculations['sum'][2] = array.sum()


    test = calculations
    return calculations
