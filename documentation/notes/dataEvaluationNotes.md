# Data Evaluation Notes

* Visualisation of Mobile App Usage (ID:8714)
* Matthew James O'Hare
* 2255357o
* Professor Matthew Chalmers

These are notes made from my evaluation of the App Tracker data set.  

* Original data had 289,142 rows, with 2 columns each - userID and appID  

* 10,368 users and 45,788 apps  
  * user ids from 2 to 16194  
  * app ids from 1 to 45788  

* Some users have a lot more data than others  
  * user 4942 has used 908 apps  
  * user 6614 has used 532 apps  
  * user 10977 has used 470 apps  
  * there are lots of users that only use 1 app - 745 - with 1007 users that use 3 apps  
  * there are 5,172 users that have used 10 or less apps  

* Range of number of users of an app is massive  
  * top used app used by - 10173 users - this is a utilities app (id: 31336)  
  * second top app used by - 9586 users - this is springboard (id: 3980)  
  * third top app used by - 6452 users - this is a utilities app (id: 3969)  

  * top 10 apps account for 20.4% of rows in the data set (58,917)  
  * top 25 apps account for 32.6% of rows in data set (94,367)  
  * top 50 apps account for 40.6% of rows overall data set (117,483)  

  * there are 29,167 apps (63.7%) that have only been used by 1 user  
  * there are 41,019 apps (89.6%) that have been used by less than 5 users  
  * there are 44,592 apps (97.4%) that have been used by less than 20 users  
  * there are 45,349 apps (99.0%) that have been used by less than 50 users  
  * this means there are only 1% of apps (439) that have been used by more than 50 users  

* There are 89 'apple' apps and 45,699 'other' apps  
* There are 39 'manual genre assignment' apps and 45,749 apps which have a category assigned  

* There are 12,732 apps which have 'NaN' assigned to them.  
* After that, there are 6,351 apps which have id '6014' assigned to them. This is games.  
* After that, there are 3,095 apps which have id '6002' assigned to them. This is utilities.  
* At the bottom, there is 2 apps that have id '1000' assigned to it. This is springboard.  
* Below that there is 1 app that has id '6021' assigned to it. This is newstand.  

* There are 2053 users that were only seen for less than 5 minutes (300 seconds).  
* There are 4600 users that were only seen for less than 1 day (86400 seconds).  

* There are some users that are anomalies, for example: user id 5 has been seen for around 50 days but has only used 7 apps with a total of 22 launches in that time.  

* After removing users who we:  
  * have seen for less than 5 minutes or  
  * have seen for less than 24 hours and used less than 1 app per hour or  
  * have seen for more than 24 hours and used more than 1 app per day.  

There were a few more anomolies:  
  * User 1617  
  * User 6308  
  * User 6384  
  * User 10621  

  * User 1171  
  * User 7466  
  * User 5379  
These are outliers on t-SNE when the number of apps is increased

While using spring models, I found some of the best parameters to be:  
* Number of iterations - best seems to be 50 and 400 depending on size of dataset  
* Kmeans clusters - optimal clusters seems to be 2, 3 or 4 depending on size of dataset  
* t-SNE perplexity - optimal seems to be 50 for large datasets and 30 for anything smaller  
* UMAP min_dist - 0.1, combined with spread, this gave the best visual  
* UMAP spread - 0.75, combined with min_dist this gave the best visual  

t-SNE - 30 perplexity, euclidean (best however 50 is also good), 30 perplexity, seuclidean (other option, its alright)
UMAP - 50 neighbors, seuclidean (best) 50 neighbors , euclidean (other option but still not the best)


