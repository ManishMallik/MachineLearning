# Machine Learning Assignment 3
We utilized Google Colab for this assignment. Attached below is the link to our Colab notebook containing the code for the programming part of assignment 3:
[https://colab.research.google.com/drive/1gD7VO4gLuY_YWOXU8y7EjGi-SJIUsttR?usp=sharing](https://colab.research.google.com/drive/1xjQjf0YI-fl8CioRtmYxGdbrTRvdqB4D?usp=sharing)

There are a total of 2 different coding cells in this notebook. Run each cell in order from top to bottom. The first cell will contain the whole main code, which uses a K-Means clustering algorithm, coded from scratch, to cluster tweets from a text file that we choose from the dataset. It will also print out the sum of squared error (SSE) for each k-cluster and the size of each cluster within those k clusters. The 2nd cell will generate a graph displaying the trend between the number of clusters (k) and the SSE.

This program uses the "usnewshealth.txt" file from the following dataset: [https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter](https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter). We have a preprocess method that will process all the tweets before clustering them.

The libraries we used are:
- re for modifying tweets, such as removing the timestamp, ID, #, any word that starts with @, and any URLs
- numpy as np for any math operations and generating random numbers
- requests, zipfile, and BytesIO to access the necessary zipfile and read the text file we wanted to read
- matplotlib.pyplot for plotting our graph of SSE vs. k clusters
- sys for exiting the program if an exception is going to be thrown when trying to read the tweets from the text file

Our report of results in a tabular format, along with the summary of our results and the graph, are all in our assignment 3 report PDF file.

Important note: we retrieved the dataset by using this URL in our code: [https://archive.ics.uci.edu/static/public/438/health+news+in+twitter.zip](https://archive.ics.uci.edu/static/public/438/health+news+in+twitter.zip)
