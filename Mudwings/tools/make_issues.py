# -*- coding: utf-8 -*-
"""
Script to generate html files for each Mudwings issue

@author: Tim Cootes
"""

def make_issue(i,image_dir,first_i,latest_i): 
    # Create html for issue i
    # Crude: Need to tidy up format
    filename="../issues/Mudwings-{:0>3d}.html".format(i)
    
    f=open(filename,"w")
    f.write("<html>\n")
    f.write("<title>Mudwings and the Rightful Bear: Issue {:0>3d}</title>\n".format(i))
    f.write("<head>\n")
    f.write("  <meta name=\"author\" content=\"Tim Cootes\">\n")
    f.write("  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("<h1 style=\"text-align:center\">\n")
    f.write("    <span style=\"color: brown\">Mudwings</span> and \n")
    f.write("    <span style=\"color: darkgreen\">The Rightful Bear</span>\n")
    f.write("    : Issue {:0>3d}</h1>\n".format(i))
    f.write("<p style=\"text-align:center\">\n")

    if (i==first_i):
        f.write(" First Previous\n")
    else:
        f.write(" <a href=\"Mudwings-{:0>3d}.html\">First</a>\n".format(first_i))
        f.write(" <a href=\"Mudwings-{:0>3d}.html\">Previous</a>\n".format(i-1))

    f.write(" <a href=\"../index.html\">Contents</a>\n")
    f.write(" <a href=\"../Mudwings-index.html\">Index</a>\n")
    
    if (i==latest_i):
        f.write(" Next Latest\n".format(i+1))
    else:
        f.write(" <a href=\"Mudwings-{:0>3d}.html\">Next</a>\n".format(i+1))
        f.write(" <a href=\"Mudwings-{:0>3d}.html\">Latest</a>\n".format(latest_i))
        
    f.write("<br>\n")

    f.write("<img src=\""+image_dir+"/Mudwings-{:d}.png\"><br>\n".format(i))
    f.write("<br>\n")
    f.write("</p>\n")
   
    
    f.write("<br><a href=\"https://TimCootes.github.io\">Tim Cootes</a> 2022\n")
    f.write("</body>")
    f.write("</html>")
    f.close()
    
    print("Page written to "+filename)
    
first_i=70
last_i=73
for i in range(first_i,last_i+1):
  make_issue(i,"../images",first_i,last_i)


# To do:
# - Add most recent issue option (Mudwings-latest.html) as a copy of last issue
# - Add target directory