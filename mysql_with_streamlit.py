import streamlit as st
import pandas as pd
import mysql.connector

#Create Database Connection
def create_connection():
    connection = mysql.connector.connect(
        host="host", #Database Host
        user="name", #Database UserName
        password="password", #Database Password 
        database="db_name" #Database Name
    )
    return connection

def main():
    st.title("Streamlit with MySQL Test")

    # Connect to the MySQL database
    connection = create_connection()

    if connection:
        cursor = connection.cursor()

        try:
            # Execute a query
            cursor.execute("SELECT * FROM `users`;") #give a Sample Query 
            results = cursor.fetchall()

            # Convert the results to a pandas DataFrame
            columns = [i[0] for i in cursor.description]
            df = pd.DataFrame(results, columns=columns)

            # Display the DataFrame as a DataTable
            st.dataframe(df)

        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()