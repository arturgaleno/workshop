import numpy as np

def parser(dataset):
    users = np.unique(dataset['user'])
    items = np.unique(dataset['item'])

    # create visualization matrix.
    ratings = np.zeros((len(users), len(items)))
    for i, user in enumerate(dataset["user"]):
        item = dataset["item"][i]
        ratings[users.tolist().index(user), items.tolist().index(item)] = 1

    return ratings, users, items

def predict(ratings, kind='user', epsilon=1e-9):
    if (kind == 'user'):
        sim = ratings.dot(ratings.T) + epsilon
    elif kind == 'item':
        sim = ratings.T.dot(ratings) + epsilon

    # calculate norms matrix.
    norms = np.array([np.sqrt(np.diagonal(sim))])
    return (sim / norms / norms.T)

def getTopItems(predictor, mapper, idx, k=15):
    return [mapper[x] for x in np.argsort(predictor[idx,:])[:-k-1:-1]]
