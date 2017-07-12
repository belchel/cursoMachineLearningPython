from sklearn import datasets
from sklearn.neural_network  import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


iris = datasets.load_iris()

X, y =iris.data, iris.target

mlp = MLPClassifier(solver='adam', alpha = 0.0001, hidden_layer_sizes = (5,), random_state=1,
                    learning_rate='constant', learning_rate_init = 0.01, max_iter=500,
                    activation='logistic', momentum=0.9, verbose=True, tol=0.0001)

X_treino, X_teste, y_treino, y_teste = train_test_split(X,y,test_size = 0.3, random_state=1)

mlp.fit(X_treino,y_treino)

saidas = mlp.predict(X_teste)

print('Saida : ', saidas)

print('Desejado: ', y_teste)

print('Score: ', mlp.score(X_teste,y_teste))


print(confusion_matrix(y_teste, saidas))

print(classification_report(y_teste, saidas))
