document.getElementById('darkModeToggle').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});


function validateForm() {
    const email = document.querySelector('input[name="email"]').value;
    const pattern = /^[^@]+@[^@]+\.[^@]+$/;
    if (!pattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }
    return true;
}
