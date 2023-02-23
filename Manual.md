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
* Recording the changes in 'alert.log' along with the time of detection
* Recording the start and end time of the scan session in 'app.log'


#### Version 1.1

Bug Fixing-
* Bug in detecting the type of change(Add/Remove) was fixed


Key Features-
* Classifying the type of change(Add/Modify/Delete)
* Accept the user choice of directory
* Terminate the scan using Keyboard Interrupt


### Version 2

Key Features-
* Providing a regex based filter for user to filter the log changes according to their needs
* Providing a menu for user for navigating between the File Monitoring and regex


### Version 3

Key Features-
* Flagging whether the file is suspicious using two methods-
  * PE File Module
  * Virus Total API

#### Version 3.1

  Bug Fixing-
  * Bug in the regex based output fixed
  * Error in formatting the results fixed

Key Features-
* Accepting the regex expression from the user for filtering the records
* Tabulating the results of the Scanned session and regex using pretty table module
* Formatting the output further for better user convenience

### Version 4

Key Features-
* Creating a seperate log file for storing the user filtered records
* Writing  the filtered records into 'result.log' for communicating the results
* Mailing the report to the user for their further references with a appropriate styling and formatting
