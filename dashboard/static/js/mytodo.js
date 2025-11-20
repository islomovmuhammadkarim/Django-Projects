document.addEventListener('DOMContentLoaded', () => {
    const todoItems = document.querySelectorAll('.todo-item');

    todoItems.forEach(item => {
        const todoId = item.dataset.id;
        const checkbox = item.querySelector('.todo-checkbox');

        checkbox.addEventListener('click', (e) => {
            e.stopPropagation();

            fetch(`/toggle/${todoId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(res => res.json())
            .then(data => {
                checkbox.classList.toggle('checked', data.completed);
                item.classList.toggle('completed', data.completed);
            })
            .catch(err => console.error(err));
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
