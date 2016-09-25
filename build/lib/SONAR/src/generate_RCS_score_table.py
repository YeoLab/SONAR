import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.cross_validation import StratifiedKFold

def get_scores_for_allprot_via_cvTesting_oversampled(Xy_df, ycol, Score_df, n_folds=10, repeats=10):
    for run in range(repeats):
        y=np.array(Xy_df[ycol])
        cv=StratifiedKFold(y, n_folds)
        for i, (train, test) in enumerate(cv):
            train_set=Xy_df.iloc[train,:]
            Positive_train_set=train_set[train_set[ycol]==1]
            Negative_train_set=train_set[train_set[ycol]==0]
            folds=int(round(len(Negative_train_set)*1.0/len(Positive_train_set)))
            Positive_train_set_oversampled=pd.concat([Positive_train_set]*folds)
            new_train_set=pd.concat([Negative_train_set,Positive_train_set_oversampled])
            X_train=np.array(new_train_set.iloc[:,:-1])
            y_train=np.array(new_train_set.iloc[:,-1])
            X_test=np.array(Xy_df.iloc[test,:-1])
            y_test=np.array(Xy_df.iloc[test,-1])
            Xy_df_test_prot_names=list(Xy_df.iloc[test].index)
            clf_SVM=svm.SVC(kernel='rbf', probability=False, class_weight={1:2.0}) #"probability=False": use confidence score to describe each sample
            scores=clf_SVM.fit(X_train, y_train).decision_function(X_test)
            score_list=zip(Xy_df_test_prot_names, scores)

            for prot_name, score in score_list:
                Score_df.loc[prot_name, ['sum_of_scores','counts']]=(Score_df.loc[prot_name, 'sum_of_scores']+score, Score_df.loc[prot_name, 'counts']+1)

                
    avg_Score_df=pd.DataFrame(index=Score_df.index)
    avg_Score_df['score']=Score_df['sum_of_scores']*1.0/Score_df['counts']
    avg_Score_df['RBP_flag']=Score_df['RBP_flag']
    
    return avg_Score_df

if __name__=='__main__':
    Xy_df=PPI_feature_table[['primary_RBP_ratio', 'secondary_RBP_ratio', 'tertiary_RBP_ratio', 'RBP_flag']]
    Score_df=pd.DataFrame(index=Xy_df.index)
    Score_df['sum_of_scores']=0
    Score_df['counts']=0
    Score_df['RBP_flag']=Xy_df['RBP_flag']
    avg_Score_df=get_scores_for_allprot_via_cvTesting_oversampled(Xy_df, 'RBP_flag', Score_df)
    avg_Score_df.to_csv('./SONAR_score_table.txt', sep='\t', index=True)
