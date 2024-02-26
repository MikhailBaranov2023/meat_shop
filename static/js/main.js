window.onload = function () {

    var data = []

    function submitButtonStyle(element) {
        element.style.backgroundColor = "red";
        data.push(+element.innerText);
        console.log(data);
        console.log(data[2]);
    }

    let order = document.getElementById('delete');
    let blockNone = document.getElementById('blockNone');
    let block = document.getElementById('dNone')

    order.onclick = function () {
        blockNone.classList.add('d-none');
        block.classList.replace('d-none', 'display');
    }


}

// _thisdocument.getElementsByClassName('.calendar-data').addEventListener('click', (event) => {
//     let value = event.target.value;
//     console.log(value)
// });

// window.addEventListener('DOMContentLoaded', () => {
//     const buttons = document.querySelectorAll('.calendar-data')
//     const rowSelector = document.querySelector('.block__row')
//     let newValues = ['2', '567', 'Т333', 'csdf', 'sdfdsggg', 'ertretret']
//
//     function changeValue(btn, newArr) {
//         for (let i = 0; i < btn.length; i++) {
//             btn[i].setAttribute('value', newArr[i])
//         }
//     }
//
//     function consoleOutput(parentSelector) {
//         parentSelector.addEventListener('click', (e) => {
//             if (!e.target.matches('button')) return
//             changeValue(buttons, newValues)
//             console.log(e.target.getAttribute('value'))
//         })
//     }
//     consoleOutput(rowSelector)
// })

// window.addEventListener('DOMContentLoaded', () => {
//
//     const buttons = document.querySelectorAll('.calendar-data')
//     let newValues = [ ]
//
//     for (let i =0; i < buttons.length; i++) {
//         buttons[i].addEventListener('click', () => {
//             buttons.forEach((item, i) => {
//                 item.setAttribute('value', newValues[i])
//             })
//             console.log(buttons[i].getAttribute('value'))
//         })
//     }
// })