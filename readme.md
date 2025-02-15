# Flask Regex Data Extractor

This is a Flask application that extracts various types of data (emails, URLs, phone numbers, credit card numbers, time, hashtags, currency, and HTML tags) from a given text using regular expressions.

## Features

- Extracts emails, URLs, phone numbers, credit card numbers, times, HTML tags, hashtags, and currency symbols.
- Displays extracted data in a user-friendly format.
- Handles both `GET` and `POST` requests.

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/flask-regex-data-extractor.git
cd flask-regex-data-extractor
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

To avoid conflicts with global Python packages, it’s best to set up a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required packages listed in the `requirements.txt`:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, you can manually install the dependencies:

```bash
pip install flask
```

### 4. Run the Flask Application

Now you can run the Flask app using:

```bash
python app.py
```

### 5. Open the Application

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

You should see the app running. You can enter text in the input box, and the app will display the extracted data based on various regex patterns.

## App Structure

```
/my_flask_app
    /templates
        index.html      # HTML template for displaying the extracted data
    /static
        /css
            style.css    # Basic styling for the app
    app.py                # Main Flask application file
    requirements.txt      # List of required dependencies
```

### `app.py`

- Contains the main Flask routes.
- Uses regular expressions to extract data from the provided text.

### `templates/index.html`

- Displays the form for text input.
- Shows the extracted data.

### `static/css/style.css`

- Contains basic styling for the frontend.

## Example Input & Output

### Input:

```plaintext
Here is a sample of complex data for testing: My email is example@example.com and my website is https://www.example.com. Call me at (123) 456-7890 or email me at support@website.com. My credit card number is 1234-5678-9876-5432. #Testing the code #complex_data <div>HTML tags <span>are fun!</span></div> More data: $1,000.99
```

### Output:

- **Emails**: `example@example.com`, `support@website.com`
- **URLs**: `https://www.example.com`
- **Phone Numbers**: `(123) 456-7890`
- **Credit Cards**: `1234-5678-9876-5432`
- **Hashtags**: `#Testing`, `#complex_data`
- **HTML Tags**: `<div>`, `<span>`, etc.
- **Currency**: `$1,000.99`
