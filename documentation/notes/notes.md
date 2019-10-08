# Reading Notes

* Visualisation of Mobile App Usage (ID:8714)
* Matthew James O'Hare
* 2255357o
* Professor Matthew Chalmers

Notes made from each reading/paper/article throughout the project

### A Large-Scale Study of iPhone App Launch Behaviour (Paper 1)

* Android is preferred to conduct research on app launch data and general usage and many studies have been carried out however no large scale study of iOS (mainly due to it being more "locked down", ie. apple have more restrictions on the functionality of apps on the App Store).
* Using only Android for studies could result in sampling bias since around a third of mobile devices have iOS (21).
* Reproduction (same phenomena but different conditions/user groups) over replication (re-perform experiments exactly as done in the past however might not be reliable if technology has changed since then).
* There have many works carried out (Related Work) to collect large amounts of data eg, time phone is on and off, the apps people install and usage patterns of app launches.
* iOS studies have only been carried out with small/local groups of people therefore does not reflect the global population.
* Results from these studies change quickly due to fast paced field so how often must they be updated/re-published to be kept up to date?/Would this be accepted without any new data/user groups?/Is this classed as HCI or more research and analytics?
* AWARE
* Using user data from jailbroken iPhones may raise questions about how representative the data actually is of iOS users.
* Data was collected via AppTracker consisting of a "backgroud logging framework that captures information on device use, and a foreground UI that displays charts and statistics on app use durations. It records timestamped logs of every time an app is opened or closed on the device. It also tracks every time the device is locked or unlocked... No information is recorded on activity withing individual apps, or activity over networks."
* "AppTracker regularly uploads user app launch data to our servers, together with a timestamp, device type, device identifier, and timezone".
* It is in an open question how personally identifiable a user might be from their app launches.
* Downloaded over 40,000 times as of September 2017 with users supplying 28 million app launch events.
* Hamming distance is used to calculate how similar users are based on the apps they have and use
  * The Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different.
* Rest of the paper is just evaluating results. There are a few evaluations eg, app usage by hour of day, characterising app usage sessions, micro-usage, identifying users from app signatures.


* References: 9, 46


### Falling Asleep with Angry Birds, Facebook and Kindle - A Large Scale Study on Mobile Application Usage (Paper 2)

* Mobile devices are compared to a "Swiss Army Knife" in that mobile phones provide a plethora of readily-accessible tools for everyday life.
* Uses data from AppSensor.
* Users typically spent a long time overall on their phones (59.23 mins) but each app was only opened for a short duration at a time eg, 71.56s although vary extensively between app categories.
* This paper is mainly examining results although interesting read and some good graphs.
* Context-aware recommender systems - recommend potential apps based on previous usage and usage from many other users ie, collaborative filtering.
  * Collaborative filtering is a method of making automatic predictions (filtering) about the interests of a user by collecting preferences or taste information from many users (collaborating)


### Differentiating Smartphone Users by App Usage (Paper 3)

* 99.4% of all users have unique usage patterns amongst the top 60 gloablly used apps, 99.67% for top 500.
* Users can be identified by virtually anything, browser version/extensions, installed fonts, timezone, Android ID etc.
* The Hamming distance between users is so large that starting or stopping to use a few additional apps will not allow the majority of users to disguise themselves, behaviour is highly individual and hard to change.
* Uses the Menthal dataset.
* A user is "anonymous" if there is some other user with a hamming distance of 0 (very few occasions - 0.33% of users in this study, out of 46726).
* The average Hamming distance in this case (for top 500 used apps) was 25.93 with 95.27% of users, their closest neighbour had a Hamming distance of at least 10 and 99.54% of users closest neighbour was at least 2.
* The average Hamming distance in this case (for top 60 used apps) was 4.9 however this was expected and still shows how most users have unique usage patterns. 

* References: 3, 7 (maybe)


### Markov Recap (From Artificial Intelligence course)

* A markov model is a stochastic model used to model randomly changing systems. It is assumed that future states depend only on the current state, not on the events that occurred before it, ie the future is independent of the past given the present.
  * Stochastic - can not determine the next state based on the current state and action due to randomness in the environment.
* A Markov chain is a mathematical system that experiences transitions from one state to another according to certain probabilistic rules.


### Modelling Smartphone Usage: A Markov State Transition Model (Paper 4)

* Markov chains have been used for many aspects of mobile computing, from optimising to predicting.
* Typically used to describe systems that have a set of observable states (phone on, phone off, locked, unlocked) and a transition matrix defines the probabilities of moving between these states.
* Static transition matrix leads to very restrictive models for many empirical settings and allowing transition probabilities to vary over time may be better. (done in another study) However this does not take into account continuous time.
* To overcome this, continuous-time Markov chains were developed to replace the transition matrix with functions. Their aim is to model how much time a model spends in a particular state. However they assume an exponential density distribution regarding the time spent at each state.
* To combine the best of the two , time-varying transition probabilites for Markov regime switching models were developed and used here.
* AWARE is used to capture hardware, software, and human based data from Android powered smartphones and can then be freely used in eg, optimising the battery life of mobile devices and understanding application use.
* Majority of the paper is evaluating and comparing results of state transitions and could be useful if needing that information at any point.
* Designer's and Knowledge free transition matrices - there is an explanation on both if required.


### Spring Embedders and Force Directed Graph Drawing Algorithms

* Force-directed algorithms, also known as spring embedders, are one of the most flexible methods for calculating layouts of undirected graphs. 
* They calculate the layout of a graph using only the information contained within the structure of the graph itself, rather than relying on domain-specific knowledge.
* These drawn graphs tend to be aesthetically pleasing, exhibit symmetries and tend to produce crossing-free layouts for planar graphs.
* Traditional spring layout methods rely on spring forces. There are repulsive forces between all nodes (based on Coulomb's Law), but also attractive forces between nodes which are adjacent (based on Hooke's Law).
  * The nodes are then moved according to the net force acting upon them.
* In general, force-directed methods define an objective function which maps each graph layout into a number in R+ representing the energy of the layout.
  * This function is defined so that low energies correspond to layouts which adjacent nodes are near some pre-defined distance from each other, and in which non-adjacent nodes are well-spaced.
  * A layout of this graph is then calculated by finding a (often local) minimum of this objective function (gradient descent).

* Decent source had a few algorithms on it and could be worth a re-read at some point


### PyData Ann Arbor: Leland McInnes | PCA, t-SNE, and UMAP: Modern Approaches to Dimension Reduction - YouTube Video

* Feature engineering - Find core features in your data.
* 2 ways of dimension reduction - Matrix Factorization, Neighbour Graphs

* Matrix Factorization - needs lots of different algorithms, eg, Principal Component Analysis (PCA), Latent Dirichlet Allocation, even Word2Vec

* Neighbour Graphs - there are also lots of algorithms, what graph is being constructed? how are you going to weight the edges? etc. This can lead to different algorithms being used eg, t-SNE, UMAP, Laplacian Eigenmaps etc

* PCA
  * The old workhouse of dimension reduction, been around for a long time although relevant
  * One can view it as trying to find a way to recontrsuct the data as a linear combination of a small number of prototypes.
  * Whole point is to attempt to reduce/minimise this reconstruction error (how close is this linear combination of prototypes to the original data) (Figure 1)
* We can reduce from very high dimensions and still keep a lot of information from the data (overall structure etc)

* t-Distributed Stochastic Neighbour Embedding (t-SNE)








