# 2022-Yousaf-Raeesa 


## Introduction

This project provides a framework to analyse and find out which features are used to define roles across networks. Networks are a distinct set of objects represented by nodes and the connection between the objects are represented by edges. Nodes that have the same role usually play the same role in the network and have similar features. For large and complex networks it is difficult to maintain an overview of all nodes and their respective roles. This framework aims to analyse nodes of the same role and their features, in order to determine which dominant features define the roles.


## Installation and Requirements

General requirement are a stable internet connection, Python v3.7 or higher and Python modules that are specified in `requirements.txt`.


## Usage

As of now we extract roles and analyse them using Twitter data stored in `twitter_data.csv`. The user should execute `main.py` in the src folder and load the data locally or remotely by entering their credentials to access the database when required. After executing the main function, features for all nodes in the network will be extracted and pickled in the respective folder. Using these metrics, the framework will compute the mean, standard deviation and variance for each feature across all roles and plot them. The features themselves will also be plotted using scatterplots and histograms. All plots are saved in their respective folder. The framework also can compute a correlation matrix for all roles.
Furthermore, we store political attributes for nodes in `politiker-info.csv`. The distribution of these attributes are also plotted across all roles.


The framework caters specifically to the Twitter data, but can be modified if required:

Features to be extracted can be added or removed in `node_features.py`. It is imperative that `features_dataframe.py`, which lists all nodes and their features, is also changed to match the features extracted. The same goes for the plots in `plot_scatter.py` and `plot_histogram.py`.
Varying political attributes can be changed in `politiker_info.py` and `political_analysis`.py.



