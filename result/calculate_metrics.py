import os
import glob
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, roc_auc_score, matthews_corrcoef

from sklearn.metrics import average_precision_score, f1_score


'''
@author songyu
@time july 15, 2023 9:07 am

input 
    csv file    
y_label,y_pred,output
0.0,2.9047025743890453e-13,0
y_lable is a true label
y_pred is the ouput of model, it's a deciaml from 0 to 1
output is a predictive label, in this prediction, if y_pred >= 0.5, output = 1, else output = 0.
output can be modified.

calculate  following metrics
    'TP': tp, 'TN': tn, 'FP': fp, 'FN': fn,
    'Accuracy': accuracy, 'Sensitivity': sensitivity,
    'Specificity': specificity, 
    'AUROC': auc, 'AUPRC':auprc,
    'F1':f1,'Precision': precision, 'MCC': mcc
    
output
    csv file
metrics listed above of each model sorted by column
'''



# 定义函数来计算指标
def calculate_metrics(file_path):
    # 读取csv文件并计算指标
    df = pd.read_csv(file_path)
    # y_label 0110
    # output 01010
    # y_pred 0.56543 0.54486461
    y_true = df['y_label']
    y_pred = df['output']
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    accuracy = accuracy_score(y_true, y_pred)
    sensitivity = recall_score(y_true, y_pred)
    specificity = tn / (tn + fp)
    auc = roc_auc_score(y_true, df['y_pred'])
    auprc = average_precision_score(y_true, df['y_pred'])
    f1 = f1_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    mcc = matthews_corrcoef(y_true, y_pred)

    # 返回包含指标的字典
    return {'File Name': os.path.basename(file_path), 'TP': tp, 'TN': tn, 'FP': fp, 'FN': fn,
            'Accuracy': accuracy, 'Sensitivity': sensitivity,
            'Specificity': specificity, 'AUROC': auc, 'AUPRC':auprc,'F1':f1,
            'Precision': precision, 'MCC': mcc}

# 创建空列表来存储所有文件的指标
results_list = []

# 遍历文件夹下的所有csv文件，并计算指标
folder_path = 'model_result/umami_result'
for file_path in glob.glob(os.path.join(folder_path, '*.csv')):
    results_list.append(calculate_metrics(file_path))

# 创建DataFrame并保存到CSV文件中
results_df = pd.DataFrame(results_list)
results_df.to_csv(f'{os.path.basename(folder_path)}_1.csv', index=False)
