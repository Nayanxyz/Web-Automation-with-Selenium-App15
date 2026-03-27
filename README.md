# 🤖 Selenium Web Automation Engine with Tkinter GUI

A hybrid Python desktop application that connects a local graphical user interface (GUI) with an automated web scraping and testing backend. This project demonstrates the "Separation of Concerns" design principle by strictly decoupling data collection from browser execution.

<img width="690" height="445" alt="Web-Automation-GUI" src="https://github.com/user-attachments/assets/84a9ce40-7aa4-4728-b26a-9ad65edb473c" />
<img width="1386" height="767" alt="Textbox" src="https://github.com/user-attachments/assets/c9d5593d-b008-45ba-8ad1-21c8e044f6c1" />

## 🧠 Engineering Architecture
This system is divided into two distinct layers:
1. **Frontend (`GUI.py`):** Built with Python's `tkinter`. It generates a secure desktop window to collect user credentials and form data. It acts exclusively as a data collection bridge and contains zero automation logic.
2. **Backend (`main.py`):** An Object-Oriented `WebAutomation` engine built with Selenium WebDriver. It receives extracted text from the GUI and executes headless/automated commands on the target website.

## ⚙️ Core Features
* **Direct Routing Bypass:** Avoids fragile React.js UI sidebars and duplicate HTML IDs by using direct URL navigation (`driver.get()`) to reach target endpoints securely.
* **Intelligent Synchronization:** Abandons rigid `time.sleep()` commands in favor of `WebDriverWait` and `ExpectedConditions` (EC), ensuring the bot only interacts with DOM elements once they are physically visible.
* **Automated File Management:** Dynamically manipulates Chrome `Options` to override default browser settings, forcing all downloaded files to save directly into the current working directory (`os.getcwd()`).
* **Robust Locators:** Prioritizes strict `By.ID` locators over brittle Absolute XPaths.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Frontend:** Tkinter (Standard Library)
* **Automation Backend:** Selenium WebDriver 4.x
* **Browser:** Google Chrome & ChromeDriver

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/Nayanxyz/Web-Automation-with-Selenium-App15.git
cd Web-Automation-with-Selenium-App15
```
**2. Install Dependencies**
```bash
pip install selenium
```

**3. Execute the Application**
```bash
python GUI.py
```

