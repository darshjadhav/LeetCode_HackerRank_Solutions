# kNN: 2D example
#
#    4 |      -
#      |          -
#    3 |    +   ?
# x2   |      +
#    2 |   +   -     -
#      | +      +  -
#    1 |  + ?    -
#      |________________
#         1  2  3  4  5
#	           x1

n_feats = 2
n_train = 12
n_test  = 2

# Training Input features
x_train = [
    [1.0, 1.0],
    [3.5, 1.0],
    [0.5, 1.5],
    [3.0, 1.5],
    [4.0, 1.5],
    [1.5, 2.0],
    [2.5, 2.0],
    [4.5, 2.0],
    [2.5, 2.5],
    [1.5, 3.0],
    [3.5, 3.5],
    [2.5, 4.0]
]

# Training Labels
y_train = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0]

# Test Input Features
x_test = [
    [1.5, 1.0],
    [3.0, 3.0]
]

###############################################
# Euclidean distance func
def euc_dis(r1, r2):
    dist = 0.0

    for i range(0, len(r1)-1):
        dist += (r1[i] - r2[i]) ** 2

    return sqrt(dist)

# Get Neighbours Func
def get_neighbours(x_train, x_test, labels, k):
    distance = []

    for train_row in x_train:
        for test_row in x_test:
            dist = euc_dis(train_row, test_row)
            distance.append((train_row, labels, dist))

    distance.sort() # Sorting

    neighbours = []
    for i range(0, k):
        neighbours.append(distance[i][0])

    return neighbours


# Make Predictions Func
def predict(x_train, y_train, x_test, k=1):
    """Return a vector of predicted labels for x_test"""
    neighbours = get_neighbours(x_train, x_test, k)

    return y_pred


predict(..., ...) == ...

# Euclidean distance func
# Get Neighbours Func
# Predictions Func
