# Book Recommendation App

## Project Overview

This project is a **Book Recommendation App** that provides personalized book suggestions. It is built using:
- **Frontend**: React Native (Expo)
- **Backend**: Flask with a MySQL database
- **Database**: MySQL, managed via SQLAlchemy ORM and Flask-Migrate
- **Recommendation System**: Machine Learning powered by **Reinforcement Learning** and **Linear Contextual Bandits**

The app allows users to browse, search, save, and interact with books, while using their interactions to generate personalized book recommendations.

---

## Features

1. **User Authentication**: Registration and Login using JWT.
2. **Book Browsing**: View available books with details such as title, author, description, and cover images.
3. **Search**: Full-text search powered by Whoosh.
4. **Interactions**: Users can like, save, and view books. These interactions are stored to personalize recommendations.
5. **Recommendations**:
   - **Content-Based Filtering**: Uses embeddings and cosine similarity to recommend books based on user preferences.
   - **Reinforcement Learning & Contextual Bandits**: A machine learning model powered by **Linear Contextual Bandits** that uses user interactions to learn preferences and deliver contextual recommendations in real-time.

---

## Installation

### 1. Backend Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/book-app.git
    cd backend
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up environment variables by copying `.env.example` to `.env`:
    ```bash
    cp .env.example .env
    ```

4. Set up the MySQL database (Ensure MySQL is installed and running):
    ```bash
    mysql -u root -p
    CREATE DATABASE bookapp;
    ```

5. Run database migrations:
    ```bash
    flask db upgrade
    ```

6. Start the backend server:
    ```bash
    flask run
    ```

### 2. Frontend Setup
1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start the Expo server:
    ```bash
    npm start
    ```

---

## Docker Setup

1. Build and run the containers:
    ```bash
    docker-compose up --build
    ```

2. The backend will be accessible at `http://localhost:5000`.

---

## Recommendation System

The app's recommendation engine combines:
- **Content-based filtering**: Books are recommended based on similarity with previously saved books, using embeddings.
- **Reinforcement Learning**: **Contextual Bandits** techniques like **Linear Contextual Bandits** learn from user interactions such as likes, saves, and views to provide recommendations that adapt to the user's preferences over time.

---

## Deployment

The app is deployed on AWS EC2. The backend runs inside a Docker container and communicates with an RDS MySQL database. Environment variables are managed via `.env` files and AWS Secrets Manager.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes and open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).
