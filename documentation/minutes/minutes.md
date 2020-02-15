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

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

I began by showing my work from last week. I explained the issue with the heatmap and showed the corrected version. From this we spoke about different metrics, at the moment the hamming distance shows more differences than similarities and takes into account all differences between users. It was suggested that I maybe look at other metrics, like the scaler product or give weights to similar values. An example of this would be to take into account the number of launches of an app by a user and then representing the distance as a function of the average usage of that app. 

I also stated that I have a lot of coursework at the moment so progress this week might be a bit slow as I prioritise other work but will do what I can.


## Meeting 11 - 05 December 2019, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

As usual, the meeting began with me explaining what I had managed to achieve in the previous week. Matthew was happy with my progress and we went on to talking about what the plan for the upcoming week. I stated that I had an upcoming exam (11th December) therefore not much progress will be made while I concentrate on that. However we agreed that the plan for the next few weeks would be to take into account the average usage of each app for a user across the whole data set and to attempt other metrics to find the most appropriate one.


## Meeting 12 - 12 December 2019, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers, Dr Alistair Morrison

Last meeting before Christmas, I explained how I have not achieved much this past week due to my exam however now that it is over, work will continue. We then spoke about what work I will do over the Christmas break before semester 2. I stated that I would continue evaluating the data and to hopefully find the best similarity metric for comparing the data. Furthermore I said that I had hoped to create some inital spring models with the data and the chosen metric. Matthew was happy with this and also suggested I note down my process writing down everything I have done and the technical specifications of what I am doing, for example, the time and memory consuption for each task etc.


## Meeting 13 - 19 December 2019, No meeting this week


## Meeting 14 - 16 January 2020, 14:00-14:30 (Skype call)

* On call - Matthew James O'Hare, Professor Matthew Chalmers

Short video call due to Matthew working from home. Began by explaining the work carried out over the Christmas period and my decision on my chosen metric - euclidean. Matthew explained the importance of normalising values when calculating this otherwise some columns may give disproportionate results as they over power or out weigh others. Matthew suggested I normalised between 0 and 1 (find min and max and scale down or by having an equal number of points either side of the mean (variance = 1)). We spoke about the accuracy of both hamming and euclidean where hamming is linear and euclidean is continuous but when moving to continuous values, we have to be careful about how much we rely on this distance being accurate. Similar with hamming however, linear may not always be accurate either as we do not neccessarily know what the numbers actually mean.

Matthew also suggested that I set up assumptions before using each metric, run them and compare. We spoke about the usefullness of t-SNE. The only problem with it is it will find clusters in the data even if there is no clusters in the first place making it slightly unreliable. UMAP takes into account global structure as well as local making it slightly better so could be a good idea to attempt both of them. However they are both very reliant on parameters and metrics. An important point from the meeting was that there is no right or correct metric or visualisation.


## Meeting 15 - 23 January 2020, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers

First face to face meeting since Christmas so there was a lot to talk about. I began by showing Matthew my results from the created visualisations. Instead of a final end graph, he suggested that I plot the graph after every, for example, 10 iterations and analyse what the visualisation is showing us and tweak the parameters to see how they change the visualisation. Another suggestion was to not set a max iterations or to plot the error and average velocity and examine when they plateu out. We also spoke about checking the data to see if there are any clusters in the first place, using sklearn and simple algorithms like k-nearest neighbour. Matthew also gave me a website - distil.pub - that has an interesting article on t-SNE that could be useful.

Regarding the metric and using the standarised euclidean distance, it was suggested that I use both the standardised and normal version and compare results. Also check that the standardised distance is calculated properly. Furthermore, as my current visualisations are only on a sample of the data, we decided it would be a good idea to attempt to use larger samples and calculate the times associated with each and how it is affected when more dimensions and apps are added.

To end the meeting we spoke about the writing of the dissertation. Matthew suggested that a good narrative for the dissertation would be to create a pipeline of my process and at each stage, give recommendations and the effects of choices at that stage on the next stage and the overall project. It was suggested that I start to note down potential headings.


## Meeting 16 - 30th January 2020, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers

As usual the meeting began with me showing Matthew my work from the past week with UMAP and kmeans visualisations. Matthew made a few points regarding them. For UMAP he suggested that I investigate the clusters to see whether the locations of each data point are appropriate and "correct". For kmeans, he suggested that I have a look to see whether the produced visualisation is actually correct as he is not sure. A suggestion was to reduce the size of the dots and look at plotting better maybe by using specifc algorithms or techniques for it.

The main points taken away to work on was to investigate kmeans to find natural clusters in high dimensional data and this would help to find a good value for k. Kmeans could then be the base when comparing to spring models, t-SNE and UMAP. Secondly, investigate potential clusters in spring models (even though they are not separate). This could potentially be done by increasing the distance between points in the spring models algorithms, if possible that is.


## Meeting 17 - 05th February 2020, 14:00-14:30

* Present - Matthew James O'Hare, Professor Matthew Chalmers

Since I had not made much progress this week, it was a quick meeting. Matthew emphasised the point of time management and making good use of my time in the upcoming weekes. He suggested that I look at what coursework and other university work I have coming up and plan around it to make sure I do not run out of time when writing the dissertation.


## Meeting 18 - 13th February 2020, 14:00-14:30 (Skype Call)

* On call - Matthew James O'Hare, Professor Matthew Chalmers

Started the call by giving an update on my progress. Matthew explained that once I was settled with my parameters and algorithms, the next step was to invetigate what these visualisations tell us about the data itself - what patterns/trends are there within the data, outliers etc (what makes them different to the rest/why) - these are all good points to talk about when writing the dissertation and could be a potential chapter. Matthew suggested that I now map out each chapter so I have a clear plan of what I want to talk about in each - plan/develop/create a story!

I asked Matthew what is better - showing high dimensional or low dimensional clusters. He replied that high dimensional clusters gives us unbiased clusters that are not dependent on the algorithm used where as low dimensional clusters are more post processing (since they show clusters based on where the algorithm has plotted each point). They both provide valid points to talk about and can compare them however when using high dimensional clusters, this allows us to analyse and compare how different algorithms plot the same clusters in different ways and positions.

Matthew stressed on being objective when writing the dissertation though. He stated that it is not up to me to push or prove an opinion on the best algorithm, the most important thing is to simply present my findings and compare them and allow the reader to create their own opinion.










