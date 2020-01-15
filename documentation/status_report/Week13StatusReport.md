# Week 13 Status Report

This week started by me getting back into work after the Christmas break.

Some good progress has been made since the last meeting and over Christmas. Firstly, extensive analysis and comparisons between various similarity metrics have resulted in me choosing euclidean distance as the most appropriate metric. This is due to representing point by point differences for each user which is ideal for this situation. Having said this, I have decided to continue to also use hamming distance as a base metric to compare to as this is still proven to be good.

I have also started creating spring models. I have used Iain's code as a starting point to work on from and adapted it to create visualisations using brute force, Chalmers 96, hybrid and pivot algorithms with my data and metrics. I used both hamming and euclidean distance as metrics and evaluated how well they perform, I can show my results tomorrow. I am currently only working with a small sample of the data to help me understand the results and keep runtimes low (currently ~1-5s).


