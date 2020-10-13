from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# helper gui python codes
import login
import xoption
import email_gui

# for imap
import email
import os
import webbrowser
from imapclient import IMAPClient
import pickle
import datetime



class UI_login(login.Ui_email, QtWidgets.QMainWindow, QtWidgets.QDialog):
    def __init__(self, imap_class):
        super().__init__()
        self.imap = imap_class



    def buttons(self):
        # to set function of quit button in file menu
        self.actionQuit.triggered.connect(lambda : self.logout())

        # for signin button
        self.signin_btn.clicked.connect(lambda: self.login())

    def login(self):
        server_name = self.server_name.text()
        email = self.Email_edit.text()
        passwd = self.Pass_edit.text()

        if (server_name != "" and email != "" and passwd != ""):
            response = self.imap.login(email, passwd, server_name)
            self.Email_edit.setText("")
            self.Pass_edit.setText("")

            if response:
                db ={}
                db["email"]  = email
                db["pswd"]   = passwd
                db["server"] = server_name

                credential_file = open('.credentials', 'wb')
                pickle.dump(db, credential_file)
                credential_file.close()
                # self.signin_widget.setVisible(False)
                self.quit_this_window()

            else:
                self.warning_label.setText("Signin Failed, Try again")

        else:
            if server_name == "":
                self.warning_label.setText("Server field is Mandatory")

            elif email == "":
                self.warning_label.setText("Email field is Mandatory")

            else:
                self.warning_label.setText("Enter your password to continue")


    def quit_this_window(self):
        QtCore.QCoreApplication.instance().quit()

    def logout(self):
        # self.imap.logout()
        sys.exit()

    def check_logined(self):
        try:
            dbfile = open('.credentials', 'rb')
            db = pickle.load(dbfile)
            temp_email = db["email"]
            temp_pswd  = db["pswd"]
            temp_srvvr = db["server"]
            if ( temp_email != "" and temp_pswd != "" and temp_srvvr != ""):
                print("user exsits logging in..!!\n")
                self.imap.login(temp_email, temp_pswd, temp_srvvr)
                dbfile.close()
                return 1
                # QtCore.QCoreApplication.instance().quit()
                # self.quit_this_window()
            else:
                return 0
                pass

        except:
            file = open(".credentials","w+")
            file.close()
            return 0


