import psycopg2


def print_labels():
    print ("Main Menu:\n")
    print ("1.Query that returns the 2 name columns of the mentors table.")
    print ("2.Query that returns the nicknames of all mentors working at Miskolc.")
    print ("3.Find Carol.")
    print ("4.Find the girl from Adipiscingenimmi University.")
    print ("5.Add Markus to the application process with code 54823.")
    print ("6.Change Jemima Foreman phone number and show it.")
    print ("7.Remove students with email at mauriseu.net domain.")
    print ("0.Exit application\n")


def connect_to_database():
    try:
        connect_str = "dbname='pico' user='pico' host='localhost' password='any_password"
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
        print (' '.join(item))
    disconnect_from_database(connection, cursor)


def miskolc_mentor_nicknames():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT nick_name FROM mentors WHERE city='Miskolc';")
    rows = cursor.fetchall()
    for item in rows:
        print (' '.join(item))
    disconnect_from_database(connection, cursor)


def find_Carol():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT full_name FROM applicants")
    if cursor.rowcount == 0:
        cursor.execute("ALTER TABLE applicants ADD full_name VARCHAR;")
    cursor.execute("UPDATE applicants SET full_name = CONCAT(first_name,' ',last_name);")
    cursor.execute("SELECT phone_number, full_name FROM applicants WHERE first_name='Carol';")
    rows = cursor.fetchall()
    for item in rows:
        print (', '.join(item))
    disconnect_from_database(connection, cursor)


def find_that_girl():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT full_name FROM applicants")
    if cursor.rowcount == 0:
        cursor.execute("ALTER TABLE applicants ADD full_name VARCHAR;")
    cursor.execute("UPDATE applicants SET full_name = CONCAT(first_name,' ',last_name);")
    cursor.execute("SELECT phone_number, full_name FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';")
    rows = cursor.fetchall()
    for item in rows:
        print (', '.join(item))
    disconnect_from_database(connection, cursor)


def add_marius():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM applicants WHERE application_code=54823;")
    if cursor.rowcount == 0:
        cursor.execute(
            "INSERT INTO applicants (first_name,last_name,phone_number,email,application_code) VALUES('Markus','Schaffarzyk','003620/725-2666','djnovus@groovecoverage.com','54823')")
        cursor.execute(
            "UPDATE applicants SET full_name = CONCAT(first_name,' ',last_name) WHERE application_code=54823;")
    cursor.execute("SELECT * FROM applicants WHERE application_code=54823;")
    rows = cursor.fetchall()
    for result in rows:
        result = list(result)
        for item in result:
            result[result.index(item)] = str(item)
        print (', '.join(result))
    disconnect_from_database(connection, cursor)


def change_foreman_phone_number():
    connection, cursor = connect_to_database()
    cursor.execute(
        "UPDATE applicants SET phone_number = '003670/223-7459' WHERE first_name = 'Jemima' AND last_name = 'Foreman';")
    cursor.execute("SELECT phone_number FROM applicants WHERE first_name = 'Jemima' AND last_name = 'Foreman';")
    rows = cursor.fetchall()
    for result in rows:
        for item in result:
            print (item)
    disconnect_from_database(connection, cursor)


def remove_arsenio_and_friend():
    connection, cursor = connect_to_database()
    cursor.execute("DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';")
    print ("Records with emails at @mauriseu.net domain are removed.")
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
            find_Carol()
        elif choice == "4":
            find_that_girl()
        elif choice == "5":
            add_marius()
        elif choice == "6":
            change_foreman_phone_number()
        elif choice == "7":
            remove_arsenio_and_friend()
        elif choice == "0":
            break
        else:
            print ("Wrong choice provided. Please try again.")


if __name__ == "__main__":
    main()
