from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
import os
import google.generativeai as genai
from sql import get_connection

## Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Model and provide query as response which converted by the user
#  text prompt(here basically text converted into sql query by gemini model)

def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-2.0-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function to retreive the query or data from the sql database
def read_sql_query(sql):
    conn = get_connection()
    cursor = conn.cursor()
    print("Generated SQL:", sql)   # Prints the SQL query before execution
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

def scalar_result(rows):
    if len(rows) == 1 and len(rows[0]) == 1:
        return float(rows[0][0])
    return rows

sql = "SELECT AVG(MARKS) FROM STUDENT WHERE COURSE = 'Data Science';"
data = read_sql_query(sql)
data = scalar_result(data)
print(data)

## Define your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The database is named students and has a single table STUDENT with columns NAME, COURSE, GRADE, MARKS
    For example,
    Example 1 - How many entries of records are present
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    Example 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT
    where CLASS="Data Science";
    If asked to delete duplicate records in the STUDENT table, generate SQL that keeps only one copy of each duplicate row.

    Example to delete duplicates (keep the row with the lowest id or first occurrence):

    DELETE t1 FROM STUDENT t1
    INNER JOIN STUDENT t2
    ON t1.NAME = t2.NAME AND t1.COURSE = t2.COURSE AND t1.GRADE = t2.GRADE AND t1.MARKS = t2.MARKS
    WHERE t1.id > t2.id;

    Assume the table has a unique id column for identifying rows. If the table does not have an id, generate queries using ROW_NUMBER() or create a temporary table to remove duplicates.
    also the sql code should not have ``` in beginning or end and sql word in output
    Please add necessary aliases for subqueries (derived tables), e.g. use "AS sub" after the subquery.

    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any query")
st.header("Gemini App to Retrieve SQL Data")

question=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

# if submit is clicked

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response)
    st.subheader("The Respone is")
    for row in data:
        print(row)
        st.header(row)