# autosage-app-using-gemini-flash

# 🚗 AutoSage – AI Vehicle Expert App (Gemini Flash)

AutoSage is an AI-powered vehicle assistant that helps users explore, compare, and understand two-wheelers and four-wheelers before purchasing them.
The application uses **Google Gemini Flash** to provide intelligent recommendations, simplified specifications, maintenance guidance, and eco-friendly vehicle suggestions.

The goal of AutoSage is to make vehicle buying decisions easy, fast, and reliable.

---

## 📌 Problem Statement

Buying a vehicle is confusing for most users.
People face difficulties such as:

* Too many vehicle options in the market
* Hard-to-understand technical specifications
* Fake or biased online reviews
* Lack of maintenance knowledge
* No personalized recommendation system

AutoSage solves this by acting as a **vehicle expert assistant**.

---

## 💡 Key Features

### 🤖 AI Vehicle Recommendation

Ask questions like:

> “Best bike under 1.5 lakh with good mileage?”

AutoSage analyzes user requirements and suggests suitable vehicles.

### 🔍 Vehicle Comparison

* Compare two or more vehicles
* Mileage comparison
* Price comparison
* Feature comparison

### 🧠 Gemini Flash AI Assistant

Natural language interaction with users:

* Understands simple English queries
* Explains specs in easy language
* Summarizes reviews

### 🛠 Maintenance Guidance

* Seasonal maintenance tips
* Battery care suggestions
* Tire pressure reminders
* Service alerts

### 🌱 Eco-Friendly Vehicle Finder

* Electric vehicle suggestions
* Hybrid car recommendations
* Environmental impact insights

### 🎤 Voice Query Support

Users can ask questions using voice commands.

---

## 🧱 System Architecture

User → Web Interface → Backend Server → Gemini Flash API → Response → User

1. User enters vehicle query
2. Backend sends prompt to Gemini Flash
3. Gemini processes the request
4. Response is formatted and shown to user

---

## 🧰 Tech Stack

**Frontend**

* HTML
* CSS
* JavaScript

**Backend**

* Python (Flask)

**AI Model**

* Google Gemini Flash API

**Database (Optional)**

* SQLite / Firebase

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/AutoSage.git
cd AutoSage
```

### 2️⃣ Install Requirements

```bash
pip install flask
pip install google-generativeai
pip install python-dotenv
```

### 3️⃣ Add Gemini API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Run the App

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Example Queries

* Best car under 10 lakh
* Compare Honda Activa and TVS Jupiter
* Maintenance tips for bike
* Best electric scooter in India
* Car with highest mileage

---

## 👤 Target Users

* Students buying first bike
* Families buying cars
* Working professionals
* Eco-conscious buyers

---

## 📊 Future Enhancements

* Showroom locator using maps
* Resale value prediction
* Insurance suggestions
* EMI calculator
* Mobile app version

---

## 🎯 Project Outcome

AutoSage reduces confusion in vehicle selection and helps users make informed decisions using Artificial Intelligence.

---

## 📜 License

This project is for educational purposes.

---

## 🙌 Acknowledgment

Developed as a college project using **Google Gemini Flash AI** to demonstrate real-world application of Artificial Intelligence in the automobile domain.
