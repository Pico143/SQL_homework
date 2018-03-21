import psycopg2


def print_labels():
    print ("Main Menu:\n")
    print ("1.Query that returns the 2 name columns of the mentors table.")
    print ("2.Query that returns the nicknames of all mentors working at Miskolc.")
    print ("3.Find Carol.")
    print ("4.Find the girl from Adipiscingenimmi University.")
    print ("5.Add Markus to the application process with code 54823.")
    print ("6.Change Jemima Foreman phone number.")
    print ("7.Remove students with email at mauriseu.net domain.")
    print ("0.Exit application\n")


def connect_to_database():
    try:
        connect_str = "dbname='pico' user='pico' host='localhost' password='F@llout2'"
        connection = psycopg2.connect(connect_str)
        connection.autocommit = True
        cursor = connection.cursor()
    except psycopg2.DatabaseError as exception:
        print(exception)
        if connection:
            connection.close()
    return connection, cursor


def disconnect_from_database(connection, cursor):
    cursor.close()
    connection.close()


def mentor_names():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT first_name,last_name FROM mentors;")
    rows = cursor.fetchall()
    for item in rows:
        print (item)
    disconnect_from_database(connection, cursor)


def miskolc_mentor_nicknames():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT nick_name FROM mentors WHERE city='Miskolc';")
    rows = cursor.fetchall()
    for item in rows:
        print (item)
    disconnect_from_database(connection, cursor)


def main():
    while True:
        print_labels()
        choice = input("Please choose an option: ")
        if choice == "1":
            mentor_names()
        elif choice == "2":
            miskolc_mentor_nicknames()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "0":
            break
        else:
            print ("Wrong choice provided. Please try again.")


if __name__ == "__main__":
    main()
