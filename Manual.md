# File Integrity Monitor

## Product Description
The file integrity monitor checks for the integrity of your directory and the files in it. It allows the user to perform log analysis on the changes logged for the directory. As a first step, a log file of the directory of interest is created. This contains four comma separated values corresponding to the file name, status, time and suspicion check. The status is determined by using hashing mechanism to compare and conclude if addition, modification or deletion of files has occured. Suspicion is determined by using two methods: Virus Total to check for suspicious hashes and PE file module to analyse executable files. Lastly, the product allows for manual log analysis using a regex based filter to acquire relevant log data. A copy of the selected records shall be mailed to the user on request.

## Features
* Logging changes (add/modify/delete) in a directory
* Flagging suspicious changes
* Log Analysis using Regular Expression 
* Mail reports

## Installation and Setup


## Environment Compatibility


## Version History
### Version 1
This version is the basic version of the application.Which computes the hash of all the files in the given directory and its sub directories and storees the hashes for continously monitoring any changes in the file hashes. If any changes is detected in the file hashes,changes are  recorded to 'alert.log'.It also has additional feature to detect what type of changes which is made to file(Add/Modify/Delete). But this version had a bug as it only detected for modification in file and it was not able to detect the addition and deletion of files.

Key Features-
* Computing the hashes of all files in given directory and its sub directory
* Detect for changes in file content in directory
* Recorded the changes in 'alert.log' along with the time of detection
* Recorded the start and end time of the scan session in 'app.log'


#### Version 1.1

Bug Fixing-

Key Features-
* Classifying the type of change(Add/Modify/Delete)
* Accept the user choice of directory
* Terminate the scan using Keyboard Interrupt


### Version 2

Key Features-
* Creating the 


### Version 3

Key Features-

#### Version 3.1

Key Features-

### Version 4

Key Features-

