document.addEventListener('DOMContentLoaded', function() {

  // 1️⃣ Ripple effect for buttons
  const buttons = document.querySelectorAll('button');
  
  buttons.forEach(button => {
    button.addEventListener('click', function(e) {
      const ripple = document.createElement('span');
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size / 2;
      const y = e.clientY - rect.top - size / 2;

      ripple.style.width = ripple.style.height = size + 'px';
      ripple.style.left = x + 'px';
      ripple.style.top = y + 'px';
      ripple.classList.add('ripple');

      this.appendChild(ripple);

      setTimeout(() => ripple.remove(), 600);
    });
  });

  // 2️⃣ Clipboard hover effect
  const clipboard = document.querySelector('.clipboard');

  if (clipboard) {
    clipboard.addEventListener('mouseenter', function() {
      this.style.transform = 'rotate(-2deg) scale(1.05)';
      this.style.transition = 'transform 0.3s ease';
    });
    
    clipboard.addEventListener('mouseleave', function() {
      this.style.transform = 'rotate(-5deg) scale(1)';
    });
  }

  // 3️⃣ Smooth scrolling / navigation
  const navLinks = document.querySelectorAll('.nav-link');

  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      // Agar link # bo‘lsa scroll yoki SPA ishlatish
      if (this.getAttribute('href') === '#') {
        e.preventDefault();
        console.log('Navigation clicked:', this.textContent);
      }
      // Agar real Django link bo‘lsa, default navigation ishlaydi
    });
  });

});

// 4️⃣ CSS for ripple effect
const style = document.createElement('style');
style.textContent = `
  button {
    position: relative;
    overflow: hidden;
  }

  .ripple {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    transform: scale(0);
    animation: ripple-animation 0.6s linear;
    pointer-events: none;
  }

  @keyframes ripple-animation {
    to {
      transform: scale(4);
      opacity: 0;
    }
  }
`;
document.head.appendChild(style);