class UI_main(xoption.Ui_MainWindow, QtWidgets.QMainWindow, QtWidgets.QDialog):
    def __init__(self, imap_class):
        super(UI_main, self).__init__()
        self.imap = imap_class


    def initialiser(self):
        self.change_window_name(self.imap.email)
        # initialising folders list
        self.folders = self.imap.list_folders()
        self.folder_listview.clear()

        for f in self.folders:
            self.folder_listview.addItem(f[-1])

        self.folder_listview.itemClicked.connect(self.folder_clicked)

    def listener(self):
        # liteing for menubar items
        self.actionExit.triggered.connect(sys.exit)
        self.logout.triggered.connect(self.logout_thisWindow)
        self.another_account.triggered.connect(self.logout_session)
        self.actionDelete.triggered.connect(self.delete_folder)
        self.actionDelete_Mail.triggered.connect(self.delete_email)

        # setting listeners for style view
        self.actionMotif.triggered.connect(lambda: self.style_choice("Fusion"))
        self.actionWindowsvista.triggered.connect(lambda: self.style_choice("Windowsvista"))
        self.actionCleanlooks.triggered.connect(lambda: self.style_choice("Cleanlooks"))
        self.actionPlastique.triggered.connect(lambda: self.style_choice("Plastique"))
        self.actionCde.triggered.connect(lambda: self.style_choice("cde"))
        self.actionWindows.triggered.connect(lambda: self.style_choice("Windows"))

        # listener for comboBox
        self.comboBox.activated[str].connect(self.search_choice)
        # listener for go button
        self.gobtn.clicked.connect(self.start_search)

        # listener for add button
        self.addbtn.clicked.connect(lambda: self.add_folder())

    def style_choice(self, text):
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))

    def search_choice(self, text):
        self.search_choice_type = text

    def start_search(self):
        choice_selected = self.search_choice_type
        parameter = self.search_input.text()

        if (choice_selected == "Seen"):
            messages = self.imap.search_mails("SEEN", "")
            print("Your choice is => ", choice_selected)

        elif (choice_selected == "Unseen"):
            messages = self.imap.search_mails("UNSEEN", "")
            print("Your choice is => ", choice_selected)

        elif (choice_selected == "Mail From"):
            messages = self.imap.search_mails("FROM", parameter)
            print("Your choice is => ", choice_selected)

        elif (choice_selected == "Deleted"):
            messages = self.imap.search_mails("DELETED", "")
            print("Your choice is => ", choice_selected)

        elif (choice_selected == "Since"):
            datelist = parameter.split("/")
            mail_date = datetime.date(int(datelist[0]), int(datelist[1]), int(datelist[2]))
            messages = self.imap.search_mails("SINCE", mail_date)
            print("Your choice is => ", choice_selected)

        elif (choice_selected == "Text"):
            messages = self.imap.search_mails("TEXT", parameter)
            print("Your choice is => ", choice_selected)

        elif (choice_selected == "Subject"):
            messages = self.imap.search_mails("SUBJECT", parameter)
            print("Your choice is => ", choice_selected)

        self.emails_listview.clear()
        self.folder_label.setText(choice_selected)
        if messages != None:
            for msgid, data in messages:
                envelope = data[b'ENVELOPE']
                email_item = 'ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date)
                self.emails_listview.insertItem(0, email_item)
                print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))
        else:
            print("No Mails")

        self.emails_listview.itemClicked.connect(self.mail_window)


    def logout_thisWindow(self):
        os.execv(sys.executable, ['python'] + sys.argv)

    def logout_session(self):
        db ={}
        db["email"]  = ""
        db["pswd"]   = ""
        db["server"] = ""

        credential_file = open('.credentials', 'wb')
        pickle.dump(db, credential_file)
        credential_file.close()
        os.execv(sys.executable, ['python'] + sys.argv)


    def folder_clicked(self,item):
        self.current_folder = item
        self.folder_label.setText(item.text())
        self.emails_listview.clear()
        print("folder clicked",item.text())
        messages = self.imap.list_mails(item.text())


        for msgid, data in messages:
            envelope = data[b'ENVELOPE']
            email_item = 'ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date)
            self.emails_listview.insertItem(0, email_item)
            print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))

        self.emails_listview.itemClicked.connect(self.mail_window)

    def add_folder(self):
        folder_name = self.add_folder_edit.text()
        self.add_folder_edit.setText("")
        self.imap.createFolder(folder_name)
        self.initialiser()

    def delete_folder(self):
        self.emails_listview.clear()
        self.imap.deleteFolder(self.current_folder.text())
        self.initialiser()
        self.folder_label.setText("Folders")
        self.search_input.setText("")

    def delete_email(self):
        self.emails_listview.clear()
        self.imap.deleteEmail(self.mail_id_number)
        print('done, Mail deleted successfully..!!')
        self.folder_clicked(self.current_folder)
        self.search_input.setText("")


    def mail_window(self, mail_item):
        print("mail clicked  => ", mail_item.text())
        id = mail_item.text().split("#")[1].split(":")[0]
        self.mail_id_number = id
        print(id)

        # getting those values
        fpath, data_body, to, mail_from, mail_date, mail_subject = self.imap.fetch_email_content(id)

        self.Email_window(fpath, data_body, to, mail_from, mail_date, mail_subject)


# This is portion of Controlling Email mainwindow: ==> ***Start***
    def Email_window(self, fpath, body, _to, _from, _date, _subject):
        file = open(fpath, 'rb')
        self._mail = email_gui.Ui_MainWindow()
        self._mail.setupUi(QtWidgets.QMainWindow())
        self._mail._show()
        self._mail._change_window_name(_subject)

        self.Email_window_configuration(fpath, body, _to, _from, _date)


    def Email_window_configuration(self, fpath, body, _to_configure, _from_configure, _date_configure):
        # setting the desired vaues in mail labels:
        self._mail.label_from.setText("From : " + _from_configure)
        self._mail.label_other.setText("Date : " + _date_configure)

        # making text edit as view only
        self._mail.email_content.setReadOnly(True)
        # print(file.read().decode())

        # setting listeners for file-menu options:
        self._mail.email_content.setText(body)
        self._mail.actionQuit.triggered.connect(self._mail._quit)
        self._mail.action_browser.triggered.connect(lambda: self.open_in_browser(fpath))
        self._mail.action_folder.triggered.connect(lambda: self.open_folder(fpath))


    def open_in_browser(self,file_path):
        webbrowser.open(file_path)

    def open_folder(self, folder_path):
        print(folder_path)
        # os.system("nautilus " + folder_path)

# ***Ending of Email mainwindow***


