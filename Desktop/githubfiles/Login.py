from tkinter import *

import mysql.connector


class Login:
    def __init__(self):


        self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='tinder3')
        self.mycursor = self.conn.cursor()

        self.root = Tk()
        self.root.title("LOGIN")
        self.root.minsize(250, 350)
        self.frame=Frame(self.root)
        self.frame.pack()
        self.frame2 = Frame(self.root)
        self.frame2.pack()
        self.bottomframe=Frame(self.root)
        self.bottomframe.pack(side=BOTTOM)


        self.email_label = Label(self.frame, text='Enter email')
        self.email_label.pack(side=LEFT)

        self.email_input = Entry(self.frame)
        self.email_input.pack(side=LEFT)

        self.password_label = Label(self.frame2, text='Enter password')
        self.password_label.pack(side=LEFT)

        self.password_input = Entry(self.frame2)
        self.password_input.pack(side=LEFT)

        self.button = Button(self.root, text='LOGIN', command=lambda: self.perform())
        self.button.pack()

        self.result = Label(self.root, text='', fg='red')
        self.result.pack()

        self.notmember_label = Label(self.bottomframe, text='not a member?')
        self.notmember_label.pack()

        self.button2 = Button(self.bottomframe, text='register', command=lambda: self.reg())
        self.button2.pack()
        self.root.mainloop()

    def perform(self):

        email = self.email_input.get()
        password = self.password_input.get()

        self.mycursor.execute(
            """SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
        user_list = self.mycursor.fetchall()
        #print(user_list[0][0])
        if len(user_list) > 0:
            self.result.configure(text='welcome')
            self.current_user_id = user_list[0][0]

            self.root3 = Tk()
            self.root3.title("user menu")


            self.display_label = Label(self.root3,
                                       text="""how can i help u?
                                        enter 1 to view all users ,
                                        enter 2 to view friend proposals,
                                        enter 3 to view friend requests
                                        enter 4 to view friends
                                        enter anything else to log out""")
            self.display_label.pack()

            self.display_input = Entry(self.root3)
            self.display_input.pack()

            self.submit = Button(self.root3, text='submit', command=lambda: self.usermenu())
            self.submit.pack()

            self.stat=Label(self.root3,text="logged in",fg='red')
            self.stat.pack()

            self.root3.mainloop()
        else:self.current_user_id=0

    def reg(self):
        self.root2 = Tk()
        self.root2.title("LOGIN")
        self.root2.minsize(250, 350)
        self.root2.maxsize(250, 350)
        self.name_label = Label(self.root2, text='Enter name')
        self.name_label.pack()

        self.name_input = Entry(self.root2)
        self.name_input.pack()

        self.password_label = Label(self.root2, text='Enter password')
        self.password_label.pack()

        self.password_input = Entry(self.root2)
        self.password_input.pack()

        self.email_label = Label(self.root2, text='Enter email')
        self.email_label.pack()

        self.email_input = Entry(self.root2)
        self.email_input.pack()

        self.age_label = Label(self.root2, text='Enter age')
        self.age_label.pack()

        self.age_input = Entry(self.root2)
        self.age_input.pack()

        self.city_label = Label(self.root2, text='Enter city')
        self.city_label.pack()

        self.city_input = Entry(self.root2)
        self.city_input.pack()

        self.gender_label = Label(self.root2, text='Enter gender')
        self.gender_label.pack()

        self.gender_input = Entry(self.root2)
        self.gender_input.pack()

        self.button3 = Button(self.root2, text='register', command=lambda: self.register())
        self.button3.pack()

        self.result2 = Label(self.root2, text='', fg='red')
        self.result2.pack()

        self.root2.mainloop()

    def register(self):
        name = self.name_input.get()

        email = self.email_input.get()

        password = self.password_input.get()
        age = self.age_input.get()
        city = self.city_input.get()
        gender = self.gender_input.get()
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
        similar_email_list = self.mycursor.fetchall()
        if (len(similar_email_list) == 0):

            self.mycursor.execute(
                """INSERT INTO `users`(`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(
                    name, email, password, gender, age, city))
            self.conn.commit()

            self.result2.configure(text="successfull")
            self.__init__()
        else:
            self.result2.configure(text="enter different email")


    def usermenu(self):
        choice = self.display_input.get()
        if choice == '1':
            self.view_users()
        elif choice == '2':
            self.view_proposals()
        elif choice == '3':
            self.view_requests()
        elif choice == '4':
            self.view_matches()
        else:
            self.current_user_id=0
            self.stat.configure(text='logged out successfully')
            self.__init__()
            
            

    def view_users(self):
        if self.current_user_id>0:
            self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}' """.format(self.current_user_id))
            all_users_list = self.mycursor.fetchall()
            #print(all_users_list)
            self.wholeuserlist = Label(self.root3, text="USERS ARE:").pack()
            for i in all_users_list:
                self.frame2 = Frame(self.root3)
                self.frame2.pack()
                self.userid=Label(self.frame2,text=i[0])
                self.userid.pack(side=LEFT)

                self.username = Label(self.frame2, text=i[1])
                self.username.pack(side=LEFT)
                self.usergender= Label(self.frame2, text=i[4])
                self.usergender.pack(side=LEFT)
                self.userage = Label(self.frame2, text=i[5])
                self.userage.pack(side=LEFT)
                self.usercity = Label(self.frame2, text=i[6])
                self.usercity.pack(side=LEFT)

            self.button4 = Button(self.root3, text='send friend request', command=lambda: self.propose())
            self.button4.pack()
    def propose(self):
        self.root4 = Tk()
        self.root4.title("send friend request")
        self.root4.minsize(250, 350)
        self.root4.maxsize(250, 350)
        self.julietid_label = Label(self.root4, text='Enter id')
        self.julietid_label.pack()

        self.julietid_input = Entry(self.root4)
        self.julietid_input.pack()



        self.button5 = Button(self.root4, text='send friend request', command=lambda: self.proposal())
        self.button5.pack()

        self.result3 = Label(self.root4, text='', fg='red')
        self.result3.pack()

        self.root4.mainloop()



    def proposal(self):
        julietid = self.julietid_input.get()
        self.mycursor.execute("""SELECT * FROM `proposals` WHERE `romeo_id` LIKE '{}' AND `juliet_id` LIKE '{}'""".format(
            self.current_user_id, julietid))
        similar_propose_list = self.mycursor.fetchall()
        if len(similar_propose_list) > 0:
            self.result3.configure(text="send request to someone else")
        else:
            self.mycursor.execute(
                """INSERT INTO `proposals`(`proposal_id`,`romeo_id`,`juliet_id`) VALUES (NULL,'{}','{}')""".format(
                    self.current_user_id, julietid))

            self.conn.commit()

            self.result3.configure(text="successfull")









    def view_proposals(self):
        if self.current_user_id>0:
            self.mycursor.execute(
                """SELECT * FROM `proposals`  p JOIN `users` u ON p.`juliet_id`=u.`user_id` WHERE p.`romeo_id` LIKE '{}'""".format(
                    self.current_user_id))
            proposed_users_list = self.mycursor.fetchall()
            #print(proposed_users_list)

            self.julietlist = Label(self.root3,text="requests sent by you:").pack()

            for i in proposed_users_list:
                self.frame2 = Frame(self.root3)
                self.frame2.pack()
                self.userid = Label(self.frame2, text=i[4])
                self.userid.pack(side=LEFT)

                self.username = Label(self.frame2, text=i[5])
                self.username.pack(side=LEFT)
                self.usergender = Label(self.frame2, text=i[7])
                self.usergender.pack(side=LEFT)
                self.userage = Label(self.frame2, text=i[8])
                self.userage.pack(side=LEFT)
                self.usercity = Label(self.frame2, text=i[9])
                self.usercity.pack(side=LEFT)


    def view_requests(self):
        if self.current_user_id>0:
            self.mycursor.execute(
                """SELECT * FROM `proposals`  p JOIN `users` u ON p.`romeo_id`=u.`user_id` WHERE p.`juliet_id` LIKE '{}'""".format(
                    self.current_user_id))
            requested_users_list = self.mycursor.fetchall()
            # print(requested_users_list)
            self.romeolist = Label(self.root3, text="friend requests for you:").pack()
            for i in requested_users_list:
                self.frame2 = Frame(self.root3)
                self.frame2.pack()
                self.userid = Label(self.frame2, text=i[4])
                self.userid.pack(side=LEFT)

                self.username = Label(self.frame2, text=i[5])
                self.username.pack(side=LEFT)
                self.usergender = Label(self.frame2, text=i[7])
                self.usergender.pack(side=LEFT)
                self.userage = Label(self.frame2, text=i[8])
                self.userage.pack(side=LEFT)
                self.usercity = Label(self.frame2, text=i[9])
                self.usercity.pack(side=LEFT)



    def view_matches(self):
        if self.current_user_id>0:
            self.mycursor.execute(
                """SELECT `juliet_id` FROM `proposals`WHERE `juliet_id` IN(SELECT `romeo_id` FROM `proposals` WHERE `juliet_id` LIKE '{}')AND `romeo_id` LIKE '{}'""".format(
                    self.current_user_id, self.current_user_id))

            match_list = self.mycursor.fetchall()
            self.romeolist = Label(self.root3, text="YOUR MATCHES ARE:").pack()
            if len(match_list) > 0:
                for i in match_list:
                    # if we print i we print the tuples individually but i[0] means the first ele of the tuples
                    # print(i[0])
                    current_juliet = i[0]
                    self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` LIKE '{}'""".format(current_juliet))
                    juliet_profile = self.mycursor.fetchall()
                    # print(juliet_profile)
                    for i in juliet_profile:
                        self.frame2 = Frame(self.root3)
                        self.frame2.pack()
                        self.userid = Label(self.frame2, text=i[0])
                        self.userid.pack(side=LEFT)

                        self.username = Label(self.frame2, text=i[1])
                        self.username.pack(side=LEFT)
                        self.usergender = Label(self.frame2, text=i[4])
                        self.usergender.pack(side=LEFT)
                        self.userage = Label(self.frame2, text=i[5])
                        self.userage.pack(side=LEFT)
                        self.usercity = Label(self.frame2, text=i[6])
                        self.usercity.pack(side=LEFT)
                        self.printstatus=Label(self.frame2,text="match found").pack()


user=Login()
