---
layout: default
title: Drug Lookup
---

<h1>Drug Lookup</h1>

<form id="search-form">
  <label for="search-input">Search by Drug:</label>
  <input type="text" id="search-input" name="search-input">
  <button type="submit">Search</button>
</form>

<div id="keywords-container">
  <!-- Keywords will be populated dynamically -->
</div>

<h2>Yearly Sales Data</h2>

<table id="data-table">
  <thead>
    <tr>
      <th>Year</th>
      <th>01</th>
      <th>02</th>
      <th>03</th>
      <th>04</th>
      <th>05</th>
      <th>06</th>
      <th>07</th>
      <th>08</th>
      <th>09</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
    </tr>
  </thead>
  <tbody>
    <!-- Table body will be populated dynamically -->
  </tbody>
</table>

<script src="/scripts/drug_lookup.js"></script>
