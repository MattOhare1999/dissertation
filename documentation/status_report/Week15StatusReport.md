# Weel 15 Status Report

As we spoke about at last week's meeting, I attempted to use basic clustering algorithms on the data to check if there were any clusters to begin with. However due to the high dimension of the data, these basic algorithms were not very effective and clustered all data points together. As a result, I looked at UMAP to improve this clustering. After careful consideration and testing regarding parameters, UMAP found clusters (better than those of t-SNE) and using in built features, I have been able to create an interactive graph which has allowed analysis to be carried out on it. I can show these visualisations and results at the meeting.

I have also exported more data sets from my Google Colab notebook (where the data analysis was carried out) to take into account more apps (top 300, 500, 1000, 10000) when creating these visualisations. I have found that although run times are longer (exact times have not been noted yet, this will be done this coming week), the visualisations themselves are relatively similar.

