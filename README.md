
# 🌐 Localized News Feed Web App

A simple full-stack application to search and display real-time news articles based on user queries using **FastAPI backend** and a **vanilla HTML/CSS/JavaScript frontend**. It fetches news from the **NewsAPI.org** service and displays it beautifully.

---

## 🚀 Features

- 🔍 Real-time news search
- 🌎 Global or local topics (e.g., "India", "AI", "Cricket", etc.)
- 📰 Clean UI using pure HTML, CSS & JS
- ⚡ FastAPI backend with CORS support
- 📱 Responsive design

---

## 📁 Project Structure

```

localized-news-feed/
│
├── index.html        ← Frontend UI (single file with HTML, CSS, JS)
├── main.py           ← FastAPI backend to fetch news data
├── README.md         ← This file

````

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repo

```bash
git clone https://github.com/your-username/localized-news-feed.git
cd localized-news-feed
````

---

### 🖥️ 2. Install Backend Dependencies

```bash
pip install fastapi uvicorn requests
```

---

### 🔑 3. Set News API Key

1. Get your free API key from [https://newsapi.org](https://newsapi.org).
2. Open `main.py` and replace:

```python
API_KEY = "your_news_api_key_here"
```

---

### 🧪 4. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

By default, it will run on:
📍 `http://127.0.0.1:8000`

---

### 🌐 5. Open the Frontend

Open the `index.html` file directly in your browser.
(Use **Live Server** in VS Code for a smoother experience.)

---

## 🖼️ Demo Screenshot

<img width="1336" height="1518" alt="image" src="https://github.com/user-attachments/assets/d97e3eca-7385-4768-8b42-1a5b2bfee139" />
<img width="1330" height="1496" alt="image" src="https://github.com/user-attachments/assets/fd26531d-4bf3-4b0e-afb1-8d0b7b91ceb7" />


---

## 📦 API Reference

### GET `/news?query=your_keyword`

Fetches latest news articles for the given query.

**Example:**

```http
GET http://127.0.0.1:8000/news?query=ai
```

Returns:

* `articles[]`: List of news items (title, description, url, source)

---

## 📌 Technologies Used

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: FastAPI (Python)
* **News Provider**: [NewsAPI.org](https://newsapi.org)
* **Deployment Ready**: Portable HTML and backend

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Developed by **\[Your Name]**
Feel free to contribute or open issues!

```


