# LogFileChallenge
Log File Challenge for Quartic.ai
-
Files:

\*.ipynb files - IPython/Jupyter Notebooks of the programs

\*.py files - Python programs

yaml_file.yaml - the YAML file for second excercise.

out.log - Sample log file

## Discussion Questions

### 1.  Briefly describe the conceptual approach you chose! What are the trade-offs?
If you want me to be honest, my basic approach was to cut on everything I'm not good at which was basically alot in this exercise. My daily style of programming is  either imperative(Bash) or declarative(Ansible/GCP Deployment Manager - YAML). I hadn't touched Python in a while.

For the first few hours when I started thinking about the solutions, I thought "Oh! I'll use a regex and put them all in a list and then move on from there". Then I thought that it'd be very inefficient or rather computationally expensive. That made me thinking then "Who's good at this?". Luckily, after my GCP certifications, I was looking for GCP community in my area and found a Google Developers Group and they were running a 3 day Machine Learning Crash Course based on [MLCC by Google](https://developers.google.com/machine-learning/crash-course/). That's where I discovered pandas(again - I had previously tried to take a data science course on Coursera and found it hard to come by due to the pace of the instructor) and knew what path to take.  That's where pandas came in and the first exercise was a breeze.

For the second exercise, I thought that I would be able to do it but that's all what I could come up with in a day. I mean, I could complete the program with all the conditions possible with the type of data we have, but would be very inefficient way of doing it. The trade off is the time complexity here. The moment the stream starts running in a loop, we are using way more CPU. With a larger dataset, we will start observing performance issues. It's also one of the many reasons that applications like Splunk and ELK stack require compute clusters to keep up with the log ingest and processing in real time. These issues could be solved with better data structures and more compute power, given more time. 

The other part to the second excercise was that although as an SRE I've had experience with Splunk and ELK stack for log analysis, I never really thought I would end up building one. I don't know if you'll like my work but for me personally, this is an impressive feat and a step in a good direction.

### 2.  What's the runtime performance? What is the complexity? Where are the bottlenecks?
I used the python `.time()` module to compute time taken that calculates CPU time.

The first exercise takes 9.47 secs to complete whereas the second exercise takes 4.14 secs to complete.

Using a GPU accelerator did not increase the performance by much. 

Complexity of both exercises is O(n).

The second exercise is partly also quick because a lot of code there is incomplete.

In the first exercise, the code runs slow where pandas computes the new dataframe that contains values from only specified timestamps. This could be reduced by processing data in chunks across a distributed architecture.

The second exercise has a tendency to get slower with more rules and more data.

### 3. If you had more time, what improvements would you make, and in what order of priority?
1.   Complete the second exercise. Optimize for flexibility and scale. Instead of hard coding If/else conditions, parse through the `key: value` structure, to create a proper rule set like an Ansible module
2. Write a better regex. Right now, the current regex does not capture the error message trace. A good log analyzer should be able to capture as much data as possible. The error message trace wasn't required for the excercise and involved taking care of the new line. It'd be a minor tweak but for the lack of time, I dropped it out.
3.   Chunk the dataframe in the first exercise. Make it quicker for larger datasets for real time data
4. Practice more Python for me. The best kind of Python, I know is for System Administrators which isn't needed much when working with on-prem clusters or cloud systems because a lot of tooling has already been done and is readily available. Python for System Adminstrators is just about getting the job done and doesn't really delve into data structures or functional computing. Moreover, over the last 2 years, we have automated our systems using Ansible to a point where a large monolithic deployment which would otherwise take 3 days is now done in 4 hours, and now it is at a point where it is about keeping those servers up through monitoring that is implemented in the combination of Splunk and a version of Nagios, so no Python there as well.
5. The other idea that I had if I had more time was to create a ML model for better alerts based on existing data. I would want predictive alerts in case hits for */login* page start spiking or number of *UnknownError* starts increasing. And I would want alerts before our services crash. I believe a linear regression based model can help. If we had more columns, we could use a classifier to prioritize some notifications over others and receive only actionable alerts. I desire to gain that knowledge by the end of my MLCC meetup and GCP - Data Engineering certification.
