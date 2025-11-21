document.addEventListener("DOMContentLoaded", async () => {
    const container = document.getElementById("time-categories");

    if (!container) return;

    try {
        const res = await fetch("/api/time-categories/");
        const data = await res.json();

        console.log("API DATA:", data);

        container.innerHTML = "";

        if (!data.categories || data.categories.length === 0) {
            container.innerHTML = "<p style='text-align:center; color:#666;'>Hozircha soha mavjud emas</p>";
            return;
        }

        data.categories.forEach(cat => {
            const total = parseInt(cat.total_minutes) || 0;

            const hours = Math.floor(total / 60);
            const minutes = total % 60;

            const div = document.createElement("div");
            div.className = "time-category";
            div.innerHTML = `
                <div class="category-name">
                    <div class="category-icon">📌</div>
                    <span>${cat.name}</span>
                </div>
                <div class="category-time">${hours} soat ${minutes} daqiqa</div>
            `;
            container.appendChild(div);
        });

    } catch (err) {
        console.error("Xatolik:", err);
        container.innerHTML = "<p style='text-align:center; color:red;'>Ma’lumot yuklanmadi</p>";
    }
});
