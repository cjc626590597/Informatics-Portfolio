from math import log
import pandas as pd


class TreeNode():
    def __init__(self, feature_name=None, node_val=None, child=None):
        """
        Treenode for decisionTree
        :param feature_name: if this node is classification node, it will be not None to record feature used to classify
        :param node_val: if this node is leaf, it will be not None to record label
        :param child: child is used to record feature value and subtree
        """
        self.feature_name = feature_name
        self.node_val = node_val
        self.child = child


def retrieveTrainingData():
    """
    This is used to retrieve training data from database
    :return:
    [0]List: data used to train (dataSet[-1] is label)
    [1]List: features used to classify
    """
    file = r'data/trainingData.xls'
    data = pd.read_excel(file, sheet_name=0)
    data.drop(data.columns[[0, -3]], axis=1, inplace=True)
    data.fillna('', inplace=True)
    features = list(data)
    features.pop(-1)
    data = data.values.tolist()
    dataSet = []
    for item in data:
        dataSet.append(item)
    return dataSet, features


def countLabels(dataSet):
    """
    Used to count the number of times that each label appears
    :param dataSet: training dataset
    :return:
    'dict': The number of times that each label appears
    """
    labels = {}
    for entry in dataSet:
        label = entry[-1]
        if label not in labels.keys():
            labels[label] = 0
        labels[label] += 1
    return labels


def calculateEntropy(dataSet):
    """
    Calculate entropy for this dataset
    :param dataSet: dataset used to calculate entropy
    :return:
    'float': entropy for this dataset
    """
    # labels of this dataSet
    labels = countLabels(dataSet)
    # total number of entry in dataset
    total = len(dataSet)
    # entropy: float
    Entropy = 0.0
    for i in labels:
        # p is possibility of i
        p = float(labels[i]) / total
        Entropy -= p * log(p, 2)
    return Entropy


def mostPossibleLabel(dataSet):
    """
    Get the most possible label
    :param dataSet: dataset used to get label
    :return:
    'str': a label in leafnode used to classify
    """
    labelCount = countLabels(dataSet)
    labelCount = sorted(labelCount.items(), key=lambda x: x[1])
    return TreeNode(node_val=labelCount[-1][0])


def getSubDiscreteDataSet(dataSet, index, value):
    """
    This is used for discrete data
    After using the feature, save data with specific value of this feature and delete this feature from dataset
    :param dataSet: dataset that needs to delete feature
    :param index: the index of feature in dataset(label)
    :param value: the value of feature
    :return:
    'List': processed dataset
    """
    subDataSet = []
    for entry in dataSet:
        if entry[index] == value:
            subSet = entry[:index]
            subSet.extend(entry[index + 1:])
            subDataSet.append(subSet)
    return subDataSet


def getSubContinuousDataSet(dataSet, index, value, direction):
    """
    This is used for continuous data
    split dataset into two part according value and feature and delete this feature
    :param dataSet: dataset that needs to be split
    :param index: the index of feature in dataset(label)
    :param value: dividing line
    :param direction: True for right, False for left
    :return:
    'List': processed dataset
    """
    subDataSet = []
    for entry in dataSet:
        if direction == False:
            if entry[index] <= value:
                subSet = entry[:index]
                subSet.extend(entry[index + 1:])
                subDataSet.append(subSet)
        if direction == True:
            if entry[index] > value:
                subSet = entry[:index]
                subSet.extend(entry[index + 1:])
                subDataSet.append(subSet)
    return subDataSet


def calculateGainRatioForDiscreteDataSet(dataSet, empiricalEntropy, featureValues, index):
    featureValuesSet = set(featureValues)
    gainRatio = 0.0
    # entropy = Sigma[ featuresLength/totalLength * log2(featuresLength/totalLength) ]
    entropy = 0.0
    # empiricalConditionalEntropy = Sigma[featuresLength/totalLength * Sigma[labelLength/featuresLength * log2(labelLength/featuresLength)] ]
    empiricalConditionalEntropy = 0.0
    # calculate gainRatio
    for value in featureValuesSet:
        # get dataset for specific value
        subDataSet = []
        for entry in dataSet:
            if entry[index] == value:
                subDataSet.append(entry)
        # this is used to calculate entropy
        p = float(len(subDataSet)) / len(dataSet)
        # all are the same value
        if p == 1.0:
            optimalFeatureIndex = index
            optimalFeatureValue = value
            return +float('inf'), optimalFeatureIndex, optimalFeatureValue
        # not one is this value
        if p == 0.0:
            continue
        entropy -= p * log(p, 2)
        empiricalConditionalEntropy += p * calculateEntropy(subDataSet)
    gainRatio = float(empiricalEntropy - empiricalConditionalEntropy) / entropy
    return gainRatio, 0, 0


