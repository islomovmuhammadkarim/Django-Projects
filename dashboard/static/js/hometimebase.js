document.addEventListener("DOMContentLoaded", async () => {
    const container = document.getElementById("time-categories");

    try {
        const res = await fetch("/api/time-categories/");
        const data = await res.json(); // { categories: [...] }

        container.innerHTML = "";

        if (!data.categories || data.categories.length === 0) {
            container.innerHTML = "<p style='text-align:center; color:#666;'>Hozircha soha mavjud emas</p>";
            return;
        }

        data.categories.forEach(cat => {
            const hours = Number(cat.hours) || 0;
            const minutes = Number(cat.minutes) || 0;
            const name = cat.name || "Noma’lum";
            const icon = cat.icon || "📌";

            const div = document.createElement("div");
            div.className = "time-category";
            div.innerHTML = `
                <div class="category-name">
                    <div class="category-icon">${icon}</div>
                    <span>${name}</span>
                </div>
                <div class="category-time">${hours} soat ${minutes} daqiqa</div>
            `;
            container.appendChild(div);
        });

    } catch (err) {
        console.error("Xatolik yuz berdi:", err);
        container.innerHTML = "<p style='text-align:center; color:red;'>Ma’lumotni yuklashda xatolik</p>";
    }
});
