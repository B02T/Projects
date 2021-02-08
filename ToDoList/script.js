let btn = document.querySelector('#btn');
const toDoContainer = document.getElementById('toDoContainer');
const inputField = document.getElementById('inputField');

btn.addEventListener("click", function() {
    console.log('click');
    let paragraph = document.createElement('p');
    paragraph.classList.add('paragraph')
    paragraph.innerText = inputField.value;
    toDoContainer.appendChild(paragraph);
    inputField.value = "";
    paragraph.addEventListener('click', function(){
        paragraph.style.textDecoration = "line-through";

    });
    paragraph.addEventListener('dblclick', function(){
        toDoContainer.removeChild(paragraph);
    });
});