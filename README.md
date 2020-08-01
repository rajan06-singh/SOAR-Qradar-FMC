# SOAR-Qradar-FMC

#This is an automated approach to take action on Qradar as part of response - blocking a source IP address on FMC when your defined rule on Qradar system triggers the event. For instance, if there is an active brute force attempt on one of your system. Build a rule on Qradar to detect such event. Make sure you capture the source IP under this detection rule. 

Once the detection rule is enable, you need to add custom action on Qradar as part of response to this rule. The configuration steps for custom action is out of scope here. Please follow Qradar documentation for this step. Under custom action, upload this file and follow below mentioned working principle. 

Pre-requisites: 
1. Username - This will be the administrator account on your FMC. 
2. Password - This will be the password of associated admin account. 
3. Source IP Address - On Qradar, it provides the option to extract source ip address when the monitoring rule triggers 
4. api_path - This need to be changed in the script. Refer FMC API_Explorer to get the api_path. The ID of the object is unique and depending on which object you want to modify, appropriate GET request should be issued. 

Note: These pre-requisites will be used as arguments to python file. Note, the order of these pre-requisites matters. You need to be careful while providing the argument in same order which is username, password and then sourceip (Or any interesting event field from Qradar) 

Working Principle:

Upload this python file under customized action on Qradar Systems. Select argument as username with value, password with value and select "sourceip" field from the event. You may select any field instead of sourceip you want to pass as argument. However remember this file will block the value of selected field on FMC. 

Now create correlation rule and add customized action as this file. Note - The python file is crafted in such a way that it will use "SourceIP" field. If you want to change this field, you need to change the same on Qradar system when you select the list of argument. 



