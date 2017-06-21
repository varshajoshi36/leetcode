from sklearn.svm import SVC
from pandas import read_csv
import pandas

def get_model(train_x, train_y):
    clf = SVC()
    classifier = clf.fit(train_x, train_y)
    return classifier

def predict():
    train_data = read_csv('data/train.csv', sep=',')
    test_data = read_csv('data/test.csv', sep=',')

    train_y = train_data['Survived']

    train_class = train_data['Pclass']
    test_class = test_data['Pclass']

    train_x = pandas.concat([train_class, train_data.iloc[:, 4:8]], axis=1)    
    test_x = pandas.concat([test_class, test_data.iloc[:, 3:7]], axis=1)    
    
    model = get_model(train_x, train_y)
    predictions = model.predict(test_x)

    pass_id = test_data.iloc[:, 0]
    pred_df = pandas.DataFrame(predictions)
    pass_id.reset_index(drop=True, inplace=True)
    pred_df.reset_index(drop=True, inplace=True)
    out_data = pandas.concat([pass_id, pred_df], axis=1, keys=["PassengerId", "Survived"])
    out_data.to_csv('data/out.csv', sep=',')


def main():
    predict()

if __name__ == '__main__':
    main()
