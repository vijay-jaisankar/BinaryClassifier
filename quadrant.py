from sklearn import tree
"""
    As DecisionTreeClassifier takes only real-valued data, let's make some assumptions:
    Q1 = [1]
    Q2 = [2]
    Q3 = [3]
    Q4 = [4]
    Origin = [5]
    X-Axis = [6]
    Y-Axis = [7]

"""

features = [
                [0,0],

                [0.00001,0],
                [-0.00001,0],
                [-1000000000,0],
                [1000000000,0],

                [0,0.00001],
                [0,-0.00001],
                [0,-1000000000],
                [0,1000000000],

                [0.0001,10000000000],
                [0.0001,0.0001],
                [10000000000,0.0001],
                [10000000000,10000000000],

                [-0.0001,10000000000],
                [-0.0001,0.0001],
                [-10000000000,0.0001],
                [-10000000000,10000000000],

                [-0.0001,-10000000000],
                [-0.0001,-0.0001],
                [-10000000000,-0.0001],
                [-10000000000,-10000000000],

                [0.0001,-10000000000],
                [0.0001,-0.0001],
                [10000000000,-0.0001],
                [10000000000,-10000000000]
            ]



labels = [[5],[6],[6],[6],[6],[7],[7],[7],[7],[1],[1],[1],[1],[2],[2],[2],[2],[3],[3],[3],[3],[4],[4],[4],[4]]

classifier = tree.DecisionTreeClassifier()
testClassifier = classifier.fit(features,labels)

x1 = float(input("Enter the x-coordinate: "))
y1 = float(input("Enter the y-coordinate: "))
l = [[]]
l[0].append(x1)
l[0].append(y1)

print(testClassifier.predict(l))



