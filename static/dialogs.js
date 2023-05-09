const loginButton = document.getElementById('loginButton');
const loginDialog = document.getElementById('loginDialog');
const editButton = document.getElementById('editButton');
const editDialog = document.getElementById('editDialog');


loginButton.addEventListener('click', () => {
    loginDialog.showModal();
});

emailConfirmBtn.addEventListener('click', (event) => {
    favDialog.close();
});

editButton.addEventListener('click', () => {
    editButton.showModal();
});

editConfirmBtn.addEventListener('click', (event) => {
    editDialog.close();
});

