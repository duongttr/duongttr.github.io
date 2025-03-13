document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript loaded!"); // Check if script runs

  document.body.addEventListener("click", function (event) {
    if (event.target.classList.contains("toggle-btn")) {
      event.preventDefault(); // Prevent page jump

      const text = event.target.previousElementSibling; // Get text <p>
      
      if (text.classList.contains("expanded")) {
        text.classList.remove("expanded");
        event.target.textContent = "Show More";
        event.target.setAttribute("data-state", "collapsed"); // Set state for CSS
      } else {
        text.classList.add("expanded");
        event.target.textContent = "Show Less";
        event.target.setAttribute("data-state", "expanded"); // Set state for CSS
      }
    }
  });
});