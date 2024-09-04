Here’s a `README.md` file for your GitHub repository:

---

# Natural Language to SQL App

## Overview

This project showcases an application that converts natural language queries into SQL commands, allowing users to interact with databases without needing technical expertise. The application leverages Google Gemini Pro's LLM for accurate query interpretation and uses Streamlit for an intuitive user interface.

## Features

- **Natural Language to SQL Conversion:** Converts user questions into SQL queries.
- **Google Gemini Pro Integration:** Utilizes advanced language models for query interpretation.
- **Streamlit Interface:** Provides a user-friendly interface for real-time querying.
- **SQLite Database Interaction:** Connects to and queries a sample SQLite database.

## Installation

### Prerequisites

- **Python 3.10** or higher
- **Conda** or a virtual environment manager
- **Google API Key** for Gemini Pro

### Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Create and Activate the Conda Environment:**

    ```bash
    conda create -p venv python=3.10 -y
    conda activate venv
    ```

3. **Install Dependencies:**

    Create a `requirements.txt` file with the following content:

    ```plaintext
    streamlit
    python-dotenv
    google-generativeai
    sqlite3
    ```

    Then run:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**

    Create a `.env` file in the root directory of your project and add your Google API key:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Code

### `app.py`

```python
from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini Pro's API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Google Gemini Model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    full_prompt = f"{prompt}\n{question}"
    response = model.generate_content(full_prompt)
    return response.text

# Function to retrieve query results from SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define your prompt
prompt = """
You are an expert in converting English questions to SQL queries!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
\nExample 2 - Tell me all the students studying in Data Science class?, 
the SQL command will be something like this SELECT * FROM STUDENT 
where CLASS="Data Science"; 
also the SQL code should not have ``` in beginning or end and SQL word in output
"""

# Streamlit App framework
st.set_page_config(page_title="I can Retrieve Any SQL Query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    response = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in response:
        st.write(row)
```

### `sql.py`

```python
import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert some records
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Abhiram', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Rajesh', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Abhiram', 'Data Science', 'A', 86)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Abhiram', 'Data Science', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Abhiram', 'Data Science', 'A', 35)''')

# Display all records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
```

### `requirements.txt`

```plaintext
streamlit
python-dotenv
google-generativeai
sqlite3
```

## Usage

1. **Run the SQL Setup Script:**

    ```bash
    python sql.py
    ```

2. **Start the Streamlit App:**

    ```bash
    streamlit run app.py
    ```

3. **Access the App:**

    Open a web browser and navigate to `http://localhost:8501` to interact with the app.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
