---
layout: default
title: Login Page
---

<div class="login-container">
  <h2>Login</h2>
  <form id="login-form">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <button type="submit">Login</button>
    <p id="error-message" class="error"></p>
  </form>
</div>

<script>
document.getElementById('login-form').addEventListener('submit', function(event) {
  event.preventDefault();

  var email = document.getElementById('email').value.trim().toLowerCase();

  // List of allowed Emory accounts
  var allowedEmails = ['abeed@dbmi.emory.edu', 'abeed.sarker@emory.edu', 'slakama@emory.edu',
                        'sudeshnadas.ds@gmail.com', 'yuting.guo@emory.edu' ];

  if (allowedEmails.includes(email)) {
    // Redirect to selection page upon successful login
    window.location.href = '/menu.html'; // Replace with your actual selection page URL
  } else {
    document.getElementById('error-message').textContent = 'Invalid email.';
  }
});
</script>
