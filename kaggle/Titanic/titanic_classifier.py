from sklearn.svm import SVC
from pandas import read_csv
import pandas

def get_model(train_x, train_y):
    clf = SVC()
    classifier = clf.fit(train_x, train_y)
    return classifier

def create_data():
    train_data = read_csv('train.csv', sep=',')
    test_data = read_csv('test.csv', sep=',')

    print test_data.shape
    #train_data = train_data.dropna()
    #test_data = test_data.dropna()
    print test_data.shape

    train_y = train_data['Survived']

    train_class = train_data['Pclass']
    test_class = test_data['Pclass']

    train_x = pandas.concat([train_class, train_data.iloc[:, 4:8]], axis=1)    
    test_x = pandas.concat([test_class, test_data.iloc[:, 3:7]], axis=1)    
    
    print test_x.shape
    model = get_model(train_x, train_y)
    predictions = model.predict(test_x)
    print type(predictions)

    pass_id = test_data.iloc[:, 0]
    pred_df = pandas.DataFrame(predictions)
    #print pass_id.shape
    #print len(predictions)
    #out_data = pandas.Panel({'PassengerId': pass_id, 'Survived': predictions})
    pass_id.reset_index(drop=True, inplace=True)
    pred_df.reset_index(drop=True, inplace=True)
    out_data = pandas.concat([pass_id, pred_df], axis=1, keys=["PassengerId", "Survived"])
    out_data.to_csv('out.csv', sep=',')


def main():
    create_data()

if __name__ == '__main__':
    main()
