# Suicide Prevention APP
## Project summary 
An intelligent classifier has been developed, capable of differentiating between social network posts with and without suicidal tendencies, in order to prevent suicide in social networks. 
Once the model was developed, it was integrated into this application, allowing it to be tested with real Twitter posts. 
With the software, users can choose the Twitter accounts they want to analyze by adding them to a list. Once satisfied with the selected users, they can initiate the analysis process, which will extract, process, and classify the latest posts from these accounts, ultimately displaying the results in an easily navigable table.

The classifier used in this application is the product of several tests to find the model with the highest performance in classifying suicidal posts. 
This classifier has achieved the highest performance with an F-measure of 0.963. The model has been trained using this dataset (https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch) and utilizes a combination of lexicons and Word2Vec for data processing, along with the Logistic Regression algorithm for the final classification.

## How to Install and Run the Project
Download the code from the file SuicidePreventionApp_v1.0.0.zip (under the Releases section). After extracting the program from the .zip file, double-click on the SuicidePreventionApp.exe file, the one with a star icon, or search for SuicidePreventionApp in the search bar. Please note that after clicking on SuicidePreventionApp, a terminal (Mac) or command prompt (Windows) will open. The application may take 10-20 seconds to initialize, depending on the speed of your computer.

