document.addEventListener('DOMContentLoaded', function() {
    // Add any client-side functionality here
    console.log('Application loaded');
    
    // Example: Add input validation
    const form = document.querySelector('.prediction-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const inputs = form.querySelectorAll('input[type="number"]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (input.value === '' || isNaN(input.value)) {
                    isValid = false;
                    input.style.borderColor = 'red';
                } else {
                    input.style.borderColor = '#ddd';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please enter valid numbers for all fields');
            }
        });
    }
});