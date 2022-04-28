#!/usr/bin/python3  	         	  

#                         ~  	         	  
#                        (o)<  DuckieCorp Software License  	         	  
#                   .____//  	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor  	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	         	  
#  	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR  	         	  
# customer of DuckieCorp, to deal in the Software without restriction,  	         	  
# including without limitation the rights to use, copy, modify, merge,  	         	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	         	  
# permit persons to whom the Software is furnished to do so, subject to the  	         	  
# following conditions:  	         	  
#  	         	  
# The above copyright notice and this permission notice shall be included in  	         	  
# all copies or substantial portions of the Software.  	         	  
#  	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	         	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	         	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  	         	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  	         	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  	         	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS  	         	  
# IN THE SOFTWARE.  	         	  


# pip install --user requests beautifulsoup4  	         	  
import requests  	         	  
from bs4 import BeautifulSoup  	         	  
from urllib.parse import urlparse, urljoin  	         	  
import sys  	         	  
import time  	         	  

def crawl(url, depth, maxdepth, visited):
    """  	         	  
    Given an absolute URL, print each hyperlink found within the document.  	         	  

    Your task is to make this into a recursive function that follows hyperlinks  	         	  
    until one of two base cases are reached:  	         	  

    0) No new, unvisited links are found  	         	  
    1) The maximum depth of recursion is reached  	         	  
    """

    if url in visited:
        return
    if depth > int(maxdepth):
        return

    indents = ""
    for i in range(depth):
        indents += "    "

    response = requests.get(url)
    visited.add(url)
    print(indents + url)
    if not response.ok:
        print(f"crawl({url}): {response.status_code} {response.reason}")
        visited.add(url)
        return




    try:
        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')

        for a in links:
            link = a.get('href')
            if link:
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link)

                # Only deal with resources accessible over HTTP or HTTPS
                if absoluteURL.startswith('http'):
                    if "#" not in absoluteURL:
                        crawl(absoluteURL, depth + 1, maxdepth, visited)
    except Exception:
        print("This URL is invalid.")

if __name__ == "__main__":

    visited = set()
    maxDepth = 3
    depth = 0
    if len(sys.argv) < 2:  	         	  
        print("Please provide an absolute url and an optional max depth.", file=sys.stderr)
        exit(0)
    elif len(sys.argv) == 3:
        url = sys.argv[1]
        maxDepth = sys.argv[2]
    else:  	         	  
        url = sys.argv[1]

    start = time.time()
    parsed = urlparse(url)
    try:
        if parsed.scheme == "http" or parsed.scheme == "https":
            if parsed.netloc:
                crawl(url, depth, maxDepth, visited)
        else:
            print("Please provide an absolute URL that contains http(s)")
            exit(0)
    except KeyboardInterrupt:
        print("The user exited the program.")

    end = time.time()
    current = end - start
    print(f"The amount of time it took to crawl this url was {current} seconds.", file=sys.stderr)
    print(f"The number of unique URL's visited was {len(visited)}")
    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")
