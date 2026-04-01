# Pujan's Login Web Application
### Flask + HTML Assignment

---

## 📁 Project Structure

```
pujan_login_app/
├── app.py              ← Python Flask backend (run this!)
├── requirements.txt    ← Python packages needed
├── users.json          ← Auto-created when you register
└── templates/
    ├── login.html      ← Login page
    ├── register.html   ← Registration page
    └── dashboard.html  ← Success page after login
```

---

## 🚀 How to Run (Step by Step)

### Step 1 — Install Flask
Open your terminal / command prompt and type:
```
pip install flask
```

### Step 2 — Go to the project folder
```
cd pujan_login_app
```

### Step 3 — Run the app
```
python app.py
```

### Step 4 — Open in browser
Go to: **http://127.0.0.1:5000**

---

## 📥 Sample Flow (as required)

1. Open browser → goes to **Login page**
2. Click "Create one" → opens **Register page**
3. Fill in username + password → click **Create Account**
4. Data saved in `users.json` file ✅
5. Go to Login → enter same credentials → click **Sign In**
6. If correct → **Dashboard** shown with welcome message ✅
7. If wrong → error message shown ✅

---

## 🔧 How the Backend Works (Simple Explanation)

- `Flask` is a micro web framework for Python
- `render_template()` → shows the HTML pages
- `request.form` → reads what the user typed in the form
- `json` module → saves/loads user data from a file
- `session` → remembers who is logged in

---

## ✅Requirements Covered

| Requirement | Status |
|---|---|
| Register page with username + password | ✅ |
| Login page with username + password | ✅ |
| Data stored in file (users.json) | ✅ |
| Login validation | ✅ |
| Success/error messages | ✅ |
| Beautiful frontend | ✅ |

---

*Built by Pujan*