document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('search-form').addEventListener('submit', function (event) {
        event.preventDefault();
        var searchTerm = document.getElementById('search-input').value.trim().toLowerCase();

        fetch('/assets/test1.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                var keywordsContainer = document.getElementById('keywords-container');
                var tableBody = document.querySelector('#data-table tbody');

                // Clear existing keywords and table rows
                keywordsContainer.innerHTML = '';
                tableBody.innerHTML = '';

                // Find matching drug and display keywords
                var matchedDrug = data.find(drug => drug.drug.toLowerCase() === searchTerm);
                if (matchedDrug) {
                    var keywords = matchedDrug.keywords || []; // Assuming keywords is an array in each drug object

                    if (keywords.length > 0) {
                        var keywordsText = keywords.join(', ');
                        keywordsContainer.innerHTML = `<strong>Keywords used:</strong> ${keywordsText}<br><br>`;
                    }

                    // Function to create table row for each year's data
                    function createTableRow(year, monthData) {
                        var row = document.createElement('tr');
                        row.innerHTML = `<td>${year}</td>`;
                        for (var month = 1; month <= 12; month++) {
                            var monthKey = month.toString().padStart(2, '0');
                            row.innerHTML += `<td>${monthData[monthKey] || 0}</td>`;
                        }
                        return row;
                    }

                    // Populate table with yearly sales data
                    Object.keys(matchedDrug).forEach(year => {
                        if (year !== 'drug' && year !== 'id' && year !== 'keywords') {
                            var row = createTableRow(year, matchedDrug[year]);
                            tableBody.appendChild(row);
                        }
                    });
                } else {
                    keywordsContainer.innerHTML = '<strong>Keywords used:</strong> No matching drug found.';
                }

                // If no matching drug found
                if (tableBody.innerHTML === '') {
                    tableBody.innerHTML = '<tr><td colspan="13">No matching records found.</td></tr>';
                }
            })
            .catch(error => console.error('Error fetching JSON:', error));
    });
});
