# 💧 Water Tracker — Project Planning Document

## 🧭 Overview

The **Water Tracker** is a simple, fun, and visually interactive application that helps users stay hydrated. It tracks daily water intake, reminds the user to drink water at intervals, and features a friendly animated character whose water level fills up as the user drinks more throughout the day.

## 🎯 Objectives

* Track the amount of water I drink each day.
* Remind me to drink water regularly (with sound or notification).
* Include **preset goals** like 2L, 3L, or custom values.
* Display a **human character** or bottle that fills up visually as I drink water.
* Keep a simple, aesthetic interface with daily progress.


## 🧩 Core Features (MVP)

1. Input buttons to log water intake (e.g. +200ml, +500ml).
2. Daily goal setting (customizable).
3. Visual progress bar or character filling animation.
4. Local storage to save daily data.
5. Notifications or reminders.


## 🚀 Future Additions

* Weekly and monthly statistics with graphs 📊
* Integration with smartwatches or health APIs
* Voice assistant reminders (“Time to drink water!”)
* Reward or streak system for consistency 🏆


## ⚙️ Technology Stack

| Layer                  | Choice                                                       |
| ---------------------- | ------------------------------------------------------------ |
| **Frontend**           | HTML, CSS (Tailwind or custom), JavaScript                   |
| **Backend**            | Flask                                                        |
| **Database**           | SQLite or local JSON file                                    |
| **Optional Libraries** | Chart.js for stats, Notification API, Anime.js for animation |


## 🧠 System Design / Architecture

```
water_tracker/
│
├── app.py                # Flask app (backend)
├── static/
│   ├── style.css         # Styling for front-end
│   └── script.js         # Handles UI and logic
├── templates/
│   └── index.html        # Main interface
├── data/
│   └── user_data.db      # SQLite database
└── README.md
```


## 🔄 Workflow

1. User logs water intake via buttons.
2. App adds the intake to the total and updates the UI.
3. A reminder triggers every X minutes.
4. The water level animation fills up relative to the goal.
5. Data is saved for the current date.


## ⌚ Development Plan

**Phase 1 – UI & Design (Day 1–2)**

* Design front-end with animated human/water level.
* Create goal selection (2L, 3L, custom).

**Phase 2 – Logic & Tracking (Day 3–4)**

* Implement add/reset functions.
* Store and retrieve daily totals.

**Phase 3 – Notifications (Day 5)**

* Add timed reminders using Notification API or background scheduler.

**Phase 4 – Polish (Day 6)**

* Optimize visuals, add icons, and smooth animations.
* Optional: show daily history chart.


## ⚠️ Possible Challenges

* Handling background reminders reliably.
* Animation sync with water percentage.
* Resetting progress at midnight.

## ✅ Success Criteria

* Works offline and remembers daily progress.
* Reminders trigger consistently.
* Visual feedback (character or bottle) updates smoothly.
* Lightweight and runs on low-end systems or browsers.
