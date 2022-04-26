# Recursive Web Crawler User Manual

Required Third Party Libraries:
    Beautifulsoup
        installation:
            pip3 install --user beautifulsoup4
            
            depending on python version
                pip install --user requests
            
    Requests
        installation:
            pip3 install --user beautifulsoup4
            
            depending on python version
                pip install --user requests


How the program works/what the user needs to do:
    The user must provide an absolute URL(explanation below). Another parameter is optional, the user may specify the depth at which they wish the crawler to crawl. The depth is how many urls deep it will crawl. 
    This program will crawl the internet until the depth requested is hit, if no depth is requested, a default depth of 3 will be provided.
    The program will print out the visited websites in a "tree" formation, as well as provide runtime statistics at the end of the crawl.
    
Absolute URL:
    An absolute URL contains enough information to locate a resource. It must include a scheme followed by "://", as well as a hostname.
    The scheme must by an http or an https for this program to run, the program will not crawl the website otherwise.

Relative URL:
    Relative URLs are urls that do not need to contain a scheme or a hostname. They may include only a partial path. These urls should be ignored by the program and will not be crawled.

