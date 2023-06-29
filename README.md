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

## User manual
The first visible screen of the application is the welcome screen in English, shown below. This is the welcoming screen where the user can read a brief explanation about the usage of the application and switch the language to Spanish if preferred. Once the user is ready, they can press the bottom button to start, which will take them to the classifier screen.

![Welcome](https://github.com/luciarguezsant/SuicidePreventionAPP/assets/96202939/79f300e8-611b-4bc4-a5c5-fb5c9b0fe12c)

Once the user has decided to start, they can proceed to the classifier screen, which is shown in the following image. Here, the user can enter the Twitter account identifiers they want to analyze and add them to the list. Additionally, they also have the option to automatically add test accounts with the "Add test accounts" button. While choosing the accounts to analyze, it is possible to remove a selected account or clear the entire list using the blue buttons "Delete account" and "Empty list". Once the user is satisfied with the list, they can press the "Analyce accounts" button, which will launch a new execution thread to extract, process, and classify the posts from the chosen accounts. Once this process is complete, the results will be displayed on the corresponding screen.

At the bottom of the classifier screen, there is a "Go to results" button that takes you to the results screen. However, without having analyzed anything, this screen will be empty.

![Classifier](https://github.com/luciarguezsant/SuicidePreventionAPP/assets/96202939/0e8e1fdc-5230-4bf1-b802-a455b0deeeee)

In the following image, the classifier screen can be observed, showing the appearance of this window once the analysis execution has been launched. The button to view the results disappears, and in its place, a progress bar appears indicating the progress level of the operation. The "Stop Analysis" button is also shown, which will terminate the operation if the user wishes to stop it or has made a mistake.

![Analyzing](https://github.com/luciarguezsant/SuicidePreventionAPP/assets/96202939/2cb5ba66-1e65-4994-8b9a-2f6b475d826e)

Once the analysis execution is completed, the results are added to a 3-column table on the results screen. The results screen features a large table where the first column displays the user to whom the tweet belongs, the second column shows the analyzed tweet, and the third column presents the classification result obtained by the classifier. Some entries, marked with an orange star, have two user identifiers. This is because they are retweeted tweets, where the first identifier corresponds to the analyzed account that retweeted the tweet, and the second identifier represents the original account that wrote the post. The entry marked with a green star is a normal post written by the user themselves.

In this window, it is possible to review the posts and their final classifications. When the user is finished, they can continue classifying more user posts by clicking on the "Continue classifying" button, which will not modify the table. If the user decides to analyze more accounts, the results will be added to the table without deleting the previous ones.

![Results](https://github.com/luciarguezsant/SuicidePreventionAPP/assets/96202939/10143031-8c86-4ae8-a437-d34b862a7875)

If the user prefers to clear the table, they can do so by clicking the "Empty table" button. This will open a dialog to ensure that they definitely want to empty all the entries in the table.

![Delete](https://github.com/luciarguezsant/SuicidePreventionAPP/assets/96202939/fd115cde-b926-4644-9674-302e7b2570c6)

