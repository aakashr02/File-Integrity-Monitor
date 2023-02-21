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

# def main():
#         parser = argparse.ArgumentParser(description="Virus Total Hash Check by  Mitul M Narotam")
#         parser.add_argument('-o', '--output', required=True, help='Output File Location EX: /Home/Desktop/output.txt ')
#         parser.add_argument('-H', '--hash', type=checkhash, required=False, help='Single Hash EX: d41d8cd98f00b204e9800998ecf8427e')
#         parser.add_argument('-u', '--unlimited', action='store_const', const=1, required=False, help='Changes the 26 second sleep timer to 1.')
#         args = parser.parse_args()
                                                                                                                                                                                                                                           
#         #Run for hash + key                                                                                                                                                                                                                
#         if args.hash and key:                                                                                                                                                                                                              
#                 file = open(args.output,'w+')                                                                                                                                                                                              
#                 file.write('\n\nBelow is the identified malicious hash.\n\n')                                                                                                                                                              
#                 file.close()                                                                                                                                                                                                               
#                 VT_Request(key, args.hash.rstrip(), args.output)                                                                                                                                                                           
                                                                                                                                                                                                                                           
def VT_Request(hash):
        params = {'apikey': key, 'resource': hash}
        url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
        json_response = url.json()
        # x = str(json_response)
        # x = x.replace("'", '"')
        # x = x.replace("False", '"False"')
        # x = x.replace("True", '"True"')
        # x = x.replace("None", '"None"')

        # parsed = json.loads(x)
        # y =json.dumps(parsed, indent = 4, sort_keys=True)

        # print ("\n")
        response = int(json_response.get('response_code'))
        if response == 0:
                # print (y + "\n\n" + hash + ' is not in Virus Total')
                # file = open(output,'a')
                # file.write(y + "\n\n" + hash + ' is not in Virus Total')
                # file.write('\n')
                # file.close()
                return 0
        elif response == 1:
                positives = int(json_response.get('positives'))
                if positives == 0:
                        return 0;
                        # print (y + "\n\n" + hash + ' is not malicious')
                        # file = open(output,'a')
                        # file.write(y + "\n\n" + hash + ' is not malicious')
                        # file.write('\n')
                        # file.close()
                else:
                        # print (y + "\n\n" + hash + ' is malicious')
                        # file = open(output,'a')
                        # file.write(y + "\n\n" + hash + ' is a malicious hash. Hit Count:' + str(positives))
                        # file.write('\n')
                        # file.close()
                        return 1
        else:
                return 0
                # print (y + "\n\n" + hash + ' could not be searched. Please try again later.')
# running the program
# if __name__ == '__main__':
        # main()
# hsh = input()
# result = VT_Request(key, hsh)
# print(result)