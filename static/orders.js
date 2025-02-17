function calculateColumnSum(tableElement, columnIndex) {
    let sum = 0;
    const rows = tableElement.querySelectorAll("tr"); // Get all rows in the table

    for (const row of rows) {
      const cells = row.querySelectorAll("td, th"); // Get all cells in the row (including headers)
      const targetCell = cells[columnIndex]; // Get the cell at the specified index

      if (targetCell) {
        const value = parseFloat(targetCell.textContent); // Extract numeric value
        sum += value;
      }
    }

    return sum;
  }

  const table = document.querySelector("table"); // Get reference to the table
  const columnIndex = 1; // Assuming you want to sum the second column (index starts at 0)

  if (table) {
    const columnTotal = calculateColumnSum(table, columnIndex);
    const totalDisplay = document.getElementById("total-display");
    totalDisplay.textContent = `Total: $${columnTotal.toFixed(2)}`; // Display total with 2 decimal places
  } else {
    console.error("Could not find table element");
  }
  function submitPayment() {
  const paymentMethod = document.getElementById("paymentMethod").value;

  // Simple validation (optional)
  if (paymentMethod === "") {
    alert("Please select a payment method.");
    return;
  }

  // Prevent default form submission behavior
  event.preventDefault();

  // AJAX request to send data to app.py
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/app.py");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  // Prepare form data (URL-encoded)
  const formData = "paymentMethod=" + encodeURIComponent(paymentMethod);

  // Handle the response from app.py
  xhr.onload = function() {
    if (xhr.status === 200) {
      alert("Payment method submitted successfully: " + xhr.responseText);
    } else {
      alert("Error submitting payment: " + xhr.statusText);
    }
  };

  // Send the request
  xhr.send(formData);
}