def calculateGainRatioForContinuousDataSet(dataSet, empiricalEntropy, value, index):
    # empiricalConditionalEntropy = Sigma[featuresLength/totalLength * Sigma[labelLength/featuresLength * log2(labelLength/featuresLength)] ]
    empiricalConditionalEntropy = 0.0
    gainRatio = 0.0
    # entropy = Sigma[ featuresLength/totalLength * log2(featuresLength/totalLength) ]
    entropy = 0.0
    rightDataSet = getSubContinuousDataSet(dataSet, index, value, True)
    # if all values in this feature are same
    if len(rightDataSet) == 0:
        optimalFeatureIndex = index
        optimalFeatureValue = value
        return +float('inf'), optimalFeatureIndex, optimalFeatureValue
    leftDataSet = getSubContinuousDataSet(dataSet, index, value, False)
    # this is used to calculate entropy
    p0 = float(len(rightDataSet)) / len(dataSet)
    empiricalConditionalEntropy += p0 * calculateEntropy(rightDataSet)
    # this is used to calculate entropy
    p1 = float(len(leftDataSet)) / len(dataSet)
    empiricalConditionalEntropy += p1 * calculateEntropy(leftDataSet)
    entropy -= p0 * log(p0, 2)
    entropy -= p1 * log(p1, 2)
    gainRatio = float(empiricalEntropy - empiricalConditionalEntropy) / entropy
    return gainRatio, 0, 0


def calculateOptimalFeature(dataSet, features):
    """
    Calculate optimal feature for classification
    :param dataSet: dataset used to calculate entropy to get optimal feature
    :param features: features of this dataset
    :return:
    'str': name of best feature
    'float/int/str': best value for classification
    """
    empiricalEntropy = calculateEntropy(dataSet)
    optimalFeatureIndex = 0
    baseGainRatio = -float('inf')
    # total number of features
    total = len(dataSet[0]) - 1
    # for continuous data, use dict to record its optimal value
    optimalFeatureDict = {}
    # go through all features
    for i in range(total):
        # values of this feature
        featureValues = [entry[i] for entry in dataSet]
        # if feature is string
        if type(featureValues[0]) == str:
            data = calculateGainRatioForDiscreteDataSet(dataSet, empiricalEntropy, featureValues, i)
            gainRatio = data[0]
            # possibility is 1.0
            if gainRatio == +float('inf'):
                return data[1], data[2]
            if gainRatio > baseGainRatio:
                optimalFeatureIndex = i
                baseGainRatio = gainRatio
        # if feature is number
        else:
            sortedValues = sorted(featureValues)
            values = []
            bestValueIndex = 0
            for j in range(len(featureValues) - 1):
                values.append((sortedValues[j] + sortedValues[j + 1]) / 2.0)
            for j in range(len(values)):
                # every value has one gainRatio
                data = calculateGainRatioForContinuousDataSet(dataSet, empiricalEntropy, values[j], i)
                gainRatio = data[0]
                # possibility is 1.0
                if gainRatio == +float('inf'):
                    return data[1], data[2]
                if gainRatio > baseGainRatio:
                    baseGainRatio = gainRatio
                    bestValueIndex = j
                    optimalFeatureIndex = i
            # different number features have different optimal value
            optimalFeatureDict[features[i]] = values[bestValueIndex]
    if type(dataSet[0][optimalFeatureIndex]) == str:
        optimalFeatureValue = features[optimalFeatureIndex]
    else:
        optimalFeatureValue = optimalFeatureDict[features[optimalFeatureIndex]]
    return optimalFeatureIndex, optimalFeatureValue


