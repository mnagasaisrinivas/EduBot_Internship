document.getElementById('darkModeToggle').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

document.getElementById('feedbackForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const form = this;
    if (!form.checkValidity()) {
        e.stopPropagation();
    } else {
        alert('Feedback submitted successfully!');
        form.reset();
    }
    form.classList.add('was-validated');
});
