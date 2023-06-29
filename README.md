# Suicide Prevention APP
## Project summary 
An intelligent classifier has been developed, capable of differentiating between social network posts with and without suicidal tendencies, in order to prevent suicide in social networks. 
Once the model was developed, it was integrated into this application, allowing it to be tested with real Twitter posts. 
With the software, users can choose the Twitter accounts they want to analyze by adding them to a list. Once satisfied with the selected users, they can initiate the analysis process, which will extract, process, and classify the latest posts from these accounts, ultimately displaying the results in an easily navigable table.

The classifier used in this application is the product of several tests to find the model with the highest performance in classifying suicidal posts. 
This classifier has achieved the highest performance with an F-measure of 0.963. The model has been trained using this dataset (https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch) and utilizes a combination of lexicons and Word2Vec for data processing, along with the Logistic Regression algorithm for the final classification.

## How to Install and Run the Project
### Guide using executable
Download the code from the file SuicidePreventionApp_v1.0.0.zip (under the Releases section). After extracting the program from the .zip file, double-click on the SuicidePreventionApp.exe file, the one with a star icon, or search for SuicidePreventionApp in the search bar. Please note that after clicking on SuicidePreventionApp, a terminal (Mac) or command prompt (Windows) will open. The application may take 10-20 seconds to initialize, depending on the speed of your computer.
### Guide using code
To run the application using the code, it is necessary to have the libraries on which this software depends installed.
#### Dependencies
- pandas
- time
- selenium
- webdriver_manager
- nltk
- gensim
- PyQt5
- tensorflow
- os
- sys
- spacy
- queue
- re
- platform
- glob
To install a library, execute the following command in your terminal:
```
pip install <library name>
```
Once all the necessary libraries are installed, you can download the code for SuicidePreventionAPP from the green button that says "<> Code", choosing the download zip option. After extracting the program from the .zip file, enter the folder and right-click to open the options. In the options, choose "Open Terminal". In the terminal, type the following command and execute it. 
```
python SuicidePreventionApp.py
```
Once executed, the application will start, which may take 2-10 seconds depending on your computer's speed.
