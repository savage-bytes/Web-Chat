![image](https://github.com/user-attachments/assets/14bdbd97-e50c-4808-8ebe-67b229f860e4)

# 🗨️ ChatConnect  

ChatConnect is a simple real-time chat application built with Django and WebSockets. No login required—just enter a name and a chat room ID to start chatting instantly!  

## 🚀 Features  

- 🔹 **No authentication required** – Just enter a name and join any room.  
- 🔹 **Real-time messaging** – Powered by Django Channels and WebSockets.  
- 🔹 **Unlimited chat rooms** – Join or create any room dynamically.  
- 🔹 **Minimalistic UI** – Clean and easy-to-use interface.  

## 🛠️ Tech Stack  

- **Backend**: Django, Django Channels, WebSockets  
- **Frontend**: HTML, CSS, JavaScript (Vanilla)  
- **Database**: SQLite (default, can be changed)
  

## ⚙️ Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/chatconnect.git
   cd chatconnect
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**  
   ```bash
   python manage.py runserver
   ```

6. **Open the app in your browser**  
   Visit: `http://127.0.0.1:8000/`  

## 🎯 Usage  

1. Enter a **display name** (what others will call you).  
2. Enter a **room ID** (e.g., "python", "django", "tech-talk").  
3. Click **Enter Room** to start chatting in real time!  

## 🌟 Contributing  

Pull requests are welcome! Feel free to fork this project and submit improvements.  

## 📜 License  

This project is open-source and available under the MIT License.  

---

Let me know if you need any modifications! 🚀
