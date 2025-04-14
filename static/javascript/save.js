document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('submit', async (e) => {
        const form = e.target;

        if (form.querySelector('input[name="save_flight"]')) {
            e.preventDefault();

            const formData = new FormData(form);

            try {
                const response = await fetch('', {
                    method: 'POST',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                    },
                    body: formData
                });

                const result = await response.json();

                if (result.status === 'ok') {
                    const button = form.querySelector('button');
                    const feedback = form.querySelector('#save-feedback');
                    
                    if (button && feedback) {
                        feedback.style.display = 'block';
                        feedback.scrollIntoView({ behavior: 'smooth', block: 'center' });

                        button.style.display = 'none';
                    }
                } else if (result.status === 'unauthorized') {
                    window.location.href = '/login';
                }

            } catch (error) {
                console.error('Save error:', error);
            }
        }
    });
});
