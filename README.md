# PasswordManager

PasswordManager is a simple web-based application designed to help users securely manage their passwords. This project is built with Flask, a lightweight Python web framework, and includes functionality for adding, editing, deleting, and managing passwords with a focus on security.

## Features

- **User Registration & Login:** Securely register and log in to your account.
- **Password Management:** Add, edit, and delete passwords.
- **Password Strength Checking:** Ensure passwords meet strength criteria.
- **Password Suggestion:** Generate strong, random passwords.
- **Password Visibility Toggle:** Show or hide stored passwords in the table.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Additional dependencies are listed in `requirements.txt`.

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/fslul14/PasswordManager.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd PasswordManager
    ```

3. **Install Dependencies:**

    It is recommended to use a virtual environment. If you don't have one, you can install dependencies globally:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**

    ```bash
    python main.py
    ```

    By default, the application will run on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Structure

- `main.py`: Entry point for the application.
- `logic/`: Contains logic for authentication, password management, and utilities.
- `static/`: Contains static files such as CSS.
- `templates/`: Contains HTML templates for rendering views.
- `tests/`: Contains test files for the application.

## Usage

- **Home Page:** Access the home page to register or log in.
- **User Home Page:** Once logged in, you can add, edit, delete, and manage passwords. Use the "Suggest Password" button to generate strong passwords.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes, improvements, or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask: For the web framework used to build this application.
- Bootstrap: For the front-end framework used for styling (if applicable).

---

