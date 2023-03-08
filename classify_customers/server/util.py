import json
import pickle

__model=None
__data_columns=None
__target=None

def estimation(sex, married, age, graduation, profession, experience, score, family, var1):
    attrs = [0]*len(__data_columns)
    attrs[0] = sexs
    attrs[1] = married
    attrs[2] = age
    attrs[3] = graduation
    attrs[4] = profession
    attrs[5] = experience
    attrs[6] = score
    attrs[7] = family
    attrs[8] = var1
    print(attrs)
    pred = __model.predict([attrs])
    string = ''
    
    if pred == 0:
        string = 'Occasional customer'
    elif pred == 1:
        string = 'Discount spender'
    elif pred == 2:
        string = 'Spender'
    else:
        string = 'Lavish spender'
        
    return string

def load_saved_artifacts():
    global __model
    global __data_columns
    global __target

    with open("server/artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
    if __model is None:
        with open("server/artifacts/customers.pickle",'rb') as f:
            __model=pickle.load(f)
        print('loading saved artifacts...done')

    with open("server/artifacts/targets.josn",'r') as f:
        __target=json.load(f)['target_names']

if __name__=='__main__':
    load_saved_artifacts()
    print(estimation(0, 1, 47, 1, 0, 2, 0, 3, 5))
    print(estimation(1, 1, 47, 1, 1, 2, 2, 3, 5))
    print(__model)