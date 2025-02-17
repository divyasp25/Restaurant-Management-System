const statusCells = document.querySelectorAll('td[id^="status"]');  // Select all status cells
const actionButtons = document.querySelectorAll('button[id^="actionButton"]');  // Select all action buttons
console.log("cnjdv")
// Loop through status cells and corresponding buttons
  const statusCell = statusCells[item];
  const actionButton = actionButtons[item];

  if (statusCell.textContent === " ") {
    console.log("vnjfv")
    actionButton.disabled = true;  // Disable button if status is empty
  } else {
    console.log("dcdc")
    actionButton.disabled = false;  // Enable button if status is not empty
  }
