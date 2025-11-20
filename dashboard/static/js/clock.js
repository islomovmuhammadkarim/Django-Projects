// Clock & progress ring
const circle = document.querySelector('.progress-ring__circle');
const radius = circle.r.baseVal.value;
const circumference = 2 * Math.PI * radius;
circle.style.strokeDasharray = `${circumference}`;
circle.style.strokeDashoffset = 0;

function updateClock() {
    // Local vaqtni olish
    const now = new Date();

    // 24-soat format
    const hours = now.getHours(); // brauzer local time
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    const formattedTime = `${String(hours).padStart(2,'0')}:${String(minutes).padStart(2,'0')}:${String(seconds).padStart(2,'0')}`;
    document.getElementById('time').textContent = formattedTime;

    // Sana va haftaning kuni
    const days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    const day = now.getDate();
    const month = months[now.getMonth()];
    const year = now.getFullYear();
    const weekday = days[now.getDay()];
    document.getElementById('date').textContent = `${day} ${month} ${year}, ${weekday}`;

    // 24 soat progress
    const totalSecondsInDay = 24 * 60 * 60;
    const secondsPassed = hours * 3600 + minutes * 60 + seconds;
    const offset = circumference * (1 - secondsPassed / totalSecondsInDay); // kamayib boradi
    circle.style.strokeDashoffset = offset;
}

setInterval(updateClock, 1000);
updateClock();
