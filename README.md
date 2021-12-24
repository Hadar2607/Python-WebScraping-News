# Python-WebScraping-News
Receive news from 4 different sites (and send the news via email)

## Description:
* During my academic studies I do not have time to read news.
* Following this I developed in python a system that collects all the news of the day, keeps the news in a fileand even sends the file by email.

### Demonstration:

#### news from site 

![image](https://user-images.githubusercontent.com/72446237/147348587-e86cc1f0-5bb1-4cd1-b6ef-84192422be52.png)

#### You can see that the file has the same titles as the news site

![image](https://user-images.githubusercontent.com/72446237/147349953-ad73c408-2f1b-4943-bd2a-1a1233a288b0.png)


#### Another site:

![image](https://user-images.githubusercontent.com/72446237/147349484-b455f636-013f-4adc-be38-7449182a3e9a.png)

#### Same result

![image](https://user-images.githubusercontent.com/72446237/147349297-0c959796-8fac-4f90-8cc8-53264f9a8274.png)

#### The file is in a remote configuration (what is painted in black is the site name)

![image](https://user-images.githubusercontent.com/72446237/147350042-8c7eb47d-c797-49e3-90d5-0f904c68d53d.png)

#### Every new day a new file is added to the folder

![image](https://user-images.githubusercontent.com/72446237/147350123-1ace48d7-272a-476e-9271-6f83f1b352d0.png)

#### After the file is saved in a folder on the computer,the news file send to the defined emails.

![image](https://user-images.githubusercontent.com/72446237/147350394-9594232a-535b-4a6d-ad89-4eee53aa7ef5.png)

# Work strategy:
* Defining Super Class: (news)
* Defining Sub Class (each news site have separate class ) because there is a need for different work in gathering information from site to site.
* At the end of the information processing, all the inheriting classes use the same methods, which are defined in the parent class.
* In the main file, the entire program is run and managed.

# Modules:
* BeautifulSoup
* csv
* smtplib
* email



