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
  * The Hamming distance between two strings or equal length is the number of positions at which the corresponding symbols are different.
* Rest of the paper is just evaluating results. There are a few evaluations eg, app usage by hour of day, characterising app usage sessions, micro-usage, identifying users from app signatures.


* References: 9, 46
