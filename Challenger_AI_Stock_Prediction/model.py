# coding=utf-8
import xgboost as xgb
import numpy as np

import tuning_xgboost

from sklearn.decomposition import PCA
from xgboost import XGBClassifier
from settings import training_data_path,test_path,prediction_path,model_path
from param_settings import param,num_boost_round,nfold,feature_num,start,end
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold

def loadCSVfile(path,feature_num,flag):
    """
    数据集导入到DMatrix
    :param feature_num:该数据集的特征值数量
    :param flag:True为training_data，False为test_data
    :return:xgb.DMatrix类型数据，里面有分开的label和data
    """
    tmp = np.loadtxt(path, dtype=np.str, delimiter=",")

    data = tmp[1:,1:feature_num + 1].astype(np.float) # 加载数据feature部分（去掉第一列id和第一行标签，变成共计92列数据，88个feature+权重+标签+分组+时间era）

    pca = PCA(n_components=60)
    data = pca.fit_transform(data)

    if(flag):
        era = tmp[:,-1][1:].astype(np.int)  # 加载样本权重部分（去掉表头）
        label = tmp[:,-2][1:].astype(np.int) # 加载类别标签部分（去掉表头）
        weight = tmp[:,-3][1:].astype(np.float)  # 加载样本权重部分（去掉表头）

        code_id = tmp[:,-4][1:].astype(np.float)
        group2 = tmp[:, -5][1:].astype(np.float)
        group1 = tmp[:,-6][1:].astype(np.float)
        res = xgb.DMatrix(data, label = label,missing = 0,weight = weight) #返回xgb.DMattrix类型的数据，用0填充缺失值

        return res
    else:
        return xgb.DMatrix(data, missing = 0) #返回xgb.DMattrix类型的数据，用0填充缺失值

def error(y_hat, y):
    """
    计算评价函数，与题目一致
    :param y_hat:预测值，是prediction的概率的numpy ndarray
    :param y:真实值，是0-1标签的DMatrix
    :return:损失值
    """

    labels = y.get_label() # numpy array类型
    weights = y.get_weight() # numpy array类型
    return 'error', - np.sum(weights * (labels * np.log(y_hat) + (np.ones(y.num_row()) - labels) * np.log(np.ones(y.num_row()) - y_hat)))


def train_and_pre(data_train,data_test):
    """
    训练
    :param data_train:
    :param data_test:
    :return:
    """
    watchlist = [(data_test, 'eval'), (data_train, 'train')]  # 看板，每次迭代都可以在控制台打印出训练集与测试集的损失

    # 1.训练模型
    # obj、feval、early_stopping_rounds、evals_result、verbose_eval、xgb_model
    bst = xgb.train(param, data_train, num_boost_round, evals=watchlist, obj=None, feval=None, maximize=False,
          early_stopping_rounds=max(num_boost_round/5,40), evals_result=None, verbose_eval=True, xgb_model=None, callbacks=None,learning_rates=None)
    # 2.保存模型
    # bst.save_model(model_path)
    # 3.预测
    preds = bst.predict(data_test)
    # 4.保存
    np.savetxt(prediction_path, np.c_[range(start, end + 1), preds], delimiter=',', header='id,proba',comments='', fmt='%f')

def tuning(path):
    """
    交叉验证调参
    :return:
    """
    # 0.软件包网格搜索
    tmp = np.loadtxt(path, dtype=np.str, delimiter=",")

    x = tmp[1:, 1:feature_num + 1].astype(np.float)  # 加载数据feature部分（去掉第一列id和第一行标签，变成共计92列数据，88个feature+权重+标签+分组+时间era）
    y = tmp[:,-2][1:].astype(np.int)
    w = tmp[:,-3][1:].astype(np.float)

    grid1 = {'n_estimators': [50,60]}
    grid2 = {'reg_lambda': [3,5,7,9]}
    grid3 = {'colsample_bylevel': [0.8]}
    grid4 = {'gamma': [0]}
    grid5 = { 'subsample': [0.8]}
    grid6 = { 'min_child_weight': [5]}
    grid7 = {'reg_alpha': [0,3,5]}
    hyperlist_to_try = [grid1, grid2, grid3,grid4,grid5,grid6,grid7]

    gridsearch_params = {
        'cv': 5,  # 已确定
        'scoring':'neg_log_loss','iid':True, 'verbose':1,  # 待确定
        'fit_params':None, 'refit':True, 'n_jobs':1,'pre_dispatch':'2*n_jobs','error_score':'raise','return_train_score':'warn'} # 无用

    booster = xgb.XGBClassifier(
                # 暂时没调
                max_delta_step=0, reg_alpha=0, reg_lambda=1,scale_pos_weight=1,
                # 待调
                gamma=0, max_depth=3, learning_rate=0.1, n_estimators=200, min_child_weight=1,subsample=1, colsample_bytree=1,
                # 无用
                objective="binary:logistic",base_score=0.5,  seed=1, nthread=None,silent=False, missing=None)

    tuned_estimator = tuning_xgboost.grid_search_tuning(x, y, hyperlist_to_try, booster,gridsearch_params=gridsearch_params,verbose=False,plotting=False)
    tuned_parameters = tuned_estimator.get_params()

    for parameter in tuned_parameters:
        print tuned_parameters[parameter],','
    print

    # 1.自己写的网格搜索
    # param_test2b = {
    #     'min_child_weight': [6, 8, 10, 12]
    # }
    # estimator = XGBClassifier(
    #     learning_rate=0.1, n_estimators=1000, max_depth=5,reg_alpha = 0,min_child_weight=2, gamma=0.15, subsample=0.8, colsample_bytree=0.8,n_jobs=1,
        # reg_lambda = 1,max_delta_step=0,silent=False,booster='gbtree',objective='binary:logistic', nthread=None, scale_pos_weight=1, seed=1)

    # gsearch = GridSearchCV(estimator = estimator,param_grid = param_test2b, scoring='logloss',fit_params = None,n_jobs=4,
        # iid=False, refit=True, cv=5, verbose=0,pre_dispatch='2*n_jobs', error_score='raise')

    # gsearch.fit()

    # 2.交叉验证
    # 待调：folds、metrics、obj、feval、verbose_eval
    # l = xgb.cv(param, data_train, num_boost_round=num_boost_round, nfold=nfold, stratified=False, folds=None,
    #            metrics=(), obj=None, feval=None,
    #            maximize=False, early_stopping_rounds=max(50, int(num_boost_round / 10)), fpreproc=None, as_pandas=True,
    #            verbose_eval=None, show_stdv=True, seed=0, callbacks=None)


    # print 'test',sum(l.get('test-logloss-mean',''))/len(l.get('test-logloss-mean','')),'train',sum(l.get('train-logloss-mean',''))/len(l.get('train-logloss-mean',''))

if __name__ == '__main__':
    data_train = loadCSVfile(training_data_path,feature_num,True)
    print data_train.num_col(),data_train.num_row()
    print data_train.get_label()
    print data_train.get_weight()
    data_test = loadCSVfile(test_path,feature_num,True)
    print data_test.num_col(),data_test.num_row()
    print data_test.get_label()
    print data_test.get_weight()
    # for i in range(0,119):
    #     print '----------------------------------',str(i)
    #     tuning(training_data_path[:-4] + str(i) + r'.csv')
    train_and_pre(data_train,data_test)