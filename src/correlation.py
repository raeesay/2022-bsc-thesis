from functools import reduce
import features_dataframe as features

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_pickle('./pickles/df_merged.pickle')

def variance(df):
    df_list = list()

    for i in range(8):
        # split dataframe into dataframes with nodes of the same role
        temp = df[df['role'] == 'role_' + str(i)]
        # calculate the variance of all features
        obj = temp.var()
        obj1 = obj.to_frame()
        obj1.columns = ['role_' + str(i)]
        obj1 = obj1.reset_index()
        # we have dataframes where the rows correspond to the variance of features
        # and the column is the role for which we calculated the variance
        df_list.append(obj1)

    # merge the dataframes so there are columns for each rol
    result = reduce(lambda df1, df2: pd.merge(df1, df2, on='index'), df_list)
    result = result.set_index('index')
    # compute correlation matrix (Pearson by default)
    #corrFinal = result.corr()
   # print('Pearson correlation matrix:' + corrFinal)

    # switch rows and columns, so that the colums are now the features
    final = result.transpose()

    # for each features plot the variance for all roles
    for column in final:
        plt.title('Variance of ' + column + ' of all roles', fontsize=20)
        plt.xlabel('roles', fontsize=15)
        plt.ylabel(column, fontsize=15)

        plt.bar(final.index, final[column])
        plt.savefig('./plots/roles/variance/' + column)
        plt.close()


def mean(df):
    df_list = list()

    for i in range(8):
        # split dataframe into dataframes with nodes of the same role
        temp = df[df['role'] == 'role_' + str(i)]
        # calculate the mean of all features
        obj = temp.mean()
        obj1 = obj.to_frame()
        obj1.columns = ['role_' + str(i)]
        obj1 = obj1.reset_index()
        # we have dataframes where the rows correspond to the mean of features
        # and the column is the role for which we calculated the mean
        df_list.append(obj1)

    # merge the dataframes so there are columns for each rol
    result = reduce(lambda df1, df2: pd.merge(df1, df2, on='index'), df_list)
    result = result.set_index('index')
    # compute correlation matrix (Pearson by default)
    #corrFinal = result.corr()
    #print('Pearson correlation matrix:' + corrFinal)

    # switch rows and columns, so that the colums are now the features
    final = result.transpose()

    # for each features plot the mean for all roles
    for column in final:
        plt.title('Mean of ' + column + ' of all roles', fontsize=20)
        plt.xlabel('roles', fontsize=15)
        plt.ylabel(column, fontsize=15)

        plt.bar(final.index, final[column])
        plt.savefig('./plots/roles/mean/' + column)
        plt.close()


def std_dev(df):
    df_list = list()

    for i in range(8):
        # split dataframe into dataframes with nodes of the same role
        temp = df[df['role'] == 'role_' + str(i)]
        # calculate the standard deviation of all features
        obj = temp.std()
        obj1 = obj.to_frame()
        obj1.columns = ['role_' + str(i)]
        obj1 = obj1.reset_index()
        # we have dataframes where the rows correspond to the standard deviation of features
        # and the column is the role for which we calculated the standard deviation
        df_list.append(obj1)

    # merge the dataframes so there are columns for each rol
    result = reduce(lambda df1, df2: pd.merge(df1, df2, on='index'), df_list)
    result = result.set_index('index')
    # compute correlation matrix (Pearson by default)
    #corrFinal = result.corr()
    #print('Pearson correlation matrix:' + corrFinal)

    # switch rows and columns, so that the colums are now the features
    final = result.transpose()

    # for each features plot the standard deviation for all roles
    for column in final:
        plt.title('Standard deviation of ' + column + ' of all roles', fontsize=20)
        plt.xlabel('roles', fontsize=15)
        plt.ylabel(column, fontsize=15)

        plt.bar(final.index, final[column])
        plt.savefig('./plots/roles/std/' + column)
        plt.close()

variance(df)
mean(df)
std_dev(df)