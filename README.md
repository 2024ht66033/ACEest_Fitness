# 🏋️ ACEest Fitness – Flask Web Application

This project is a web-based fitness tracker for managing personal workouts. It was developed as part of a DevOps assignment to demonstrate best practices in version control, unit testing, Docker containerization, and CI/CD automation using GitHub Actions.

---

## 📁 Project Structure

Aceest_Fitness/
├── flask_app.py # Main Flask application
├── test_app.py # Pytest unit tests
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── .github/
│ └── workflows/
│ └── main.yml # GitHub Actions CI/CD pipeline
└── README.md # Project documentation

---

## ⚙️ Technologies Used

- Python 3.9+
- Flask
- Pytest
- Docker
- Git & GitHub
- GitHub Actions

---

## 🚀 How to Run the Application Locally

### 🧰 Prerequisites

- Python installed (`python --version`)
- `pip` for installing packages

### ▶️ Steps to Run

```bash
# Clone the repository
git clone https://github.com/2024ht66033/Aceest_Fitness.git
cd Aceest_Fitness

# Install dependencies
pip install -r requirements.txt

# Start the Flask app
python flask_app.py
•	The app will run at: http://127.0.0.1:5000
________________________________________
📡 API Endpoints
Method	Endpoint	Description
POST	/add_workout	Add a workout with duration
GET	/workouts	View all workouts
________________________________________
🧪 Running Unit Tests Locally
Unit tests are written using Pytest to validate the API functionality.
📦 Run Tests
pytest test_app.py
Expected:
•	Tests should pass if endpoints work correctly.
________________________________________
🐳 Docker Containerization
🔨 Build Docker Image
docker build -t aceest_fitness .
🚀 Run the Container
docker run -p 5000:5000 aceest_fitness
Visit the app at: http://localhost:5000
________________________________________
🔁 GitHub Actions CI/CD Pipeline
The project includes an automated CI/CD workflow:
✅ Trigger
•	Every git push to the repository
🔄 What It Does
•	Sets up Python environment
•	Installs dependencies
•	Runs pytest tests
📁 File
•	.github/workflows/main.yml
Check the Actions tab on GitHub for run logs and status.
________________________________________
👤 Author
•	Name: Tanveersingh Champawat
•	GitHub ID: 2024ht66033
________________________________________
📝 License
For educational and academic purposes only.

---

