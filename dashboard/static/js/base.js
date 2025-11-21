document.addEventListener('DOMContentLoaded', function () {

    /* ================================
       TODO ELEMENTLARINI TEKSHIRISH
    ================================== */
    const todoInput = document.getElementById('todoInput');
    const addTodoBtn = document.getElementById('addTodoBtn');
    const todoList = document.getElementById('todoList');

    if (todoInput && addTodoBtn && todoList) {

        function updateStats() {
            const totalTasksEl = document.getElementById('totalTasks');
            const completedTasksEl = document.getElementById('completedTasks');
            const inProgressTasksEl = document.getElementById('inProgressTasks');

            if (!totalTasksEl || !completedTasksEl || !inProgressTasksEl) return;

            const allTodos = document.querySelectorAll('.todo-item');
            const completedTodos = document.querySelectorAll('.todo-item.completed');

            totalTasksEl.textContent = allTodos.length;
            completedTasksEl.textContent = completedTodos.length;
            inProgressTasksEl.textContent = allTodos.length - completedTodos.length;
        }

        function addTodo() {
            const todoText = todoInput.value.trim();
            if (!todoText) return;

            const todoItem = document.createElement('div');
            todoItem.className = 'todo-item fade-in';

            const priorities = ['priority-high', 'priority-medium', 'priority-low'];
            const priorityTexts = ['Yuqori', "O'rta", 'Past'];
            const randomIndex = Math.floor(Math.random() * 3);

            todoItem.innerHTML = `
                <div class="todo-checkbox"></div>
                <div class="todo-text">${todoText}</div>
                <span class="todo-priority ${priorities[randomIndex]}">${priorityTexts[randomIndex]}</span>
            `;

            todoList.appendChild(todoItem);
            todoInput.value = '';
            updateStats();
        }

        addTodoBtn.addEventListener('click', addTodo);

        todoInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') addTodo();
        });

        document.addEventListener('click', function (e) {
            if (e.target.classList.contains('todo-checkbox')) {
                const checkbox = e.target;
                const todoItem = checkbox.parentElement;
                checkbox.classList.toggle('checked');
                todoItem.classList.toggle('completed');
                updateStats();
            }
        });
    }

    /* ================================
       POMODORO TIMER ELEMENTLARINI TEKSHIRISH
    ================================== */
    const startTimerBtn = document.getElementById('startTimer');
    const pauseTimerBtn = document.getElementById('pauseTimer');
    const resetTimerBtn = document.getElementById('resetTimer');
    const timerDisplay = document.getElementById('timerDisplay');

    if (startTimerBtn && pauseTimerBtn && resetTimerBtn && timerDisplay) {

        let timerInterval, minutes = 25, seconds = 0, isTimerRunning = false;

        function updateTimerDisplay() {
            const m = minutes < 10 ? '0' + minutes : minutes;
            const s = seconds < 10 ? '0' + seconds : seconds;
            timerDisplay.textContent = `${m}:${s}`;
        }

        function updateTimer() {
            if (seconds === 0) {
                if (minutes === 0) {
                    pauseTimer();
                    resetTimer();
                    return;
                }
                minutes--;
                seconds = 59;
            } else {
                seconds--;
            }
            updateTimerDisplay();
        }

        function startTimer() {
            if (!isTimerRunning) {
                isTimerRunning = true;
                timerInterval = setInterval(updateTimer, 1000);
            }
        }

        function pauseTimer() {
            clearInterval(timerInterval);
            isTimerRunning = false;
        }

        function resetTimer() {
            clearInterval(timerInterval);
            isTimerRunning = false;
            minutes = 25;
            seconds = 0;
            updateTimerDisplay();
        }

        startTimerBtn.addEventListener('click', startTimer);
        pauseTimerBtn.addEventListener('click', pauseTimer);
        resetTimerBtn.addEventListener('click', resetTimer);
    }

    /* ================================
       NAVIGATION ACTIVE
    ================================== */
    const navItems = document.querySelectorAll('.nav-item');
    if (navItems.length) {
        navItems.forEach(item => {
            item.addEventListener('click', function () {
                navItems.forEach(i => i.classList.remove('active'));
                this.classList.add('active');
            });
        });
    }

});
