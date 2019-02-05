import mysql.connector
class Tinder:
    def __init__(self):
        #connect to db
        self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='tinder3')
        self.mycursor=self.conn.cursor()
        self.program_menu()
    #menu
    def program_menu(self):
        program_input=input(""" hi what would u llike to do?
        1.enter 1 to create an acc
        2.enter 2 to login
        3.anything else to exit""")
        if program_input=='1':
            self.register()
        elif program_input=='2':
            self.login()
        else:
            print('bye')
    #register
    def register(self):
        name=input("NAME")
        email=input("EMAIL")
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
        similar_email_list=self.mycursor.fetchall()
        if(len(similar_email_list)>0):
            email=input("enter diff............user already exists!!")


        password=input("password")
        gender=input("GENDER")
        age=input("AGE")
        city=input("CITY")

        self.mycursor.execute(""" INSERT INTO `users` (`userid`,`name`,`email`,`password`,`gender`,`age`,`city`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(name,email,password,gender,age,city))
        self.conn.commit()
        print("reg successfull")
        self.program_menu()
    def login(self):
        email=input("enter email")
        password=input("enter password")
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
        user_list = self.mycursor.fetchall()
        #print(user_list)
        counter = 0
        for i in user_list:
            counter += 1
            current_user = i
        if counter > 0:

            print("successful")
            self.current_user_id = current_user[0]
            print(self.current_user_id)
            self.user_menu()
        else:
            print("incorrect")
            self.program_menu()
    def user_menu(self):
        user_input=input("""how can i help u?
        1.enter 1 to view all users
        2.enter 2 to view proposal
        3.enter 3 to view request
        4.enter 4 to view matches
        5.enter anything to log out""")
        if user_input=='1':
            self.view_users()
        elif user_input=='2':
            self.view_proposal()
        elif user_input=='3':
            self.view_request()
        elif user_input=='4':
            self.view_matches()
        else:
            print("bye")
            self.current_user_id=0
    def view_users(self):
        self.mycursor.execute("""SELECT * FROM `users` WHERE `userid` NOT LIKE '{}' """.format(self.current_user_id))
        all_users_list=self.mycursor.fetchall()
        #print(all_users_list)

        for i in all_users_list:
            print(i[0],'  |  ',i[1],'  |  ',i[4],' | ',i[5],' | ',i[6])
            print("------------------------------------------------------")
        julietid=input("enter the id of the user whom u want to propose")
        self.mycursor.execute("""SELECT * FROM `proposals` WHERE `romeoid` LIKE '{}' AND `julietid` LIKE '{}'""".format(self.current_user_id,julietid))
        similar_propose_list=self.mycursor.fetchall()
        if len(similar_propose_list)>0:
            julietid=input("propose someoneone else")
        self.propose(self.current_user_id,julietid)
    def propose(self,romeoid,julietid):
        self.mycursor.execute("""INSERT INTO `proposals` (`proposalid`,`romeoid`,`julietid`) VALUES (NULL,'{}','{}')""".format(romeoid,julietid))
        self.conn.commit()
        print("proposal successfull")
        self.user_menu()
    def view_proposal(self):
        print("the juliet id for u are:")

        self.mycursor.execute("""SELECT * FROM `proposals`  p JOIN `users` u ON p.`julietid`=u.`userid` WHERE p.`romeoid` LIKE '{}'""".format(self.current_user_id))
        proposed_users_list = self.mycursor.fetchall()
        print(proposed_users_list)

        for i in proposed_users_list:
            print( i[4], '  |  ', i[5], ' | ', i[7], ' | ', i[8],'|',i[9])
            print("------------------------------------------------------")
        self.user_menu()
    def view_request(self):
        self.mycursor.execute(
            """SELECT * FROM `proposals`  p JOIN `users` u ON p.`romeoid`=u.`userid` WHERE p.`julietid` LIKE '{}'""".format(
                self.current_user_id))
        requested_users_list = self.mycursor.fetchall()
        #print(requested_users_list)
        for i in requested_users_list:
            print(i[4], '  |  ', i[5], ' | ', i[7], ' | ', i[8], '|', i[9])
            print("------------------------------------------------------")
        self.user_menu()
    def view_matches(self):
        self.mycursor.execute("""SELECT `julietid` FROM `proposals`WHERE `julietid` IN(SELECT `romeoid` FROM `proposals` WHERE `julietid` LIKE '{}')AND `romeoid` LIKE '{}'""".format(self.current_user_id,self.current_user_id))
        
        match_list=self.mycursor.fetchall()
        if len(match_list)>0:
            for i in match_list:
                #if we print i we print the tuples individually but i[0] means the first ele of the tuples
                #print(i[0])
                current_juliet=i[0]
                self.mycursor.execute("""SELECT * FROM `users` WHERE `userid` LIKE '{}'""".format(current_juliet))
                juliet_profile=self.mycursor.fetchall()
                #print(juliet_profile)
                for i in juliet_profile:
                    print(i[0],'|',i[1],'|',i[4],'|',i[5],'|',i[6])
                    print("--------------------------------------------------------")
                print("match found")




        else:
            print("sorry")
        self.user_menu()
user=Tinder()
#only login users,logout
#done email chk,repeat proposal
