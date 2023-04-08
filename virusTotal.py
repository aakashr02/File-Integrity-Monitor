# 178ba564b39bd07577e974a9b677dfd86ffa1f1d0299dfd958eb883c5ef6c3e1 - malicious hash

#virus total malware scanning script
import requests
import argparse
import os
import time
import json

# enter your private key here from virus total
key = '7c9ef07b7c35a62009279ffff171892d8f0949ba8f82856835e883ef2067030f'

# validate hash passed by user by checking its length
def checkhash(hsh):
        try:
                if len(hsh) == 32:
                        return hsh
                elif len(hsh) == 40:
                        return hsh
                elif len(hsh) == 64:
                        return hsh
                else:
                        print ("The Hash input does not appear valid.")
                        exit()
        except Exception:
                        print ('There is something wrong with your hash \n' + Exception)

#Function to connect to VirusTotal database and determine if the given hash is Malicious                                                                                                                                                                                                                                           
def VT_Request(hash):
        params = {'apikey': key, 'resource': hash}
        try:
                # passing the hash to the virusTotal API
                url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
                if url.status_code==200:
                        json_response = url.json()
                        
                        #Get the response code indicating if the hash was present in the VirusTotal database
                        response = int(json_response['response_code'])
                        
                        # if the hash is not present, it is likely to be safe
                        if response == 0:
                                return 0
                        
                        # if the hash is present
                        elif response == 1:
                                # Get the number of vendors who mark the hash as malicious
                                positives = int(json_response['positives'])
                                
                                # if no vendor marks it malicious return false
                                if positives == 0:
                                        return 0;
                                
                                # if some vendor marks it malicious return true
                                else:
                                        return 1
                        else:
                                return 0
        
        # if the VirusTotal Database cannot be contacted return -1                        
        except requests.exceptions.RequestException as e:
                return -1;
                
# running the program
# if __name__ == '__main__':
        # main()
# hsh = input()
# result = VT_Request(key, hsh)
# print(result)