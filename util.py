import json
import pickle
import numpy as np
import os

__Category = None
__data_columns = None
__model = None


def get_Category():

    return __Category


def load_saved_artifacts():
    print("loading saved artifcats... start")
    global __data_columns
    global __Category
    with open(r"C:\Users\Prakruthi\OneDrive\Desktop\Data_Science\Project_Folder\Server\artifacts\columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __Category = __data_columns[5:]


    global __model
    with open(r"C:\Users\Prakruthi\OneDrive\Desktop\Data_Science\Project_Folder\Server\artifacts\Sales_Optimization.pickel", 'rb') as f:
        __model = pickle.load(f)
    print("loading artidacts is done")

    
def get_predict_revenue(Category,Income,Price,Discount_Percent,Units_Sold,Cost):
    try:
        cat_index = __data_columns.index(Category.lower()) # giving index to the hard coded category value
    except: 
        cat_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = Income
    x[1] = Price
    x[2] = Discount_Percent
    x[3] = Units_Sold
    x[4] = Cost
    if cat_index >= 0:
        x[cat_index] = 1
    return __model.predict([x])[0]


if __name__ == '__main__':

    load_saved_artifacts()
    print(get_Category())
    print(get_predict_revenue('Beauty',78145,20.21,10,18,127.32))
    #print(get_predict_revenue('Apparel',78145,61.69,20,18,500.69))
    print(get_predict_revenue('Apparel',61679,61.69,18,20,499.69))