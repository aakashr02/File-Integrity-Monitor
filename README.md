# File-Integrity-Monitor
The file integrity monitor checks for the integrity of your directory and the files in it. It allows the user to perform log analysis on the changes logged for the directory.
As a first step, a log file of the directory of interest is created. This contains four comma separated values corresponding to the file name, status, time and suspicion check. The status is determined by using hashing mechanism to compare and conclude if addition, modification or deletion of files has occured. Suspicion is determined by using two methods: Virus Total to check for suspicious hashes and PE file module to analyse executable files. Lastly, the product allows for manual log analysis using a regex based filter to acquire relevant log data. A copy of the selected records shall be mailed to the user on request. 



## Flow chart of our project
<div align="center">


<img width="593" alt="image" src="https://user-images.githubusercontent.com/62467011/220698818-d5a82c9b-2f02-4548-a6f6-b679aa8a5ce1.png">

</div>


## Comparsion and Analysis with Other Tools

| Feature | File Integrity Monitoring System | Wazuh File Integrity Monitoring System |
| :---: | :---: | :---: |
| Directory and file monitoring | Monitors a single directory and its files | Can monitor multiple directories and files across multiple servers |
| Change detection | Uses hashing mechanisms to detect changes in files | Offers similar functionality with additional features such as rootkit detection |
| Suspicious activity detection | Uses Virus Total to check for suspicious hashes | Registry monitoring for system configuration changes, Docker container monitoring |
| Exe File Monitoring | Uses PE file module to analyze executable files | Registry monitoring for system configuration changes, Docker container monitoring |
| Real-time alerts | Provides real-time alerts when changes are detected | Provides real-time alerts and notifications for any anomalies or security threats |
| Manual log analysis | Allows manual log analysis using regex-based filter | Provides centralized log management and analysis with Elasticsearch and Kibana | 
| Integration | 	Does not offer integration with other security tools | Integrates with other security tools such as vulnerability scanners, SIEMs, and IDS |
| Open-source |  Not yet Published | Yes, it is an open-source platform |
| Scalability | Suitable for smaller organizations or those with simpler needs | Suitable for larger organizations with complex security needs |
| Support | Not yet Provided | Provides community support as well as commercial support for enterprise users |


Overall, Wazuh file integrity monitoring system offers more advanced features and capabilities than the file integrity monitoring system described earlier, such as registry monitoring, Docker container monitoring, and centralized log management and analysis with Elasticsearch and Kibana. Additionally, Wazuh integrates with other security tools such as vulnerability scanners, SIEMs, and intrusion detection systems, making it a more comprehensive security solution. However, the file integrity monitoring system described earlier may be a suitable option for smaller organizations or those with simpler security requirements.
