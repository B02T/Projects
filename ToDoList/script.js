const btnAddToDo = document.getElementById('#addToDo');
const toDoContainer = document.getElementById('#toDoContainer');
const inputField = document.getElementById('#inputField');

btnAddToDo.addEventListener('click', () => {
    var paragraph = document.createElement('p');
    paragraph.classList.add('paragraph-styling')
    paragraph.innerText = inputField.value;
    toDoContainer.appendChild(paragraph)
});