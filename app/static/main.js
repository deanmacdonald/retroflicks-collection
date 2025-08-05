document.addEventListener('DOMContentLoaded', () => {
    console.log("📽️ RetroFlicks main.js loaded");

    // Autofocus on the search input field
    const searchInput = document.getElementById('query');
    if (searchInput) {
        searchInput.focus();
    }

    // Keyboard shortcut: Submit form when Enter is pressed inside search field
    const form = document.querySelector('form');
    if (form && searchInput) {
        searchInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                form.submit();
            }
        });
    }

    // Optional Enhancement: Show a loading message when form is submitted
    if (form) {
        form.addEventListener('submit', () => {
            console.log("🎬 Searching for flicks...");
        });
    }

    // Future idea: Add interactivity like random movie picker or result sorting
});

