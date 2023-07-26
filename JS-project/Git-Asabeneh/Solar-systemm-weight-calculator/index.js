
const sg = {
    // specific gravity wrt earth
    Sun: 27.01,
    Mercury: 0.38,
    Venus: 0.91,
    Earth: 1,
    Moon: 0.166,
    Mars: 0.38,
    Jupiter: 2.34,
    Saturn: 1.06,
    Uranus: 0.92,
    Neptune: 1.19,
    Pluto: 0.06
};

// acceration due to gravity on earth
const g = 9.8;


document.querySelector('#cal-button').addEventListener('click', function (e) {

    clearScreen();


    showWeight();

});

function showImg() {

    var planet = document.querySelector('#planet').value;

    const planetImg = document.createElement('img');
    planetImg.src = "images/" + planet + ".png";
    planetImg.classList.add("planet-img");
    document.querySelector('.image').appendChild(planetImg);

}

function showWeight() {

    var mass = document.querySelector('#mass').value;
    var planet = document.querySelector('#planet').value;

    const weight = Number(mass) * sg[planet] * g;

    const desc = document.createElement('p');
    desc.classList.add('inner-text-box');

    if (mass == '') {

        desc.innerHTML = "Mass is required.";
    } else {

        if (planet == 'none') {

            desc.innerHTML = "Planet is required.";
        } else {
            showImg();
            desc.innerHTML = "The weight of the object on <strong> " + planet + " </strong>" + "<div class='circle'> <strong class='weight' >" + weight.toPrecision(4) + " N </strong></div>";
        }
    }

    document.querySelector('.description').appendChild(desc);

}

function clearScreen() {

    const img = document.querySelectorAll('.planet-img');
    const text = document.querySelectorAll('.inner-text-box');

    if (img.length != 0) {
        document.querySelector('.image').innerHTML = ' ';
    }
    if (text.length != 0) {
        document.querySelector('.description').innerHTML = ' ';
    }
}