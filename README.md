# FlaskBlog

FlaskBlog is a web blogging platform built with Flask, a micro web framework written in Python. This project aims to provide a simple yet functional blog platform where users can share their thoughts and ideas through posts. FlaskBlog includes features such as user authentication, post creation, editing, and deletion, and admin management.

## Live Version

A live version of FlaskBlog is available at the following link: [https://flaskblog-ws8o.onrender.com](https://flaskblog-ws8o.onrender.com).


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12.0 or higher installed on your machine.
- pip for installing Python packages.

## Setup Instructions

Follow these steps to get FlaskBlog up and running on your local machine:

1. Clone the repository:

    ```bash
    git clone https://github.com/BAXTOR95/FlaskBlog.git
    cd FlaskBlog
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Initialize the database:

    ```bash
    flask --app main.py init-db
    ```

4. Create an admin user:

    ```bash
    flask --app main.py create-admin admin@example.com "strongpassword" "Admin Name"
    ```

## Running the Project

To run FlaskBlog on your local machine, use the following command:

```bash
flask --app main.py run
```

This will start a development server, and you can access the blog at `http://localhost:5000`.

## Contributing

We welcome contributions to FlaskBlog! If you have suggestions for improvements or bug fixes, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

Ensure to update tests as appropriate.
