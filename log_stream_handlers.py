# -*- coding: utf-8 -*-
"""Log Stream Handlers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1syCb3X-0IanYWLkpQssGKTLSrN3r2tIh

# Set Project
"""

from google.colab import auth
auth.authenticate_user()

# https://cloud.google.com/resource-manager/docs/creating-managing-projects
#project_id = '[your Cloud Platform project ID]'
!gcloud config set project bookshelf-1860044

"""# Get Files

This above part could be removed. I used Google Colaboratory which are basically Google hosted Jupyter notebooks. The code above authenticates my GCP console to the notebook. I could make the files publically available either to all users or all Google authenticated users which would eliminate the need to autheticate or set project. 


---


The code below could also be removed if we directly provide the file names. I did not want to copy them in the temporary instance over and over again.
"""

# Download the file from a given Google Cloud Storage bucket.
!gsutil cp gs://ihopeitworks/* .

"""# Import Packages"""

import yaml
import logging
import sys
import re
import pandas as pd
import numpy as np
from datetime import datetime

"""#Open YAML File

I used YAML format instead of JSON because it is easier to read and also because I previously have worked with YAML in Ansible and GCP.
"""

with open("yaml_file.yaml", 'r') as yamlfile:
    config = yaml.load(yamlfile)

"""#Regex

I used my experience with Splunk to define regex. Splunk takes in each line in the log file and then passes it through a regex to get fields.
"""

regex="^((\d{4}-\d{2}-\d{2})\s(\d{2}:\d{2}:\d{2}\.\d+))\s\[PID (\d+)\]\s\[(\d+)\w{2}\]\s\[UID (\w+)\]\s\[(\w+)\]\s(\/\w+)(.*Error name: (\w.+))?(.*)$"

"""#Open Stream and check conditions from YAML (Incomplete)

We open the file as an input stream and start reading a line at a time. Then extract the regex matches in a line and append them to the empty lists. I created empty lists because then from there on I can either map them to numpy or a pandas dataframe to run analysis. 

This part of the code is currently very static. The part that I couldn't get through was processing all of this while data was streaming. I could understand  that there is a need to create event handlers which would be something very similar to creating a custom Ansible module. What I could not understand was to handle new rules for which the functions have not been written so I could write something like [this](https://docs.ansible.com/ansible/2.3/dev_guide/developing_modules_general.html):

At one point I could only either stream the data and output log if the condition matches or analyze the data, no both at the same time.

For example, from the example rules, I could write a rule that if the error is equal to the value set in the YAML file, then write a log line, but I could not figure out how to do it if it matches a given count in the specified time delta.
 
If I process information outside the loop that reads the lines, then we are out of the stream and if I process it inside the loop then there is only one value in the loop at that moment. 

If I initialize the empty lists in the loop, the lists are again fresh empty everytime a line is read.

The way this is taken care of in Ansible and GCP is that in the background there is a preset YAML file that defines the style from which the scripts consume data.

I took a similar approach and created a YAML file that contains some sample parameters and read from there.
"""

with open('out.log', 'r') as sys.stdin:  # Open the file as an input stream

    # Initialize empty lists. I did not want to run the analysis in the loop while it loads the stream.
    
    timestamps = []
    pid = []
    response_time_in_ms = []
    uid = []
    log_level = []
    url = []
    error_message = []
    error_type = []
    message = []
    
    lines = sys.stdin.readlines()
  
    # print(lines) ## List of lines
  
    for line in lines:  # Start reading from lines as an input stream
  
        regex_read = re.findall(regex,line) # single element tuple as list
 
        #   Extracting Date/Time isn't required but comes handy.
  
        #   date = "".join([match[1] for match in regex_read]) 
        # This was the previous code where each parameter contained all values as a list of strings
    
        #   time = "".join([match[2] for match in regex_read])

        timestamps.append("".join([match[0] for match in regex_read])) 
        # These values contain list of lists that have a single value.
        # We convert them into a string and then append them to the list.
        pid.append("".join([match[3] for match in regex_read]))
    
        response_time_in_ms.append("".join([match[4] for match in regex_read]))
    
        uid.append("".join([match[5] for match in regex_read]))
    
        log_level.append("".join([match[6] for match in regex_read]))
     
        url.append("".join([match[7] for match in regex_read]))
    
        error_message.append("".join([match[8] for match in regex_read]))
      
        error_type.append("".join([match[9] for match in regex_read]))
    
        message.append("".join([match[10] for match in regex_read]))
      
      #try/catch exceptions within the loop
      
        try:
            if (config['log_level']['enabled_flag']) == True:                         
              #Check if we even need to write a log if with conditions based on log_level
                if (config['log_level']['count_thresh'] < 7 and
                   (len(set(log_level[-config['log_level']['count_thresh']:]))) == 1):
                       logging.warning('Watch out!')
                ##At each line check if last n elements that are specified as 
                #config['log_level']['count_thresh'] are same 
                #and write a log if the condition matches
                                                        
                                                                                    
        except:
          pass
  
  # The above solution kinda works but is way too complex and inefficient.

# The other idea was to use dataframes
  
  
#   logfile=pd.DataFrame({'Timestamp': timestamps,
#                      'PID': pid,
#                      'Response Time': response_time_in_ms,
#                      'UID': uid,
#                      'Log Level': log_level,
#                      'URL': url,
#                      'error_message': error_message,
#                      'error_type': error_type,
#                      'message': message})

  
  
  
  
#   logfile=logfile.replace('', np.nan)
#   logfile = logfile.dropna(how='all') 
#   logfile['Timestamp'] = pd.to_datetime(logfile['Timestamp'])
#   logfile['Response Time']=pd.to_numeric(logfile['Response Time'])
  
  
  

  
  
  
#logfile.dtypes

#print(logfile['Timestamp'].iloc[-1])

#print (pd.date_range(start=logfile['Timestamp'].iloc[-1], end=logfile['Timestamp'].iloc[0],freq='S'))
  
  
#   ############################################################################################
#   #             INSERT TRY/CATCH STATEMENTS FOR THE CONDITIONS                               #
#   ############################################################################################
  
  
  
# #print(type(configfg['log_level']['count_thresh']))


 
#   #print(timestamps)

    
# #print(timestamps[0])
        
#print(timestamps)