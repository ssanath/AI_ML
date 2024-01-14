#Decision Tree
import pandas as pd
import math
data = pd.read_csv("dt3.csv")
class TreeNode:
    def __init__(self, label=None, attribute=None, branches=None):
        self.label = label
        self.attribute = attribute
        self.branches = branches if branches is not None else {}

def best_att(ex, target_att, att, Ent, tot):
    gains = []
    for a in att:
        ent = 0
        A_val = ex[a].unique().tolist()
        for val in A_val:
            count_val = ex[a].value_counts()[val]
            No_pos = ex[(ex[a] == val) & (ex[target_att] == 'Yes')].shape[0]
            No_neg = ex[(ex[a] == val) & (ex[target_att] == 'No')].shape[0]

            if count_val != 0 and No_pos != 0 and No_neg != 0:
                ent_val = -((No_pos / count_val) * math.log2(No_pos / count_val)) - (
                            (No_neg / count_val) * math.log2(No_neg / count_val))
                ent += (count_val / tot) * ent_val
        gains.append(Ent - ent)
    return gains

def Gain(ex, target_att, att):
    No_pos = ex[target_att].value_counts().get('Yes', 0)
    No_neg = ex[target_att].value_counts().get('No', 0)
    tot = No_pos + No_neg
    Ent = -((No_pos / tot) * math.log2(No_pos / tot)) - ((No_neg / tot) * math.log2(No_neg / tot))
    gains = best_att(ex, target_att, att, Ent, tot)
    max_gain = max(gains)
    return att[gains.index(max_gain)]

def DecisionTree(ex, target_att, att):
    root = TreeNode()
    if (ex[target_att] == "Yes").all():
        root.label = "Yes"
        return root
    elif (ex[target_att] == "No").all():
        root.label = "No"
        return root
    elif not att:
        most_common = ex[target_att].value_counts().idxmax()
        root.label = most_common
        return root
    else:
        A = Gain(ex, target_att, att)
        root.attribute = A
        A_val = ex[A].unique().tolist()
        for val in A_val:
            root.branches[val] = TreeNode()
            examples_subset = ex[ex[A] == val]
            if examples_subset.empty:
                most_common = ex[target_att].value_counts().idxmax()
                root.branches[val].label = most_common
            else:
                root.branches[val] = DecisionTree(examples_subset, target_att, list(set(att) - set([A])))
    return root

target_attribute = "Stolen"
attributes = [attr for attr in data.columns if attr != target_attribute]
tree_root = DecisionTree(data, target_attribute, attributes)
def print_tree(node, depth=0):
    if node.label is not None:
        print('  ' * depth + f'Label: {node.label}')
    else:
        print('  ' * depth + f'Attribute: {node.attribute}')
        for branch, subtree in node.branches.items():
            print('  ' * (depth + 1) + f'Value: {branch}')
            print_tree(subtree, depth + 2)

print_tree(tree_root)
