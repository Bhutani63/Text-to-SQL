# Text-to-SQL

A user-friendly Streamlit web app that converts natural language queries into SQL commands, executes them on a locally connected MySQL database, and presents results in plain language.

---

## Features

- Converts plain English queries into SQL using Google Generative AI
- Connects to MySQL database using `mysql-connector-python`
- Interactive UI built with Streamlit for easy use
- Uses environment variables for sensitive info via `python-dotenv`

---

## Requirements

- Python 3.7+
- streamlit
- google-generativeai
- python-dotenv
- mysql-connector-python

---

## Installation & Setup
1. Clone the repository:
   git clone https://github.com/Bhutani63/Text-to-SQL.git
   cd Text-to-SQL

2. **Create and activate a virtual environment:**
    python -m venv streamlit_env
    
    On Windows
    streamlit_env\Scripts\activate
    
    On macOS/Linux
    source streamlit_env/bin/activate


3. **Install dependencies:**

    pip install -r requirements.txt


4. **Create a `.env` file in the project root with the following variables:**

    MYSQL_HOST=localhost
    MYSQL_USER=your_mysql_username
    MYSQL_PASSWORD=your_mysql_password
    MYSQL_DATABASE=your_database_name
    GOOGLE_API_KEY=your_google_api_key

   
---

## Usage

Run the application with:

  streamlit run app.py

Once running, Streamlit will provide a local URL (typically http://localhost:8501) in your terminal or browser.

Open the URL in your browser.

Enter natural language questions or commands in plain English.

The app will generate SQL queries using Google’s generative AI and run them against your MySQL database.

Results will be displayed in simple, readable form within the app UI.

## Project Structure

- `app.py` — Streamlit app and user interface
- `sql.py` — Handles SQL query generation and database interaction
- `requirements.txt` — Project dependencies
- `.gitignore` — Defines ignored files for Git
- `.env` — Environment variables (not tracked in Git)

## Troubleshooting

# Connection errors:
Double-check your .env variables for exact MySQL credentials and database details.

# SQL errors (e.g., column mismatch):
Ensure your database schema matches what the app expects. You might need to adjust the SQL queries accordingly.

# Environment setup issues:
  Make sure all dependencies in requirements.txt are installed and your virtual environment is activated.

# Lost connection errors during queries:
  Consider increasing MySQL timeout settings temporarily via MySQL client:
  
  SET GLOBAL net_read_timeout=120;
  SET GLOBAL net_write_timeout=120;
  SET GLOBAL wait_timeout=28800;
  SET GLOBAL interactive_timeout=28800;

## License

  This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributions

  Contributions are welcome! Please open issues or submit pull requests for improvements.

---

## Contact

Created by Simran. Feel free to reach out with questions or feedback.


1. **Clone the repo:**

