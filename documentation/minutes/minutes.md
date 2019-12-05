# Meeting Minutes

* Visualisation of Mobile App Usage (ID:8714)
* Matthew James O'Hare
* 2255357o
* Professor Matthew Chalmers

Minutes from meetings held with supervisor.

## Meeting 1 - 25th September 2019, 13:30-14:00

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

We discussed the background of the project, where the data to be used originated and how it came to be. Matthew said I should receive this data soon, once it has been anonymised, and in the mean time said he would email me readings to help with research. The programming lanaguage to be used was brought up by Matthew and I stated that I would be using Python as I am familiar with it and explained I will be doing research into libraries such as Matplotlib and this was agreed with by Matthew. We then discussed the vision of the project and some general ideas - although there are many forms the project could take and was decided this vision will be more specifc in the coming weeks when more research is carried out and data is evaluated.  

We finished by speaking about setting up regular meetings which was agreed as every Thursday 13:30-14:00.  


## Meeting 2 - 3rd October 2019, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

The meeting was moved to 14:00 as requested by Matthew and it was decided that this would be the new weekly meeting time. I started off by asking some quesions of Matthew:  
  * Preferred method of communication: email (keep the curreny thread of conversation to make it easier for both parties). It was also decided that Alistair would be cc'd in the email to keep him up to date also
  * Weekly status reports: email to Matthew the night before each meeting (Wednesday night)
  * Repo access: Matthew and Alistair both said they would not mind having repo access.  

As no status report was provided this week, I explained the work that I had done over the past week. We then moved on to discussing some papers where Matthew suggested I read the papers that were cited in the ones he provided. Alistair also suggested that I read the papers in order of years.
We then moved on to the topic of AWARE where Alistair explained this to me in the context of app tracking. Matthew then suggested that I download Iain Cattermole's code and try to run it and understand what is happening.

Matthew stated that there should be three main alogirthms I should be looking at: spring models, t-SNE and UMAP. I said I would do some reading on these. A general consensus was that we are still shaping the project in terms of which path to go down as many suggestions were brought up (spring models, machine learning, recommender system, potentially using description/reviews from app store dataset to cluster them) so it was decided that more reading would be done in order to develop a clear plan.


## Meeting 3 - 10 October 2019, 14:00-14:30

* Present - Matthew O'Hare, Professor Matthew Chalmers

At the start of the meeting I asked Matthew if he received my status report from the previous week alright and he did but struggled to open it. It was agreed that next week I will send it in plain text either in email or a text document. We spoke about what I had done in the previous week and I then asked what algorithms Matthew might recommend I use. He replied, stating I might need to use faster ones due to the large data however said that I should start small and build up. The easiest algorithms are the brute force and 96'. Matthew suggested I start with these, use a small amount of data and build it up. He suggested that I find out where the poker data came from (UCI data repo) and find out whether they are based on real hands or generated ones. He went on to say that app data is a lot more challenging than the poker data set as this has predefined categories where as app usage does not. He recommened that I email Alistair and ask for a small chunk of the data and potentially meet up with him to run through it.

We then spoke about a plan when I have received the data. Matthew suggested that I look at each attribute and plot them on a graph, evaluate the shape etc and use metrics like mean, min, max, range etc to understand what the data is showing. I may potentially get a hypothesis to prove or come up with new metrics when evaluating the data. He said that the distribution of app frequencies will not be uniform and to expect this. Matthew gave me things to watch out for like null values or error values in the data. We then spoke about what metrics to use for comparing items (items = a persons usage, individual apps etc) eg, hamming distance of the set of apps each user has installed. Matthew suggested I look at the metrics from the papers referenced in his paper. This could potentially lead to a comparison between previous studies when writng my dissertation. To finish, we spoke about being methodical when doing this project however it is one thing doing it, the main point is I must show how I was methodical when writing my disseratation and explain what I did, this will help a lot.


## Meeting 4 - 17 October 2019, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

Following on from last week, we started the meeting by me explaining the work I had done in a little more detail. I explained how the majority of reading was done on UMAP and Matthew stated that although a UMAP project would be good, it would be easier to get help from both Matthew and Alistair if the project was based on spring models, however this can be decided once the data has been obtained and evaluated. I also explained how I had found a potential other data set that could be used further down the line. Matthew also mentioned another potential data set - Carat. Although Alistair then found this data set online and found it to be not of much use, nonetheless I agreed to find it myself and have a look at it. It was mentioned that this could potentially be compared to the AppTracker data in future. Matthew also suggested I try find the data set from the Welke paper as that could be useful also. We also spoke about Iain's code once again and decided that next week we might have a look at it and try to fix a potential error in the metric part. I said I will have a look at this also this coming week. For the remainder of the meeting we tried to debug a problem that Alistair was having with connecting to the data set on Matthew's machine.

We finished by recapping the plan for the week. While Alistair is anoymising the data set, I will have a look for the data set from the Welke paper and the Carat data set. I will also have a further look at Iain's code to try find the bug before next week.


