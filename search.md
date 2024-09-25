---
layout: default
title: Search Page
---

<h1>Search subreddits</h1>

<form id="search-form">
    <label for="search-input">Search for:</label>
    <input type="text" id="search-input" name="search-input">
    <button type="submit">Search</button>
</form>

<div id="search-results">
    <!-- Search results will be displayed here -->
</div>


<script>
document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var searchTerm = document.getElementById('search-input').value.toLowerCase();
    
    // Fetch JSON data and perform search
    fetch('/subreddits_list_2024.json') // Adjust the path as per your actual file location
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Fetched JSON data:', data); // Log the fetched data to console
            var resultsHtml = '';
            data.forEach(doc => {
                // Check if 'types' is a string and contains the search term
                if (typeof doc.subreddit === 'string' && doc.subreddit.toLowerCase().includes(searchTerm)) {
                    resultsHtml += `<p> ${doc.subreddit}</p>`;
                }
                // Check if 'types' is an array of strings and any element contains the search term
                else if (Array.isArray(doc.subreddit) && doc.subreddit.some(type => type.toLowerCase().includes(searchTerm))) {
                    resultsHtml += `<p> ${doc.subreddit.join(', ')}</p>`;
                }
            });
            document.getElementById('search-results').innerHTML = resultsHtml;
        })
        .catch(error => console.error('Error fetching JSON:', error));
});
</script>
