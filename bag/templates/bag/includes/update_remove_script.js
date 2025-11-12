<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Update quantity on click
        const updateLinks = document.querySelectorAll('.update-link');
        updateLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const form = this.previousElementSibling;
                console.log('Update clicked, form found:', form);
                if (form && form.classList.contains('update-form')) {
                    form.submit();
                }
            });
        });

        // Remove item and reload on click
        const removeLinks = document.querySelectorAll('.remove-item');
        removeLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const csrfToken = "{{ csrf_token }}";
                const itemId = this.id.split('remove_')[1];
                const url = `/bag/remove/${itemId}/`;

                console.log('Remove clicked, itemId:', itemId, 'url:', url);

                fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': csrfToken
                    },
                    body: 'csrfmiddlewaretoken=' + csrfToken
                })
                .then(function(response) {
                    if (response.ok) {
                        location.reload();
                    } else {
                        console.error('Error removing item:', response.status);
                    }
                })
                .catch(function(error) {
                    console.error('Error removing item:', error);
                });
            });
        });
    });
</script>