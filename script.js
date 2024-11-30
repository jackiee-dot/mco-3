document.getElementById('admissionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const program = document.getElementById('program').value;
    document.getElementById('admissionResponse').innerText = `Thank you, ${name}. Your application for ${program} has been received. We will contact you at ${email}.`;
    document.getElementById('admissionForm').reset();
});

// Mobile menu toggle
const mobileMenu = document.getElementById('mobile-menu');
const navUl = document.querySelector('header nav ul');

mobileMenu.addEventListener('click', function() {
    navUl.classList.toggle('active');
    mobileMenu.classList.toggle('active');
});