def getSubFeatures(index, features):
    """
    delete one feature from features
    :param index: index of feature which needs to be delete
    :param features: features list
    :return:
    'List': processed features
    """
    subFeatures = features[:index]
    subFeatures.extend(features[index + 1:])
    return subFeatures


def createDecisionTree(dataSet, features):
    """
    create decisionTree according to C4.5 algorithm
    :param baseDataSet: whole dataset
    :param dataSet: dataset used to train
    :param features: features of this dataset
    :return:
    'treeNode': node for dataset
    """
    # delete returned Tree later
    labels = [entry[-1] for entry in dataSet]
    if len(set(labels)) == 1:
        return TreeNode(node_val=labels[0])
    if len(dataSet) == 0:
        return TreeNode()
    if len(dataSet[0]) == 1:
        return mostPossibleLabel(dataSet)
    # calculate best feature
    optimalFeatureIndex, optimalFeatureValue = calculateOptimalFeature(dataSet, features)
    # create classification node if it is not leaf
    node = TreeNode(feature_name=features[optimalFeatureIndex])
    # processed features
    subFeatures = getSubFeatures(optimalFeatureIndex, features)
    # if feature is string
    if type(dataSet[0][optimalFeatureIndex]) == str:
        values = [entry[optimalFeatureIndex] for entry in dataSet]
        ValuesSet = set(values)
        # use dict to store children for this node to go to next feature
        children = dict()
        for value in ValuesSet:
            subDataSet = getSubDiscreteDataSet(dataSet, optimalFeatureIndex, value)
            children[value] = createDecisionTree(subDataSet, subFeatures)
        node.child = children
    # if feature is number
    else:
        # use value to split dataset
        value = optimalFeatureValue
        rightDataSet = getSubContinuousDataSet(dataSet, optimalFeatureIndex, value, True)
        leftDataSet = getSubContinuousDataSet(dataSet, optimalFeatureIndex, value, False)
        # use dict to store children for this node to go to next feature
        children = dict()
        children['>' + str(value)] = createDecisionTree(rightDataSet, subFeatures)
        children['<=' + str(value)] = createDecisionTree(leftDataSet, subFeatures)
        node.child = children
    return node


def predict(root, x, features):
    """
    Predict label of x via decision tree (root)
    :param root: root of decision tree
    :param x: data that needed to be predict
    :param features: feature of x
    :return:
    'str': predicted label of x
    """
    if root is None:
        return None

    # leaf node
    if root.node_val is not None:
        return root.node_val

    if root.feature_name is None:
        return None
    index = features.index(root.feature_name)
    xValue = x[index]
    for key, node in root.child.items():
        if type(xValue) == str:
            if key == xValue:
                # go to next node
                return predict(node, x, features)
        else:
            if key[0] == '>':
                value = key.replace('>', '')
                value = float(value)
                if xValue > value:
                    # go to next greater node
                    return predict(node, x, features)
            if key[0] == '<':
                value = key.replace('<=', '')
                value = float(value)
                if xValue <= value:
                    # go to next smaller node
                    return predict(node, x, features)


def traverseTree(root):
    """
    traverse the decision tree from root
    :param root: root of a tree
    :return: No
    """
    if root.node_val is None:
        print('Node:' + str(root.feature_name) + str(root.child))
    else:
        print('Leaf:' + str(root.feature_name) + str(root.node_val))
    if root.child is not None:
        for k, v in root.child.items():
            print(k)
            traverseTree(v)


if __name__ == '__main__':
    _dataSet, _features = retrieveTrainingData()
    _root = createDecisionTree(_dataSet, _features)
    #traverseTree(_root)
    file = r'data/testData.xls'
    data = pd.read_excel(file, sheet_name=0)
    correctResult = []
    tmp = data.values.tolist()
    for item in tmp:
        correctResult.append(item[-1])
    print(correctResult)
    data.drop(data.columns[[0, -3, -1]], axis=1, inplace=True)
    data.fillna('', inplace=True)
    data = data.values.tolist()
    total = len(data)
    correct = 0.0
    i = 0
    for item in data:
        result = predict(_root, item, _features)
        print(result)
        if result == correctResult[i]:
            correct += 1
        i += 1
    print(100 * correct/total)
