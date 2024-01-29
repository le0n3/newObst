import MySQLdb
import discord
import config
try:
    connetion = MySQLdb.connect(
        host='Skillless.mysql.pythonanywhere-services.com',
        user='Skillless',
        passwd=config.getDBPassword(),
        db='Skillless$discorde', connect_timeout=20)
    connetion.autocommit(True)

except:
    print("Bei der Verbindung mit der datenbank ist ein fehler aufgetreten ")


def NweUser( User : discord.Member):
    try:
        UserExists = f"SELECT `User_Name` FROM user WHERE User_name = '{User.id}'; "
        with connetion.cursor() as SQL_Abfrage_New_User_Check:
            SQL_Abfrage_New_User_Check.execute(UserExists)
            all = SQL_Abfrage_New_User_Check.fetchall()
            SQL_Abfrage_New_User_Check.close()
        if len(all) != 0:
            return "Dich Gibt es bereits!!"
        else:
            UserAdd = f"INSERT INTO user (`User_ID`, `User_Name`, `User_SocalCredits`) VALUES ({User.id},'{User.name}', 0);"
            with connetion.cursor() as SQL_Insert:
                SQL_Insert.execute(UserAdd)
                SQL_Insert.close()
            return "Du wurdes hinzugefügt!!"
    except Exception as e:
        SQL_Abfrage_New_User_Check.close()
        SQL_Insert.close()
        print(e)
        return "Digga Fheler oder so frag Leon"



def SocialCreditEdit(User: discord.Member, Credits):
    getcredit = f"SELECT `User_SocalCredits` FROM user WHERE `User_ID` = '{User.id}';"
    try:
        try:
            with connetion.cursor() as SQL_Abfrage:
                SQL_Abfrage.execute(getcredit)
                credit = SQL_Abfrage.fetchall()
                SQL_Abfrage.close()
            if len(credit) == 0:
                NweUser(User)
        except:
            SQL_Abfrage.close()
            return f"User ID Was infalid: {User.id}"
        try:
            credit = credit[0][0]
            credit += Credits
            UpdateCredits = f"UPDATE user SET `User_SocalCredits` = {credit} WHERE `User_ID` = '{User.id}';"
            with connetion.cursor() as SQL_Insert:
                SQL_Insert.execute(UpdateCredits)
                SQL_Insert.close()
            return ""
        except:
            SQL_Insert.close()
            return "Datenbank Fehler versuche es später erneut"
    except Exception as e:
        SQL_Abfrage.close()

        return f"Error: {e}"


def GetMyCredits(User: discord.Member):
    getcredit = f"SELECT `User_SocalCredits` FROM user WHERE `User_ID` = '{User.id}';"
    try:
        with connetion.cursor() as SQL_Abfrage:
            SQL_Abfrage.execute(getcredit)
            credit = SQL_Abfrage.fetchall()
            SQL_Abfrage.close()
        if len(credit) == 0:
            return f"{User.name} du bist noch nicht im Credet System Angemeldet"
        else:
            return f"{User.name} hat {credit[0][0]} SocialCredit in der Hosentasche"

    except Exception as e:
        SQL_Abfrage.close()
        return f"Error: {e}"


def TopThree():
    UserExists = "SELECT * FROM user ORDER BY `User_SocalCredits` desc LIMIT 3;"
    try:
        with connetion.cursor() as SQL_Abfrage_TopThree:
            SQL_Abfrage_TopThree.execute(UserExists)
            all = SQL_Abfrage_TopThree.fetchall()
            SQL_Abfrage_TopThree.close()
            if len(all) != 0:
                return f"1. Platz gewinnt {all[0][0]} mit {all[0][1]} Punkten !!!\n2. Platz gewinnt {all[1][0]} mit {all[1][1]} Punkten !!\n3. Platz gewinnt {all[2][0]} mit {all[2][1]} Punkten !"
            else:
                return "Es gibt nicht genug mitspieler"
    except Exception as e:
        SQL_Abfrage_TopThree.close()
        return f"Error: {e}"


def GetCredits(User: discord.Member):
    getcredit = f"SELECT `User_SocalCredits` FROM user WHERE `User_ID` = '{User.id}';"
    try:
        with connetion.cursor() as SQL_Abfrage:
            SQL_Abfrage.execute(getcredit)
            credit = SQL_Abfrage.fetchall()
            SQL_Abfrage.close()
        if len(credit) == 0:
            return f"{User.name} du bist noch nicht im Credet System Angemeldet"
        else:
            return credit[0][0]

    except Exception as e:
        SQL_Abfrage.close()
        return f"Error: {e}"



def ConCheck():
    UserExists = "SELECT * FROM `user`  LIMIT 1;"
    try:
        with connetion.cursor() as SQL_Abfrage_Check:
            SQL_Abfrage_Check.execute(UserExists)
            _ = SQL_Abfrage_Check.fetchall()
            SQL_Abfrage_Check.close()
            return "OK"

    except Exception as e:
        SQL_Abfrage_Check.close()
        return f"Error: {e}"