## Meeting 5 - 24 October 2019, 14:00-14:20

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

A shorter meeting than usual since there was less to talk out. I began by going over my weekly status report and then asked Alistair how he was getting on with the app usage data as I cannot make much more progress without it. He said he now has access to it so will hopefully have it to me by the start of next week. We then spoke further about other potential data sets that I could look at. Matthew said he will message the team behind the "Differentiating Smartphone Users by App Usage" (Welke et al.) paper and see if they would send a portion of data to analyse. Matthew also mentioned another data set that they have used before (bond?) that could potentially be found and used, he said he would have a look for it.

I then mentioned how I have still not found the error in Iain's code from last year. Matthew suggested I try running it with different data sets that we know the output to, for example, MNIST fashion or MNIST digits. I agreed to do this and Alistair suggested I bring my laptop with all the outputs to the next meeting and we will debug together if I have no luck.


## Meeting 6 - 31 October 2019, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

This meeting started on a positive note with Alistair stating that he had just about completed anonymising the data set which he showed to me and explained. He said he would email this to me soon. The columns in the data are UserID and AppID which Matthew suggested in future we could maybe add in genre and the length of time each user had the AppTracker downloaded but to begin with this would be fine. Moving on from this we decided to start out small and simple. Matthew suggested I understand each dimension well before using any algorithms with it. This means be formal in my process, start out with simple charts and graphs/different data structures (map, matrix etc) and evaluate the data in depth so I know what I am working with (mean, median, max, min, range etc), and then progress into harder more challenging tasks. Matthew also suggested this would be good when writing my dissertation and explaining this process, concentrating on things like design structure by giving reason as to why certain things were done (eg, why I chose a specific data structure to hold the data). This would all be good content.

We then moved on to talking about the data when it was used in Matthew and Alistair's paper where they said that due to large range in the length of time users had the app downloaded (from hours to years), they made the decision to chop off the top and bottom 1% to clean up the data (look in paper for exact details). This could be something I may look at doing depending on results when I come to evaluate the data. To finish, Matthew suggested I break everything down and make a plan of action and we agreed that by next week I will come back to them with everything I have found out about the data once evaluation is complete.


## Meeting 7 - 7th November, Cancelled by Matthew due to prior commitments


## Meeting 8 - 14 November 2019, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

I started the meeting by outlining my results from my data evaluation. I spoke about my graphs and how sparse the data was when Matthew suggested looking at something like Zipf's Law to maybe make the graphs easier to view. We spoke further about analysis and to make the results more meaninfgul. Matthew suggested I could use the top 100 apps for comparing distances (since every user should have hopefully used one of these) or top 300 or top 500 (like a sliding window) and compare the results to find the optimal parameters. I said I will look at the Welke et al paper and find out the parameters they used in their study.

I then asked Alistair about what he thought the top app would be in this data and he suggested spring board. He then went on to showing me the new data he had been working on where more columns were added to improve evaluation and analysis. Some extra columns were Apple v Non-Apple apps, category ID and the amount of time in seconds that we had seen the user (from the first bit of data to the last) so this will be helpful.

To finish, Matthew suggested I develop my idea for the project in terms of what I will do with the data.


## Meeting 9 - 21 November 2019, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

I began by showing my work from last week. There was confusion about the heatmap that I showed them and whether it was correct. We spoke about potential solutions to debug - make sure that the screen only shows one entry per pixel as there was a concern that it was grouping together multiple in a pixel. However Matthew said that this would be good content for the diss by explaining the problem and how I overcame it. I also had a question about a missing genre category which Alistair answered. ID 6021 is newstand. Furthermore, having discovered that the most used application was AppTracker, it may be necessary to exclude this from the results since this app was required however currently unsure what difference it would make. When talking about the filtering of users, I asked if there was a specific number that be a "good" amount but both Matthew and Alistair said no, they stated that there is not 1 perfect algorithm or dataset or metric for this, it is a case of trial and error and choosing the best fit and justifying my decision. There is also the potential to move into the machine learning area, for example, clustering to understand the data further.

The majority of the remainder of the meeting was about the dissertation. Matthew mentioned that for the diss, we want to create a kind of road map of how to do this data analysis so that in future it could be done with another dataset using the same guidelines. Also the most important thing is about showing reasoned judgements as to why I did things (eg, chose certain parameters etc).


## Meeting 10 - 28 November 2019, 14:00-14:30

* Present - Matthew James O'Hare. Professor Matthew Chalmers, Dr Alistair Morrison

I began by showing my work from last week. I explained the issue with the heatmap and showed the corrected version. From this we spoke about different metrics, at the moment the hamming distance shows more differences than similarities and takes into account all differences between users. It was suggested that I maybe look at other metrics, like the scaler product or give weights to similar values. An example of this would be to take into account the number of launches of an app by a user and then representing the distance as a function of the average usage of that app. 

I also stated that I have a lot of coursework at the moment so progress this week might be a bit slow as I prioritise other work but will do what I can.






















