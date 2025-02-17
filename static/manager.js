const navItems = document.querySelectorAll('.nav-item');
const contentDiv = document.getElementById('content');

navItems.forEach(item => {
    item.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default navigation

        const url = item.getAttribute('href');

        // Use AJAX (fetch) to fetch content from Flask
        fetch(url)
            .then(response => response.text())
            .then(html => {
                contentDiv.innerHTML = html; // Replace content
            })
            .catch(error => {
                console.error('Error fetching content:', error);
                // Handle errors appropriately
            });
    });
});
