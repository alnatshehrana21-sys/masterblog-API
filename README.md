# 🦁 Masterblog API - TheBlogSpot

Welcome to **Masterblog API**, a professional RESTful backend built with **Flask**. This project serves as a robust data engine for blogging platforms, allowing for cross-platform communication between a cloud-hosted API and local frontend applications.

## ✨ Features
* **Read (List & Sort):** Fetch all blog posts with support for custom sorting by title or content.
* **Search:** Quickly find posts using title or content keywords via query parameters.
* **Create:** Add new posts with automatic unique ID generation and data validation.
* **Update:** Modify existing post data using partial updates (only change what you need).
* **Delete:** Remove posts from the database using specific ID endpoints.
* **CORS Support:** Enabled to allow secure requests from different origins (Local vs. Cloud).

## 🛠️ Tech Stack
* **Backend:** Python 3 with Flask
* **Security:** Flask-CORS for cross-origin resource sharing
* **API Testing:** Postman
* **Deployment:** Codio
* **Version Control:** Git & GitHub

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Masterblog-API.git](https://github.com/YOUR_USERNAME/Masterblog-API.git)
    cd Masterblog-API
    ```

2.  **Install Dependencies:**
    ```bash
    pip install flask flask-cors
    ```

3.  **Run the Backend (Codio):**
    ```bash
    python3 backend/backend_app.py
    ```
    *The API will be available at `http://0.0.0.0:5002`.*

4.  **Connect the Frontend:**
    * Open your local browser to your frontend URL.
    * Paste your Public API URL (e.g., `https://your-box-id-5002.codio.io/api`) into the API Base URL field.

## 📁 Project Structure
* `backend/backend_app.py`: The core API logic, routing, and search/sort functionality.
* `frontend/`: Contains the static files (HTML, CSS, JS) to interact with the API.
* `.settings/`: Project configuration files.

---
Created by **TheBlogSpot** 🚀
