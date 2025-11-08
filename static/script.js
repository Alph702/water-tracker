document.addEventListener('DOMContentLoaded', () => {
    const goalInput = document.getElementById('goal');
    const water = document.querySelector('.water');
    const totalIntakeSpan = document.getElementById('total-intake');
    const intakeButtons = document.querySelectorAll('.intake-btn');
    const resetButton = document.getElementById('reset-btn');
    const enableNotificationsButton = document.getElementById('enable-notifications-btn');

    let totalIntake = 0;
    let goal = parseInt(goalInput.value);
    const today = new Date().toISOString().split('T')[0];

    const updateUI = () => {
        totalIntakeSpan.textContent = totalIntake;
        const percentage = Math.min((totalIntake / goal) * 100, 100);
        const yTransform = 100 - percentage;
        water.style.transform = `translateY(${yTransform}%)`;
    };

    const fetchData = () => {
        fetch(`/api/data?date=${today}`)
            .then(response => response.json())
            .then(data => {
                totalIntake = data.total_intake || 0;
                updateUI();
            });
    };

    goalInput.addEventListener('change', () => {
        goal = parseInt(goalInput.value);
        updateUI();
    });

    intakeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const amount = parseInt(button.dataset.amount);
            fetch('/api/data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ amount, date: today })
            })
            .then(() => {
                totalIntake += amount;
                updateUI();
            });
        });
    });

    resetButton.addEventListener('click', () => {
        fetch('/api/data', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ date: today })
        })
        .then(() => {
            totalIntake = 0;
            updateUI();
        });
    });

    enableNotificationsButton.addEventListener('click', () => {
        if (!("Notification" in window)) {
            alert("This browser does not support desktop notification");
        } else if (Notification.permission === "granted") {
            new Notification("You are all set for reminders!");
        } else if (Notification.permission !== "denied") {
            Notification.requestPermission().then(function (permission) {
                if (permission === "granted") {
                    new Notification("You will now receive reminders!");
                    setInterval(() => {
                        new Notification("Time to drink water!");
                    }, 3600000); // 1 hour
                }
            });
        }
    });

    fetchData();
});