
## Decisions
Since each directory could have sub-directories and a "sub-directory" itself can have sub-sub-directories and so on, we need to check the directories, sub-directories, sub-sub-directories..etc. This checking process is the same for each directory or sub-directory or ... etc. So if we solve it for one directory, we can generalize it to the all directories, sub directories, ... etc and it goes into the direction of recursive functions. 
## Time efficiency
O(n<sub>1</sub>*n<sub>2</sub>*n<sub>3</sub>...n<sub>m</sub>) ~ O(n<sup>m</sup>) where n<sub>1</sub>, n<sub>2</sub> ... n<sub>n</sub> are the numbers of "directories", "sub-directories" and "sub-sub-directories" and so on.
## Space efficiency
The length of returned list plus number of function calls: O(n)