import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFontDatabase, QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem, QHeaderView
import tensorflow as tf
import os
import sys
file_dir = os.path.join(os.getcwd(), "SEANCE-master")
sys.path.append(file_dir)
import SEANCE_1_2_0


class WelcomeWindow(QDialog):
    def __init__(self):
        super().__init__()
        path = os.path.join("Interface","Welcome.ui")
        loadUi(path, self)
        self.startButton.clicked.connect(self.go_to_app)
        self.lenguageComboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.label_4.setPixmap(QPixmap("logo.png"))
    def go_to_app(self):
        widget.setCurrentIndex(windows["Classifier"])

    def on_combobox_changed(self, value):
        if value == "Español":
            widget.setCurrentIndex(windows["Bienvenido"])
            self.lenguageComboBox.setCurrentIndex(0)


class BienvenidoWindow(QDialog):
    def __init__(self):
        super().__init__()
        path = os.path.join("Interface", "Bienvenido.ui")
        loadUi(path, self)
        self.startButton.clicked.connect(self.go_to_app)
        self.lenguageComboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.label_4.setPixmap(QPixmap("logo.png"))
    def go_to_app(self):
        widget.setCurrentIndex(windows["Clasificador"])

    def on_combobox_changed(self, value):
        if value == "English":
            widget.setCurrentIndex(windows["Welcome"])
            self.lenguageComboBox.setCurrentIndex(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        path = os.path.join("Interface", "appInterface.ui")
        loadUi(path, self)
        self.addButton.clicked.connect(self.add_account)
        self.addTestAccButton.clicked.connect(self.add_test_accounts)
        self.backButton.clicked.connect(self.go_back)
        self.lenguageComboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.accountLineEdit.returnPressed.connect(self.add_account)
        self.delAccountButton.clicked.connect(self.delete_account)
        self.delAllButton.clicked.connect(self.delete_all_accounts)
        self.setAccounts = set()
        self.repetidoLabel.setText("")
        self.analyzeButton.clicked.connect(self.analyze_accounts)
        self.progressBar.hide()
        self.updateLabel.hide()
        self.quitButton.hide()
        self.quitButton.clicked.connect(self.quit_analysis)
        self.goToResultsButton.clicked.connect(self.go_to_results)
        self.label_4.setPixmap(QPixmap("logo2.png"))
        self.threadHasBeenTerminated = False

    def go_back(self):
        widget.setCurrentIndex(windows["Welcome"])

    def go_to_results(self):
        widget.setCurrentIndex(windows["Results"])

    def add_account(self):
        accountID = self.accountLineEdit.text()
        if len(accountID) > 0:
            if "@"+accountID not in self.setAccounts:
                self.accountListWidget.addItem("@"+accountID)
                self.setAccounts.add("@"+accountID)
                if self.repetidoLabel != "":
                    self.repetidoLabel.setText("")
            else:
                self.repetidoLabel.setText("@"+accountID+" has already been added.")
                self.repetidoLabel.setAlignment(Qt.AlignCenter)
        self.accountLineEdit.setText("")
        self.accountLineEdit.setCursorPosition(0)
        # cursor = self.textCursor()
        # cursor.setPosition(cursor.position(), QTextCursor.KeepAnchor)
        # self.setTextCursor(cursor)

    def add_test_accounts(self):
        testAcc = ["@SuicidalExample", "@HealthyExamplee"]
        for acc in testAcc:
            if acc not in self.setAccounts:
                self.accountListWidget.addItem(acc)
                self.setAccounts.add(acc)
                if self.repetidoLabel != "":
                    self.repetidoLabel.setText("")

    def on_combobox_changed(self, value):
        if value == "Español":
            widget.setCurrentIndex(windows["Clasificador"])
            self.lenguageComboBox.setCurrentIndex(0)
            clasificador.accountListWidget.clear()
            clasificador.setAccounts.clear()
            numItems = self.accountListWidget.count()
            for x in range(numItems):
                clasificador.accountListWidget.addItem(self.accountListWidget.item(x).text())
                clasificador.setAccounts.add(self.accountListWidget.item(x).text())

    def delete_account(self):
        items = self.accountListWidget.selectedItems()
        for item in items:
            self.accountListWidget.takeItem(self.accountListWidget.row(item))
            self.setAccounts.remove(item.text())

    def delete_all_accounts(self):
        self.accountListWidget.clear()
        self.setAccounts.clear()

    def analyze_accounts(self):
        if not self.setAccounts:
            self.repetidoLabel.setText("No users added to analyze")
            self.repetidoLabel.setAlignment(Qt.AlignCenter)
        else:
            self.analyzeButton.setEnabled(False)
            self.update_progressbar(0, "Extracting data", "Extrayendo datos")
            self.goToResultsButton.hide()
            self.progressBar.show()
            self.updateLabel.show()
            self.quitButton.show()
            ventanaResults = widget.widget(windows["Results"])
            self.myThread = AnalysisThread(list(self.setAccounts))
            self.myThread.start()
            self.myThread.update_progressbar.connect(self.update_progressbar)
            self.myThread.update_table.connect(ventanaResults.add_table)
            self.myThread.finished.connect(self.open_results)

    def update_progressbar(self, val, textEn, testEs):
        self.progressBar.setValue(val)
        self.updateLabel.setText(textEn)

    def open_results(self):
        if self.threadHasBeenTerminated:
            self.threadHasBeenTerminated = False
            self.analyzeButton.setDisabled(False)
        else:
            widget.setCurrentIndex(windows["Results"])
            self.accountListWidget.clear()
            self.setAccounts.clear()
            self.progressBar.hide()
            self.updateLabel.hide()
            self.quitButton.hide()
            self.goToResultsButton.show()
            self.analyzeButton.setDisabled(False)

    def quit_analysis(self):
        if not self.myThread.isFinished():
            self.threadHasBeenTerminated = True
            self.myThread.terminate()
            self.myThread.wait()
            self.progressBar.hide()
            self.updateLabel.hide()
            self.quitButton.hide()
            self.goToResultsButton.show()

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        path = os.path.join("Interface", "appInterfazEs.ui")
        loadUi(path, self)
        self.addButton.clicked.connect(self.add_account)
        self.addTestAccButton.clicked.connect(self.add_test_accounts)
        self.backButton.clicked.connect(self.go_back)
        self.lenguageComboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.accountLineEdit.returnPressed.connect(self.add_account)
        self.delAccountButton.clicked.connect(self.delete_account)
        self.delAllButton.clicked.connect(self.delete_all_accounts)
        self.setAccounts = set()
        self.repetidoLabel.setText("")
        self.analyzeButton.clicked.connect(self.analyze_accounts)
        self.progressBar.hide()
        self.updateLabel.hide()
        self.quitButton.hide()
        self.quitButton.clicked.connect(self.quit_analysis)
        self.goToResultsButton.clicked.connect(self.go_to_results)
        self.label_4.setPixmap(QPixmap("logo2.png"))
        self.threadHasBeenTerminated = False

    def go_back(self):
        widget.setCurrentIndex(windows["Bienvenido"])

    def go_to_results(self):
        widget.setCurrentIndex(windows["Results"])

    def add_account(self):
        accountID = self.accountLineEdit.text()
        if len(accountID) > 0:
            if "@"+accountID not in self.setAccounts:
                self.accountListWidget.addItem("@"+accountID)
                self.setAccounts.add("@"+accountID)
                if self.repetidoLabel != "":
                    self.repetidoLabel.setText("")
            else:
                self.repetidoLabel.setText("@"+accountID+" has already been added.")
                self.repetidoLabel.setAlignment(Qt.AlignCenter)
        self.accountLineEdit.setText("")
        # cursor = self.textCursor()
        # cursor.setPosition(cursor.position(), QTextCursor.KeepAnchor)
        # self.setTextCursor(cursor)

    def add_test_accounts(self):
        testAcc = ["@SuicidalExample", "@HealthyExamplee"]
        for acc in testAcc:
            if acc not in self.setAccounts:
                self.accountListWidget.addItem(acc)
                self.setAccounts.add(acc)
                if self.repetidoLabel != "":
                    self.repetidoLabel.setText("")

    def on_combobox_changed(self, value):
        if value == "English":
            widget.setCurrentIndex(windows["Classifier"])
            self.lenguageComboBox.setCurrentIndex(0)
            classifier.accountListWidget.clear()
            classifier.setAccounts.clear()
            numItems = self.accountListWidget.count()
            for x in range(numItems):
                classifier.accountListWidget.addItem(self.accountListWidget.item(x).text())
                classifier.setAccounts.add(self.accountListWidget.item(x).text())

    def delete_account(self):
        items = self.accountListWidget.selectedItems()
        for item in items:
            self.accountListWidget.takeItem(self.accountListWidget.row(item))
            self.setAccounts.remove(item.text())

    def delete_all_accounts(self):
        self.accountListWidget.clear()
        self.setAccounts.clear()

    def analyze_accounts(self):
        if not self.setAccounts:
            self.repetidoLabel.setText("No hay usuarios añadidos para analizar")
            self.repetidoLabel.setAlignment(Qt.AlignCenter)
        else:
            self.analyzeButton.setEnabled(False)
            self.update_progressbar(0, "Extracting data","Extrayendo datos")
            self.goToResultsButton.hide()
            self.progressBar.show()
            self.updateLabel.show()
            self.quitButton.show()
            ventanaResults = widget.widget(windows["Results"])
            ventanaResults.lenguageComboBox.setCurrentIndex(1)
            self.myThread = AnalysisThread(list(self.setAccounts))
            self.myThread.start()
            self.myThread.update_progressbar.connect(self.update_progressbar)
            self.myThread.update_table.connect(ventanaResults.add_table)
            self.myThread.finished.connect(self.open_results)

    def update_progressbar(self, val, textEn, testEs):
        self.progressBar.setValue(val)
        self.updateLabel.setText(testEs)

    def open_results(self):
        if self.threadHasBeenTerminated:
            self.threadHasBeenTerminated = False
            self.analyzeButton.setDisabled(False)
        else:
            ventanaResults = widget.widget(windows["Results"])
            ventanaResults.lenguageComboBox.setCurrentIndex(1)
            widget.setCurrentIndex(windows["Results"])
            self.accountListWidget.clear()
            self.setAccounts.clear()
            self.progressBar.hide()
            self.updateLabel.hide()
            self.quitButton.hide()
            self.goToResultsButton.show()
            self.analyzeButton.setDisabled(False)

    def quit_analysis(self):
        if not self.myThread.isFinished():
            self.threadHasBeenTerminated = True
            self.myThread.terminate()
            self.myThread.wait()
            self.progressBar.hide()
            self.updateLabel.hide()
            self.quitButton.hide()
            self.goToResultsButton.show()

class ResultsWindow(QDialog):
    def __init__(self):
        super().__init__()
        path = os.path.join("Interface", "Results.ui")
        loadUi(path, self)
        self.backButton.clicked.connect(self.go_back)
        self.tableWidget.setColumnCount(3)
        self.continueButton.clicked.connect(self.go_back)
        self.emptyButton.clicked.connect(self.empty_table)
        self.label_4.setPixmap(QPixmap("logo2.png"))
        if self.lenguageComboBox.currentText() == "Español":
            self.label.setText("Resultados del clasificador.")
            self.label.setAlignment(Qt.AlignCenter)
            self.tableWidget.setHorizontalHeaderLabels(["Usuario", "Tweet", "Resultado clasificación"])
        else:
            self.tableWidget.setHorizontalHeaderLabels(["UserTag", "Tweet", "Classification Result"])
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView..Stretch)
        scrollbar = self.tableWidget.verticalScrollBar()
        scrollbar.setStyleSheet("QScrollBar:vertical { width: 25px; }")
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.lenguageComboBox.currentTextChanged.connect(self.change_lenguage)



    def go_back(self):
        if self.lenguageComboBox.currentText() == "Español":
            widget.setCurrentIndex(windows["Clasificador"])
        else:
            widget.setCurrentIndex(windows["Classifier"])

    def change_lenguage(self):
        if self.lenguageComboBox.currentText() == "Español":
            self.label.setText("Resultados del clasificador.")
            self.label.setAlignment(Qt.AlignCenter)
            self.tableWidget.setHorizontalHeaderLabels(["Usuario", "Tweet", "Resultado clasificación"])
            self.continueButton.setText("Continuar clasificando")
            self.emptyButton.setText("Vaciar tabla")
        else:
            self.label.setText("Classification results.")
            self.label.setAlignment(Qt.AlignCenter)
            self.tableWidget.setHorizontalHeaderLabels(["UserTag", "Tweet", "Classification Result"])
            self.continueButton.setText("Continue classifying")
            self.emptyButton.setText("Empty table")

    def add_table(self, rowResults):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        numrows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(numrows)
        self.tableWidget.setItem(numrows - 1, 0, QTableWidgetItem(rowResults[0]))
        self.tableWidget.setItem(numrows - 1, 1, QTableWidgetItem(rowResults[1]))
        self.tableWidget.setItem(numrows - 1, 2, QTableWidgetItem(rowResults[2]))
        self.tableWidget.resizeColumnsToContents()

    def empty_table(self):
        deleteDialog = DeleteTableDialog()
        deleteDialog.setModal(True)
        deleteDialog.exec()

