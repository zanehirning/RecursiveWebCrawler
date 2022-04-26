# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

###Description

- The original URL must be an http(s) absolute URL
- From a starting URL provided by the user, this program will crawl the web and click on any links present, as well as printing them out.
- An integer will be given by the user, this is how many links deep the web crawler will crawl, the default is three links.
- A good solution will take a valid URL and crawl the web for coordinating links.
- If no input is given, a usage message will be printed and the system will exit without crawling.
- If bad input is given, an error message will be printed.

###What I know:

- I know how to take input from the user and provide usage messages/raise errors if bad input is given.

###What I don't know:

- All of the libraries we are given need to be looked at and understood. 
- I currently do not know how any of the libraries work.


*   A detailed written description of the problem this program aims to solve.
*   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.


## Phase 1: System Analysis *(10%)*

**Deliver:**

- The data used by my program will mostly come from the user. 
- The max-depth and the url are provided by the user.
- Depth and visited are parameters passed in, depth starts are 0, and visited can be an empty set or a set of url's that should never be visited.


- The output will take form of a "tree" in a sense. 
- The output will contain all the urls visited, it will also report some crawling statistics at the end of the crawl.


- Recursion will be used to create a "loop"
- Base cases will be given so an infinite recursion state is not met.
- The libraries provided will be used to assist us.
- Different kinds of errors will be raised when appropriate


*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).


## Phase 2: Design *(30%)*

**Deliver:**

```python
    def crawler(url, depth, maxdepth, visited):
        visited is a set of urls
        depth is current depth
        url is the starting url or current
        maxdepth is the maxdepth provided by the user, if not, use 3.
        
        Possible base cases:
            if url in visited. #if the url has already been visited, then it should quit.
            if depth > maxdepth. #if the depth is greater than to the max depth, we do not want to go farther.         
            
        If these base cases are not satisfied:
            append the url to visited
            update the url to be the current url
            print(url)
            return crawler(url, depth+1, maxdepth, visited)
        
        Printing out the spaces to form tree:
            for i < depth:
                print("    ")
```

- If the input is bad(a site that crawler is not able to visit), then the url will be added to the visited and the program will immediately return
- Exceptions will be thrown but the program should not crash. 
- URL's that do not contain http(s) will not be printed out.


## Phase 3: Implementation *(15%)*

**Deliver:**

```python
def crawl(url, depth, maxdepth, visited):
    if url in visited:
        return
    if depth >= int(maxdepth):
        return

    response = requests.get(url)

    if not response.ok:  	         	  
        print(f"crawl({url}): {response.status_code} {response.reason}")
        visited.add(url)
        return  	         	  

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
                    return crawl(url, depth + 1, maxdepth, visited)
    
        indents = ""
    for i in range(depth):
        indents += "    "
    visited.add(url)
    print(indents + url)
    return crawl(url, depth + 1, maxdepth, visited)

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
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        print("The user exited the program.")

    end = time.time()
    current = end - start
    print(f"The amount of time it took to crawl this url was {current} seconds.", file=sys.stderr)
    print(f"The number of unique URL's visited was {len(visited)}")
    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")
```

- While writing this code, I noticed that in some cases, my code would quit early. 
- This was because of the way I was doing my returning crawl statements, and adding things into visited.
- The url would not be updated to the next url to visit, thus is would stop because the url was already in visited.
- This was a pretty simple fix, I changed where my indents were printed out for conciseness, and then I removed the return statements regarding crawl
- I also had to change the crawl in the for loop to crawl the next time with absoluteURL and not url.


- I learned how to catch a keyboard interruption and end early.
- I learned more about recursion and how to use it to solve issues.

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

- I did not have any personal test cases. 
- I tested my code on each of the provided url's and tested different kinds of error catchings.
- My program seemed to catch every type of error I could think of, whether it is not an absolute URL, http(s), etc.

- All of the tests that I tried seemed to have worked, there were not any issues with any of the tests I ran.


## Phase 5: Deployment *(5%)*

**Deliver:**

Final code has been pushed. Everything looks correct on github.

## Phase 6: Maintenance

**Deliver:**

###1.
- Most of my program is pretty easy to follow an understand. Everything flows well and works together in order to be it easy to follow.
- It should not take long depending on the errors. Syntax errors would be easy to find. System failures that don't reach what was envisioned would be more difficult to find, but it is probably a result of failed recursion.

###2.
- This code should make sense to most people, if they understand how the libraries function and how recursion works it should be understandable.
- This code will make sense to me in six months, this code does not have any obvious errors.

###3.
- Implementations should be decently easy, it depends on the implementations that are needed.
- The implementation restrictions lie within the power of libraries that are utilized.

###4.
- This program should work on new hardware, and would probably work better on new hardware.
- This program should work on new or different OS's.
- As long as new versions don't change how libraries function or recursion works everything should work on the next version.

