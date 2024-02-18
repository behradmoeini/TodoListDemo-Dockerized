# TodoListDemo-Dockerized

A simple, Dockerized Flask application for managing a task list, demonstrating the integration of Flask with PostgreSQL within Docker containers.

## Features

- View a list of tasks.
- Add new tasks to the list.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation

1. Clone the repository: ```git clone https://github.com/behradmoeini/TodoListDemo-Dockerized.git```
2. Navigate to the project directory: ```cd TodoListDemo-Dockerized```
3. Build and start the containers: ```docker-compose up --build```


### Accessing the Application

After starting the containers, access the task list application by navigating to `http://localhost:5000` in your web browser.

## Adding Tasks

To add a task, simply:
1. Enter the task in the input field on the homepage.
2. Click the "Add Task" button.

The new task will be displayed in the list on the main page.

## Technology Stack

- **Frontend**: HTML rendered through Flask
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

## Acknowledgments

- Flask, for the minimalist Python web framework.
- PostgreSQL, for the open-source relational database.
- Docker, for simplifying deployment.
