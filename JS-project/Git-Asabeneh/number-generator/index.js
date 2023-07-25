

document.querySelector('button').addEventListener('click', function (e) {
    const prevData = document.querySelectorAll('.box');

    const n = Number(document.querySelector('#number').value);

    const numArea = document.querySelector('#num-area');

    console.log(prevData.length);
    if (prevData.length != 0) {
        for (let i = 0; i < prevData.length; i++) {

            numArea.removeChild(prevData[i]);

        }
    }

    let numBox;
    for (let i = 0; i <= n; i++) {

        numBox = document.createElement('div');
        numBox.classList.add('box');
        numBox.classList.add('col');
        numBox.innerHTML = i;

        if (isPrime(i) == 1) {
            numBox.classList.add('red');

        }
        else if ((i) % 2 == 0) {
            numBox.classList.add('green');

        } else {
            numBox.classList.add('yellow');

        }
        numArea.appendChild(numBox);

    }
});

var isPrime = (num) => {
    if (num == 1 || num == 0) {
        return 0;
    }
    for (let i = 2; i <= num / 2; i++) {

        if (num % i == 0) {
            return 0;
        }
    }
    return 1;
}