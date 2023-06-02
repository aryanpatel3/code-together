## Overview
Code Together is a web-based application that provides a coding environment for algorithmic problem-solving. Users can write code in an advanced code editor with VSCode like features and run it against a set of predefined test cases, receiving feedback on the correctness of their solutions.

## Technologies Used
- **Frontend**: React, React-Router, and Chakra UI
- **Backend**: FastAPI

Code execution is done in a sandboxed Docker environment using the [Piston API](https://github.com/engineer-man/piston). The testing framework is custom built to compare against tests and provide user feedback.

## Running locally
To set up the Algorithmic Coding Platform locally, follow these steps:

1. Clone the repository: `git clone https://github.com/aryanpatel3/code-together`
2. Install the dependencies for the frontend and backend:
   - ensure you have nodejs and python installed
   - instructions are for mac and linux:
       - for the frontend, navigate to the `frontend` directory and run `npm install`.
       - for the backend, navigate to the `app` directory and create a virtual environment usng `python -m venv .venv`. Activate the environment using `source .venv/bin/activate` and run `pip install -r requirements.txt`.
3. Start the frontend and backend servers:
   - for the frontend, navigate to the `frontend` directory and run `npm start`.
   - for the backend, navigate to the `app` directory and run `python main.py`.
4. Access the application in your browser at `http://localhost:3000`. The server is started at `http://localhost:8000`.
