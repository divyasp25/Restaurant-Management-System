const tableBody = document.getElementById("myTable").querySelector("tbody");
let slrNo = 1; // Counter for SLR numbers

function addRow() {
  const row = document.createElement("tr");
  row.innerHTML = `
    <td>${slrNo}</td>
    <td><input type="date" name="date"></td>
    <td><input type="number" name="amount"></td>
  `;
  tableBody.appendChild(row);

  slrNo++; // Increment SLR number for the next row
}

// Add an initial row upon page load
addRow();

// Add a button or similar trigger for adding more rows
// (replace with your preferred method)
document.getElementById("addRowButton").addEventListener("click", addRow);
