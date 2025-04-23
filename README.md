# 📚StudySync - Python Exam Prep CLI

StudySync is a simple command-line interface (CLI) app designed for Python exam preparation. It allows users to take quizzes on different Python topics, track their scores, and review incorrect answers to help them prepare better for their exams.

## Features

1. **Take Quiz by Topic**: Choose a specific Python topic and answer questions related to it.
2. **View Scores**: Check your scores for all completed quizzes.
3. **Review Incorrect Answers**: *(Feature not yet implemented)*
4. **Exit**: Finish your session and exit the app.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Steps to Get Started

1. **Clone the Repository**:

   Clone the project to your local machine using the following command:

   **`git clone https://github.com/faryal16/Class_07_OOP_Principles.git`**

2. **Navigate to the Project Folder**:

   Change to the project directory:

   **`cd Class7 StudySync`**

3. **Install Dependencies**:

   Install the required dependencies using pip:

   **`pip install -r requirements.txt`**

   The dependencies are:

   - `termcolor`: For colored terminal output.
   - Any additional dependencies can be added to `requirements.txt` as needed.

4. **Run the Application**:

   You can run the application using Python:

   **`python main.py`**

   This will start the quiz app in your terminal.

## Usage

Upon running the app, you'll be prompted to enter your name. Then, you'll see the following options:

1. **Take Quiz by Topic**: Choose a Python topic and answer the quiz questions. Your progress will be saved.
2. **View My Scores**: See your current scores for completed quizzes.
3. **Review Incorrect Answers**: *(Not yet implemented, but planned for future updates.)*
4. **Exit**: End the session and exit the app with a congratulatory message.

### Example Run:

📘 Welcome to StudySync - Python Exam Prep 📘

✍ Please enter your name: John

Hello John! Let's get started with your Python exam preparation! 💪

Choose an option:

Take quiz by topic

View my scores

Review incorrect answers

Exit

Enter your choice: 1

Select a topic: 📚

Python Basics

Data Structures

Functions Enter topic number: 1

[Quiz begins here...]


## App Functionality

1. **Taking a Quiz by Topic**:
   - The user will be presented with a list of available topics (e.g., Python Basics, Data Structures, Functions).
   - Once a topic is selected, the quiz for that topic will begin, asking multiple-choice questions.
   - The user's score is recorded after each quiz session.

2. **View Scores**:
   - The user can check their scores for completed quizzes. It displays the scores for each topic and overall performance.

3. **Review Incorrect Answers (Planned for Future)**:
   - This feature will allow users to review questions they answered incorrectly, helping them learn from their mistakes.

4. **Exit**:
   - The user will be shown a congratulatory message and the app will exit.

## Contributing

If you'd like to contribute to StudySync, feel free to fork the repository and submit pull requests with new features or bug fixes.

## License

This project is open-source and available under the MIT License.