class imap:
    def __init__(self):
        try:
            dbfile = open('.credentials', 'rb')
            db = pickle.load(dbfile)
            temp_server = db["server"]
            if (temp_server == ""):
                self.server_fail_flag = 1                                               # declaring that server object of imap is not initialised
                pass

            else:
                try:
                    self.server = IMAPClient(temp_server, use_uid=True)
                    self.server_fail_flag = 0
                except:
                    self.server_fail_flag = 1                                           # declaring that server object of imap is not initialised
                    print("Couldn't able to sign in. Please try again with valied credentials")

        except:
            self.server_fail_flag = 1                                                   # declaring that server object of imap is not initialised
            file = open(".credentials","w+")
            file.close()


    def login(self, id, passwd, server):
        self.server_name = server
        self.email  = id
        self.passwd = passwd
        try:
            if (self.server_fail_flag == 1):
                self.server = IMAPClient(self.server_name, use_uid=True)
            self.server.login(self.email, self.passwd)
            return 1
            print("Login successful")
        except :
            return 0


    def logout(self):
        print("Logged out")
        self.server.logout()

    def list_folders(self):
        print("LIST OF FOLDERS")
        folders = self.server.list_folders()
        for i in folders:
            print(i[-1])

        return folders

        print("")
        print(server.get_gmail_labels(messages))

    def createFolder(self, folderName):
        self.server.create_folder(folderName)
        print("Folder named - %s - is created successfully..." % folderName)

    def deleteFolder(self, folderName):
        self.server.delete_folder(folderName)

    def deleteEmail(self, messages):
        self.server.delete_messages(messages)

    def list_mails(self, folder_name):
        select_info = self.server.select_folder(folder_name)
        print('%d messages in %s' % (select_info[b'EXISTS'], folder_name))

        # messages = server.search(['FROM', 'best-friend@domain.com'])
        messages = self.server.search(['ALL'])
        # messages = self.server.sort(['ARRIVAL'])
        print("%s messages from %s" % (len(messages), folder_name))

        fetched_msgs = self.server.fetch(messages, ['ENVELOPE']).items()

        return fetched_msgs

    def search_mails(self, catagory, parameter):
        if (catagory in ["FROM", "TEXT", "SINCE", "SUBJECT"]):
            print([catagory, parameter])
            messages = self.server.search([catagory, parameter])
            print("%s messages from Search catagory -> %s" % (len(messages), catagory))

            fetched_msgs = self.server.fetch(messages, ['ENVELOPE']).items()
            print("fetched Messages are ", fetched_msgs)
            return fetched_msgs

        else:
            print([catagory])
            messages = self.server.search([catagory])
            print(messages)
            print("%s messages from Search catagory -> %s" % (len(messages), catagory))

            fetched_msgs = self.server.fetch(messages, ['ENVELOPE']).items()
            print("fetched Messages are ", fetched_msgs)
            return fetched_msgs

    def fetch_email_content(self, msg_id):
        for msgid, data in self.server.fetch(msg_id, 'RFC822').items():
            # print("\nMESSAGE", msgid)
            # print("\nDATA IS => \n", data)
            # envelope = data[b'ENVELOPE']
            msg = email.message_from_bytes(data[b'RFC822'])
            # print(msgid, email_message.get('From'), email_message.get('Subject'))
            # print(email_message.get('To'), email_message.get('body'))
            subject = msg.get('Subject')
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                        print(body)
                    elif "attachment" in content_disposition:
                        # download attachment
                        filename = part.get_filename()
                        if filename:
                            if not os.path.isdir(subject):
                                # make a folder for this email (named after the subject)
                                os.mkdir(subject)
                            filepath = os.path.join(subject, filename)
                            # download attachment and save it
                            open(filepath, "wb").write(part.get_payload(decode=True))
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    # print only text email parts
                    print(body)

            if content_type == "text/html":
                # if it's HTML, create a new HTML file and open it in browser
                if not os.path.isdir(subject):
                    # make a folder for this email (named after the subject)
                    os.mkdir(subject)
                filename = "{}.html".format(subject[:50])
                filepath = os.path.join(subject, filename)
                # write the file
                open(filepath, "w").write(body)

            # some data about mail
            to        = msg.get("To")
            mail_from = msg.get("From")
            mail_date = msg.get("Date")
            mail_subject = msg.get("Subject")
            print("To   =>", to)
            print("From =>", mail_from)
            print("Date =>", mail_date)
            print("="*100)

            # returning the useful values
            return (filepath, body, to, mail_from, mail_date, mail_subject)


if __name__ == "__main__":
    # instantiating imap class to be user at all places
    global_imap = imap()

    # configuring to start login window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_login(global_imap)
    ui.setupUi(MainWindow)
    login_status = ui.check_logined()                       # checks if user is loged in earlier or not and directly
    if not login_status:                                    # logs it into main window if logged earlier.
        MainWindow  .show()
        ui.buttons()
        app.exec_()
        MainWindow.close()
    else:
        MainWindow.close()
        pass

    print("\nstarting main window\n")

    # starting mainwindow
    app2 = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui_main = UI_main(global_imap)
    ui_main.setupUi(MainWindow2)
    ui_main.initialiser()
    ui_main.listener()
    MainWindow2.show()
    app2.exec_()
