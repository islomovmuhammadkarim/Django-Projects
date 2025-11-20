// DOM Elements
const todoInput = document.getElementById('todoInput');
const addTodoBtn = document.getElementById('addTodoBtn');
const todoList = document.getElementById('todoList');
const startTimerBtn = document.getElementById('startTimer');
const pauseTimerBtn = document.getElementById('pauseTimer');
const resetTimerBtn = document.getElementById('resetTimer');
const timerDisplay = document.getElementById('timerDisplay');
const totalTasksEl = document.getElementById('totalTasks');
const completedTasksEl = document.getElementById('completedTasks');
const inProgressTasksEl = document.getElementById('inProgressTasks');

// Timer variables
let timerInterval;
let minutes = 25;
let seconds = 0;
let isTimerRunning = false;

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    // HTML-dagi oldindan yuklangan vazifalar asosida statistikani yangilash
    updateStats();
    setupEventListeners();
});

// Setup Event Listeners
function setupEventListeners() {
    // Todo functionality
    addTodoBtn.addEventListener('click', addTodo);
    todoInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            addTodo();
        }
    });

    // Delegatsiya: todo checkbox click
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('todo-checkbox')) {
            toggleTodoItem(e.target);
        }
    });

    // Timer controls
    startTimerBtn.addEventListener('click', startTimer);
    pauseTimerBtn.addEventListener('click', pauseTimer);
    resetTimerBtn.addEventListener('click', resetTimer);

    // Navigation menu active state
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        item.addEventListener('click', function() {
            navItems.forEach(navItem => navItem.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

// Todo Functions
function addTodo() {
    const todoText = todoInput.value.trim();
    if (todoText === '') return;

    const todoItem = document.createElement('div');
    todoItem.className = 'todo-item fade-in';
    
    // Random priority logic
    const priorities = ['priority-high', 'priority-medium', 'priority-low'];
    const priorityTexts = ['Yuqori', "O'rta", 'Past'];
    const randomIndex = Math.floor(Math.random() * 3);
    
    todoItem.innerHTML = `
        <div class="todo-checkbox"></div>
        <div class="todo-text">${todoText}</div>
        <span class="todo-priority ${priorities[randomIndex]}">${priorityTexts[randomIndex]}</span>
    `;
    
    todoList.prepend(todoItem); // Yangi vazifani tepaga qo'shamiz
    todoInput.value = '';
    updateStats();
}

function toggleTodoItem(checkbox) {
    const todoItem = checkbox.parentElement;
    const isCompleted = checkbox.classList.contains('checked');
    
    if (isCompleted) {
        checkbox.classList.remove('checked');
        todoItem.classList.remove('completed');
    } else {
        checkbox.classList.add('checked');
        todoItem.classList.add('completed');
    }
    
    updateStats();
}

function updateStats() {
    const allTodos = document.querySelectorAll('.todo-item');
    const completedTodos = document.querySelectorAll('.todo-item.completed');
    
    totalTasksEl.textContent = allTodos.length;
    completedTasksEl.textContent = completedTodos.length;
    inProgressTasksEl.textContent = allTodos.length - completedTodos.length;
}

// Timer Functions
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

function updateTimer() {
    if (seconds === 0) {
        if (minutes === 0) {
            // Timer completed
            pauseTimer();
            showNotification("Pomodoro taymer tugadi! Dam olish vaqti.");
            // Agar avtomatik ravishda dam olish vaqtiga o'tishni xohlasangiz, bu yerga kod yozing
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

function updateTimerDisplay() {
    const formattedMinutes = minutes < 10 ? `0${minutes}` : minutes;
    const formattedSeconds = seconds < 10 ? `0${seconds}` : seconds;
    timerDisplay.textContent = `${formattedMinutes}:${formattedSeconds}`;
}

// Notification function
function showNotification(message) {
    // Create notification element
    const notification = document.createElement('div');
    notification.style.position = 'fixed';
    notification.style.bottom = '20px';
    notification.style.right = '20px';
    notification.style.backgroundColor = '#333333';
    notification.style.color = 'white';
    notification.style.padding = '15px 20px';
    notification.style.borderRadius = '8px';
    notification.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.2)';
    notification.style.zIndex = '1000';
    notification.style.transition = 'opacity 0.5s ease';
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 500);
    }, 3000);
}