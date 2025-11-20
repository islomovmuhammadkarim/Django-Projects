document.addEventListener("DOMContentLoaded", () => {
    // ===== Toshkent vaqti va progress ring =====
    const circle = document.querySelector('.progress-ring__circle');
    const radius = circle.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;
    circle.style.strokeDasharray = `${circumference}`;
    circle.style.strokeDashoffset = 0;

    const timeEl = document.getElementById('time');
    const dateEl = document.getElementById('date');

    function updateClock() {
        const now = new Date(new Date().toLocaleString("en-US", {timeZone: "Asia/Tashkent"}));
        const hours = String(now.getHours()).padStart(2,'0');
        const minutes = String(now.getMinutes()).padStart(2,'0');
        const seconds = String(now.getSeconds()).padStart(2,'0');
        timeEl.textContent = `${hours}:${minutes}:${seconds}`;

        const days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
        const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
        const day = now.getDate();
        const month = months[now.getMonth()];
        const year = now.getFullYear();
        const weekday = days[now.getDay()];
        dateEl.textContent = `${day} ${month} ${year}, ${weekday}`;

        const totalSecondsInDay = 24*60*60;
        const secondsPassed = now.getHours()*3600 + now.getMinutes()*60 + now.getSeconds();
        const progress = (1 - secondsPassed/totalSecondsInDay) * circumference;
        circle.style.strokeDashoffset = progress;
    }
    setInterval(updateClock, 1000);
    updateClock();

    // ===== HomeTime Tracker =====
    const timeCategoriesContainer = document.getElementById("time-categories");
    async function fetchTimeCategories() {
        try {
            const res = await fetch('/api/time-categories/');
            const data = await res.json();
            timeCategoriesContainer.innerHTML = "";

            if(data.categories.length === 0){
                timeCategoriesContainer.innerHTML = "<p style='text-align:center; color:#666;'>Hozircha soha mavjud emas</p>";
                return;
            }

            data.categories.forEach(cat => {
                const div = document.createElement("div");
                div.className = "time-category";
                div.innerHTML = `
                    <div class="category-name">
                        <div class="category-icon">📌</div>
                        <span>${cat.name}</span>
                    </div>
                    <div class="category-time">${Math.floor(cat.total_minutes/60)} soat</div>
                `;
                timeCategoriesContainer.appendChild(div);
            });

        } catch(err){
            console.error(err);
        }
    }
    fetchTimeCategories();

    // ===== Muhim Vazifalar =====
    const tasksContainer = document.getElementById("tasks-list");
    async function fetchTasks() {
        try {
            const res = await fetch('/api/important-tasks/');
            const data = await res.json();
            tasksContainer.innerHTML = "";

            if(data.tasks.length === 0){
                tasksContainer.innerHTML = "<p style='text-align:center; color:#666;'>Hozircha muhim vazifa yo'q</p>";
                return;
            }

            data.tasks.forEach(task => {
                const div = document.createElement("div");
                div.className = "task-item";
                div.innerHTML = `
                    <div class="task-icon">⚡</div>
                    <div class="task-name">${task.title}</div>
                `;
                tasksContainer.appendChild(div);
            });

        } catch(err){
            console.error(err);
        }
    }
    fetchTasks();
});
