# 🔐 Pujan's Login Web Application
### Flask + HTML Assignment — GitHub & Render Deployment Guide

---

## 📁 Project Structure

```
pujan_login_app/
├── app.py              ← Python Flask backend
├── requirements.txt    ← Python packages (flask + gunicorn)
├── Procfile            ← Tells Render how to run the app
├── .gitignore          ← Files Git should ignore
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html
```

---

## 💻 Run Locally (on your PC)

```bash
# Step 1 - Install packages
sudo apt install python3-flask -y

# Step 2 - Run the app
python3 app.py

# Step 3 - Open browser at: http://127.0.0.1:5000
```

---

## 🐙 PART 1 — Push to GitHub

### 1. Install Git
```bash
sudo apt install git -y
```

### 2. Set your Git identity
```bash
git config --global user.name "Pujan"
git config --global user.email "youremail@gmail.com"
```

### 3. Create repo on GitHub
- Go to https://github.com → click "+" → "New repository"
- Name: pujan-login-app → Public → Create repository

### 4. Push your code
```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/pujan-login-app.git
git push -u origin main
```

---

## 🚀 PART 2 — Deploy on Render (Free)

1. Go to https://render.com → Sign up with GitHub
2. Click "New +" → "Web Service" → Connect your repo
3. Settings:
   - Runtime: Python 3
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
   - Instance Type: Free
4. Environment Variables → Add:
   - Key: SECRET_KEY  Value: pujan_super_secret_2024
5. Click "Create Web Service" → wait 2-3 mins
6. Your live URL: https://pujan-login-app.onrender.com 🎉

---

*Built by Pujan · Flask + HTML Assignment*
# python-login-app
