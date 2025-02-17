const addButtons = document.querySelectorAll('.add-button');
const selectedItemsElement = document.getElementById('selected-items');

let selectedItems = [];

addButtons.forEach(button => {
    button.addEventListener('click', () => {
        const itemName = button.parentNode.querySelector('h2').textContent;

        if (button.classList.contains('added')) {
            button.classList.remove('added');
            button.textContent = 'Add';
            selectedItems = selectedItems.filter(item => item !== itemName);
        } else {
            button.classList.add('added');
            button.textContent = 'Added';
            selectedItems.push(itemName);
        }

        selectedItemsElement.textContent = `Selected Items: ${selectedItems.join(', ')}`;
    });
});



  
const registrationForm = document.getElementById('registration-form');
const errorMessage = document.getElementById('error-message');
registrationForm.addEventListener('submit', (event) => {
    event.preventDefault(); 
    if (selectedItems.length === 0) {
        errorMessage.textContent = "Please select an item!";
      } else {
    fetch('/welcome', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(selectedItems)
    })// Prevent form submission
        
        // Simulate successful addition to cart
        // You would replace this with your actual logic to add items to the cart
        const successMessage = 'Successfully added to cart. <a href="/cart" style="color:#587621;"><b>View Cart</b></a>';
        
        // Update the content of the error-message element with the success message
        errorMessage.innerHTML = successMessage;}
    });

