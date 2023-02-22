# File-Integrity-Monitor
The file integrity monitor checks for the integrity of your directory and the files in it. It allows the user to perform log analysis on the changes logged for the directory.
As a first step, a log file of the directory of interest is created. This contains four comma separated values corresponding to the file name, status, time and suspicion check. The status is determined by using hashing mechanism to compare and conclude if addition, modification or deletion of files has occured. Suspicion is determined by using two methods: Virus Total to check for suspicious hashes and PR file module to analyse executable files. Lastly, the product allows for manual log analysis using a regex based filter to acquire relevant data. A copy of the selected records shall be mailed to the user on request.   

:--: 
## Flow chart of our project
:--:
<div align="center">


<img width="593" alt="image" src="https://user-images.githubusercontent.com/62467011/220698818-d5a82c9b-2f02-4548-a6f6-b679aa8a5ce1.png">

</div>
