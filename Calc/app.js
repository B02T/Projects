const submit = document.querySelector('#btn');
const wrapper = document.querySelector('.wrapper');
function parser(n){
    return parseFloat(n);
}

submit.addEventListener('click', () => {
    let value = document.querySelector('#value').value;
    let percentage = document.querySelector('#percentage').value;
    const total = parser((value - percentage) / value * 100).toFixed(3);
    const print = document.createElement("h3")
    print.innerHTML = total.toString() + " %";
    let child = document.body.appendChild(print);
    wrapper.appendChild(child);

});


