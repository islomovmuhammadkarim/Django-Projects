document.addEventListener("DOMContentLoaded", () => {
    const statsContainer = document.getElementById("stats-container");

    async function fetchDashboardStats() {
        try {
            const res = await fetch('/api/dashboard-stats/');
            const data = await res.json();
            statsContainer.innerHTML = "";

            const stats = [
                {title: "Barcha vazifalar", value: data.total_tasks, icon: "fas fa-tasks"},
                {title: "Bajarilgan", value: data.completed_tasks, icon: "fas fa-check-circle"},
                {title: "Jarayonda", value: data.in_progress_tasks, icon: "fas fa-spinner"},
                {title: "Umumiy vaqt", value: data.total_time, icon: "fas fa-clock"}
            ];

            stats.forEach(stat => {
                const div = document.createElement("div");
                div.className = "stat-card";
                div.innerHTML = `
                    <div class="stat-card-header">
                        <span class="stat-card-title">${stat.title}</span>
                        <i class="${stat.icon} stat-card-icon"></i>
                    </div>
                    <div class="stat-card-value">${stat.value}</div>
                `;
                statsContainer.appendChild(div);
            });
        } catch(err) {
            console.error("Dashboard stats API xatosi:", err);
        }
    }

    fetchDashboardStats();
});
