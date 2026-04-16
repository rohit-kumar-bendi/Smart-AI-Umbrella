Smart AI Umbrella for Crops
This project automates crop protection using sensors, Raspberry Pi, and AI.



# 🌾 Smart AI Umbrella System

An IoT-based smart agriculture system that automatically protects crops using environmental conditions.

## 🚀 Features

- 🌡 Temperature monitoring
- 🌧 Rain detection
- 🌱 Soil moisture detection
- ☂ Automated umbrella control
- 📊 Real-time dashboard
- 🧠 Decision engine with explanations
- 📈 Sensor data visualization
- ⚙ Manual and auto modes

## 🧠 Working

The system uses a rule-based algorithm:

- Rain + Dry Soil → Close umbrella (allow irrigation)
- Rain + Moist Soil → Open umbrella
- High Temperature → Open umbrella
- Normal Conditions → Close umbrella

## 🖥 Tech Stack

- Python
- Flask
- HTML/CSS
- Chart.js

## 📂 Project Structure

- `main.py` → Decision engine
- `dashboard/app.py` → Backend server
- `templates/` → UI
- `static/` → CSS
- `shared/state.json` → System state

## ▶ How to Run

```bash
python main.py
cd dashboard
python app.py