document.addEventListener('DOMContentLoaded', function() {
  const pubDescriptionLinks = document.querySelectorAll('.pub-description-link');
  const pubDescriptionBoxes = document.querySelectorAll('.pub-description-box');
  const pubDescriptionCloses = document.querySelectorAll('.pub-description-close');

  pubDescriptionLinks.forEach(function(link, index) {
    link.addEventListener('click', function() {
      pubDescriptionBoxes[index].style.display = 'block';
    });
  });

  pubDescriptionCloses.forEach(function(close) {
    close.addEventListener('click', function() {
      const box = close.closest('.pub-description-box');
      box.style.display = 'none';
    });
  });
});
