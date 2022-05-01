# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:05:58 2022

@author: Tim Cootes
"""

from collections import defaultdict

# Set up structure to hold issue numbers for each keyword
issues_per_key = defaultdict(list)

n_keys=0
# Read in lines from file
# Assumed to have format:
# IssueNumber Keyword1 Keyword2 ...
# (arbitrary number of keywords)
with open('IssueKeywords.txt') as file:
    for line in file:
        b=line.split()
        if (len(b)>=2):
            issue=b[0]
            for k in range(1,len(b)):
                issues_per_key[b[k]].append(issue)
            n_keys+=len(b)-1
                

# Get issue numbers for each key (in alphabetic order)        
for key in sorted(issues_per_key):
    print(key, issues_per_key[key])
    
    
# Create index html file
# Crude: Need to tidy up format
index_file=open("../Mudwings-index.html","w")
index_file.write("<html>\n")
index_file.write("<title>Mudwings and the Rightful Bear: Index</title>\n")
index_file.write("<body>\n")
#index_file.write("<h1>Mudwings and the Rightful Bear: Index</h1>\n")
index_file.write("<h1><span style=\"color: brown\">Mudwings</span> and \n")
index_file.write("    <span style=\"color: darkgreen\">The Rightful Bear</span> : Index</h1>\n")

# Record first character in keyword
# Enables separating into groups by alphabet
first_char="-"
for key in sorted(issues_per_key):
    if (key[0] != first_char):
        first_char=key[0]
        index_file.write("---<b>"+first_char+"</b>---<br>\n")
        
    index_file.write(key+" : \n")
    for n in issues_per_key[key]:
        index_file.write("  <a href=\"Mudwings-"+n+".html\">"+n+"</a>\n")
    index_file.write("  <br>\n")

index_file.write("<br><a href=\"https://TimCootes.github.io\">Tim Cootes</a> 2022\n")
index_file.write("</body>")
index_file.write("</html>")
index_file.close()

print("Index written to ../Mudwings-index.html")

print("Number of keywords used",n_keys)
print("Number of unique keywords: ",len(issues_per_key))
