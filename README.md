# SOAR-Qradar-FMC
Security Automated Response (Qradar - FMC)

#This is an automated approach to take action such as blocking a source IP address on FMC when your defined rule on Qradar system triggers the event. 

Pre-requisites: 
1. Username - This will be the administrator account on your FMC. 
2. Password - This will be the password of associated admin account. 
3. Source IP Address - On Qradar, it provides the option to extract source ip address when the monitoring rule triggers 
4. api_path - This need to be changed. The path includes id as the last resource of api path.  

Note: These pre-requisites will be used as arguments to python file. Note, the order of these pre-requisites matters. You need to be careful while providing the argument in same order which is username, password and then sourceip

Working Principle:

Go ahead and upload this python file under customized action with a name on Qradar Systems. Select argument as username with value, password with value and select "sourceip" field from the event. You may select any field you want to pass as argument. 

Now create correlation rule and add customized action as this file. Note - The python file is crafted in such a way that it will use "SourceIP" field. If you want to change this field, you need to change the same on Qradar system when you select the list of argument. 



