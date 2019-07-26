## Solving python kata for acyclic graphs 

## Approach: 
- [x] make a drawing that visualised all the nodes
![alt text](https://github.com/karolinkas/python-katas/blob/master/network.jpg)

- [x] think of a simple real life example that helps imagining this:  
A train network where the trains have to deliver a bunch of packages and therefore have to go to each city only once
and can only travel one direction

![](https://media.giphy.com/media/PPWfbsCjUQJXsMEiim/giphy.gif)


## Steps taken:
1. Find direct connections from one city to another by searching through the edges array
2. Find further connections from a city you have been to to a next one by searching through the edges array of the next city
3. Make sure we don't visit any city twice by creating a lookup table for cities we've been to