class DeleteTableDialog(QDialog):
    def __init__(self):
        super().__init__()
        path = os.path.join("Interface", "BorrarTablaMensaje.ui")
        loadUi(path, self)
        self.setWindowTitle("Empty table")
        self.move(widget.x()+widget.width()//2-self.width()//2, widget.y()+widget.height()//2-self.height()//2)
        self.yesButton.clicked.connect(self.empty_table)
        self.noButton.clicked.connect(self.close)
        if results.lenguageComboBox.currentText() == "Español":
            self.label.setText("¿Quieres vaciar la tabla?")
            self.label.setAlignment(Qt.AlignCenter)
            self.yesButton.setText("Sí")
            self.noButton.setText("No")

    def empty_table(self):
        results.tableWidget.clear()
        results.tableWidget.setRowCount(0)
        if results.lenguageComboBox.currentText() == "Español":
            results.tableWidget.setHorizontalHeaderLabels(["Usuario", "Tweet", "Resultado clasificación"])
        else:
            results.tableWidget.setHorizontalHeaderLabels(["UserTag", "Tweet", "Classification Result"])
        self.done(0)

    def close(self):
        self.done(0)

class AnalysisThread(QThread):
    update_table = pyqtSignal(object)
    update_progressbar = pyqtSignal(int, str, str)
    def __init__(self, users):
        QThread.__init__(self)
        self.users = users

    def run(self):
        df_tweets = self.data_extraction(self.users)

        self.update_progressbar.emit(55, "All tweets extracted", "Todos los tweets extraídos")
        df_lexicons = self.process_tweets_lexicons(df_tweets, 'Tweets')
        self.update_progressbar.emit(65, "Processed with lexicons", "Procesado con léxicos")
        df_w2v = self.process_tweets_word2vec(df_tweets, 'Tweets')
        self.update_progressbar.emit(85, "Processed with Word2Vec", "Procesado con Word2Vec")
        
        del df_lexicons["filename"]
        del df_lexicons["nwords"]
        df_lexicons.reset_index(drop=True, inplace=True)
        df_w2v.reset_index(drop=True, inplace=True)
        df_procesado_final = pd.concat([df_lexicons, df_w2v], axis=1)

        # Transformar dataframe a tensorflow object
        x_test = tf.convert_to_tensor(df_procesado_final, dtype=tf.float32)

        # Cragar modelo de clasificacion Logistic Regresion Tensorflow
        save_path = os.path.join('ResultadosLogisticRegresion',
                                 'log_reg_final_100_2_0')
        log_reg_loaded = tf.saved_model.load(save_path)
        # Realizar prediccion
        test_preds = log_reg_loaded.get_predictions(x_test)
        self.update_progressbar.emit(95, "Classification done", "Clasificación terminada")

        self.update_progressbar.emit(100,  "Results generated", "Resultados generados")
        for indice, fila in df_tweets.iterrows():
            if test_preds[indice] == 0: pred = 'non-suicide'
            else: pred = 'suicide'
            items = [fila["UserTags"], fila["Tweets"], pred]
            self.update_table.emit(items)

    def data_extraction(self, usersList):
        cargaProgressBar = 10
        DRIVER_PATH = "\chromedriver_win32\chromedriver.exe"  # This path works for macos
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://twitter.com/login")

        # driver.maximize_window()  # For maximizing window
        # Log in username
        username = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']")))
        username.send_keys("SuicidePr3v3nt")
        next_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Next')]")))
        next_button.click()

        # Password
        password = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password.send_keys('Cuentadeprevencion')  # Cuentadeprevencion
        log_in = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Log in')]")))
        log_in.click()
        self.update_progressbar.emit(cargaProgressBar, "Logged in successfully", "Sesión iniciada correctamente")

        UserTags = []
        Tweets = []
        numTweetsTotales = 0
        valorCargaPorUsuario= 40//len(usersList)
        for i in range(0, len(usersList)):  # For each user
            botonLupa = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//a[@href="/explore"]')))
            botonLupa.click()
            search_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")))
            search_box.send_keys(usersList[i])
            search_box.send_keys(Keys.ENTER)
            people = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'People')]")))
            people.click()
            try:
                profile = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                         "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div"
                         "/div[3]/section/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]")))
            except Exception:
                profile = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                         "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section"
                         "/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span")))
            profile.click()
            print("Entrado en perfil de", usersList[i])
            numTweetsString = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div"
                               "/div[1]/div[1]/div/div/div/div/div/div[2]/div/div"))).text
            miles = numTweetsString.find('K Tweets')
            millones = numTweetsString.find('M Tweets')
            if miles == -1 and millones == -1:
                end = numTweetsString.find(' Tweets')
                numTweets = int(numTweetsString[:end].replace(",", ""))
                if numTweets > 30:
                    numTweets = 30
            else:
                numTweets = 30  # Max 30 tweets
            numTweetsTotales += numTweets
            scrollDistance = 0
            valorCargaPorPublicacion = valorCargaPorUsuario//numTweets
            if valorCargaPorPublicacion == 0: valorCargaPorPublicacion = 1
            while len(Tweets) < numTweetsTotales:  # While not all tweets have been extracted
                articles = WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//article[@data-testid='tweet']")))
                for article in articles:  # For each tweet available in the screen
                    try:
                        Tweet = article.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text.replace('\n',
                                                                                                                ' ')
                        UserTag = article.find_element(By.XPATH, ".//div[@data-testid='User-Name']").text.replace('\n',
                                                                                                                  ' ')
                    except NoSuchElementException:
                        if miles == -1 and millones == -1 and int(numTweetsString[:end].replace(",", "")) < 50:  # few tweets
                            numTweetsTotales -=1
                        print("Tweet sin texto o etiqueta de usuario")
                        break
                    if Tweet not in Tweets and len(Tweets) < numTweetsTotales:
                        Tweets.append(Tweet)
                        startUser = UserTag.rfind('@')
                        retweet = UserTag.find(usersList[i])
                        if retweet == -1:  # It's a retweet
                            UserTags.append(usersList[i] +" "+ UserTag[startUser:])
                        else:
                            UserTags.append(UserTag[startUser:])
                        if cargaProgressBar < 50:
                            cargaProgressBar += valorCargaPorPublicacion
                        self.update_progressbar.emit(int(cargaProgressBar), str(len(Tweets)) + " tweets extracted",
                                                     str(len(Tweets)) + " tweets extraídos")
                scrollDistance += 600
                driver.execute_script('window.scrollTo(' + str(scrollDistance - 600) + ',' + str(
                    scrollDistance) + ');')  # scroll down to get more tweets
                time.sleep(1.5)
            print("Extraídos", len(Tweets), "tweets.")

        driver.quit()
        df = pd.DataFrame(zip(UserTags, Tweets)
                          , columns=['UserTags', 'Tweets'])
        return df

    # Codigo de preprocesamiento con Word2Vec
    def process_tweets_word2vec(self, dfTweets, columnTextName):
        path = os.path.join("Word2VecModel", "Word2VecModelFinal")
        model = Word2Vec.load(path)
        dfW2V = pd.DataFrame(columns=[*range(0, 100)])

        for indice, fila in dfTweets.iterrows():
            print("Word2Vec processing: post ", indice)
            textoSinComas = fila[columnTextName].replace(",", " ").replace(".", " ")
            post = word_tokenize(textoSinComas.lower())
            primera = True
            vector_media = []
            num_palabras_inexistentes = 0
            for palabra in post:
                if palabra in model.wv:
                    if primera:
                        vector_media = model.wv.get_vector(str(palabra)).copy()
                        primera = False
                    else:
                        vector_temp = model.wv.get_vector(str(palabra))
                        i = 0
                        for valor in vector_temp:
                            vector_media[i] = vector_media[i] + valor
                            i += 1
                else:
                    num_palabras_inexistentes += 1
            num_palabras = len(post) - num_palabras_inexistentes
            vector_final = list()
            for valor in vector_media:
                vector_final.append(valor / num_palabras)
            if len(vector_final) == 100:
                dfW2V.loc[indice] = vector_final
            else:
                print("Publicacion rara en", indice, post)
                dfW2V.loc[indice] = [0] * 100
                # raise Exception("Vector de longitud erronea en indice", indice,
                #                 "con longitud", len(vector_media), "y publicacion:", textoSinComas)

        return dfW2V

    # Codigo de preprocesamiento con lexicos
    def process_tweets_lexicons(self, dfTweets, columnTextName):
        GALC = 1
        EmoLex = 1
        ANEW = 1  # 5
        SENTIC = 1
        VADER = 1
        HuLiu = 1  # 8
        GI = 1
        Lasswell = 1
        nouns = 0
        verbs = 0
        adjectives = 0  # 13
        adverbs = 0
        allWords = 1  # 15
        threeLeft = 0
        components = 1  # 17

        var_list = [0, GALC, EmoLex, ANEW, SENTIC, VADER, HuLiu,
                    GI, Lasswell, nouns, verbs, adjectives, adverbs, allWords,
                    threeLeft, components]

        df_lexicons = SEANCE_1_2_0.main(dfTweets, columnTextName, var_list)
        return df_lexicons

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = {
        "Welcome": 0,
        "Bienvenido": 1,
        "Classifier": 2,
        "Clasificador": 3,
        "Results": 4
    }
    QFontDatabase.addApplicationFont('Space_Grotesk\static\SpaceGrotesk-Bold.ttf')
    QFontDatabase.addApplicationFont('Space_Grotesk\static\SpaceGrotesk-Light.ttf')
    QFontDatabase.addApplicationFont('Space_Grotesk\static\SpaceGrotesk-Medium.ttf')
    QFontDatabase.addApplicationFont('Space_Grotesk\static\SpaceGrotesk-Regular.ttf')
    QFontDatabase.addApplicationFont('Space_Grotesk\static\SpaceGrotesk-SemiBold.ttf')
    welcome = WelcomeWindow()
    bienvenido = BienvenidoWindow()
    classifier = MainWindow()
    clasificador = VentanaPrincipal()
    results = ResultsWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.addWidget(bienvenido)
    widget.addWidget(classifier)
    widget.addWidget(clasificador)
    widget.addWidget(results)
    widget.setFixedHeight(800)
    widget.setFixedWidth(930)
    widget.setCurrentIndex(windows["Welcome"])
    widget.setWindowTitle("Suicide prevention App")
    widget.show()
    # Start the event loop.
    try: sys.exit(app.exec_())
    except:
        if hasattr(classifier, "myThread"):
            if not classifier.myThread.isFinished():
                classifier.myThread.quit()
        if hasattr(clasificador, "myThread"):
            if not clasificador.myThread.isFinished():
                clasificador.myThread.quit()
        print("Saliendo...")




