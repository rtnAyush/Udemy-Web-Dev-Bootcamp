import mainData from "../data/allData";

const colourArr = ['green', 'yellow', 'red', 'red', 'red', 'red', 'red', 'red', 'red'];
// const randomColor = ['g', 'y', 'r', 'b', 'p', 'o'];

const mainBox = document.querySelector('.wrapper');
var box, innerBox, inner2Box;

var upperBox = document.createElement('h1');
upperBox.innerHTML = mainData.description + " in <span class='big' > " + mainData.challengeYear + "</span>";
mainBox.appendChild(upperBox);
setInterval(function() {
  const randomColor = Math.floor(Math.random()*16777215).toString(16);
  document.querySelector('span').style.color = '#' + randomColor;
}, 1000);


for (var i = 0; i < mainData.challenges.length; i++) {

  box = document.createElement('div');
  box.classList.add('box');

  box.classList.add(colourArr[i]);
  mainBox.appendChild(box);

  innerBox = document.createElement('div');
  innerBox.innerHTML = "<a href= " + mainData.challenges[i].githubUrl + "> " + mainData.challenges[i].name + " </a>";
  box.appendChild(innerBox);

  innerBox = document.createElement('details');
  box.appendChild(innerBox);
  inner2Box = document.createElement('summary');
  inner2Box.innerHTML = mainData.challenges[i].topics[0];
  innerBox.appendChild(inner2Box);

  for (var j = 1; j < mainData.challenges[i].topics.length; j++) {

    inner2Box = document.createElement('p');
    inner2Box.innerHTML = mainData.challenges[i].topics[j];
    inner2Box.style.textAlign = 'left';
    innerBox.appendChild(inner2Box);

  }

  innerBox = document.createElement('div');
  innerBox.innerHTML = mainData.challenges[i].status;
  box.appendChild(innerBox);

}

box = document.createElement('h1');
box.innerHTML = mainData.author.firstName + " " + mainData.author.lastName;
mainBox.appendChild(box);

box = document.createElement('div');
box.innerHTML = mainData.author.bio;
mainBox.appendChild(box);


// sills and  qualification area
box = document.createElement('div');
box.classList.add('box');
box.style.textAlign = 'left';
mainBox.appendChild(box);

// Titles
innerBox = document.createElement('div');
innerBox.innerHTML = "<h3>Titles</h3>";
box.appendChild(innerBox);

for (var j = 0; j < mainData.author.titles.length; j++) {

  inner2Box = document.createElement('div');
  inner2Box.innerHTML = mainData.author.titles[j][0] + "   " + mainData.author.titles[j][1];
  innerBox.appendChild(inner2Box);

}

// Skills
innerBox = document.createElement('div');
innerBox.innerHTML = "<h3>Skills</h3>";
box.appendChild(innerBox);

for (var j = 0; j < mainData.author.skills.length; j++) {

  inner2Box = document.createElement('div');
  inner2Box.innerHTML = "&#9989;  " + mainData.author.skills[j];
  innerBox.appendChild(inner2Box);

}

// qualifications
innerBox = document.createElement('div');
innerBox.innerHTML = "<h3>Qualifications</h3>";
box.appendChild(innerBox);

for (var j = 0; j < mainData.author.qualifications.length; j++) {

  inner2Box = document.createElement('div');
  inner2Box.innerHTML = mainData.author.qualifications[j];
  innerBox.appendChild(inner2Box);

}

// keywords area

box = document.createElement('div');
box.innerHTML = "<h3>Keywords</h3>";
box.style.textAlign = 'left';
mainBox.appendChild(box);

innerBox = document.createElement('div');
innerBox.classList.add('box');
box.appendChild(innerBox);

for (var i = 0; i < mainData.keywords.length; i++) {

  const randomColor = Math.floor(Math.random()*16777215).toString(16);
  inner2Box = document.createElement('div');
  inner2Box.classList.add('key-box');
  inner2Box.style.backgroundColor = "#" + randomColor;
  inner2Box.innerHTML = "#" + mainData.keywords[i];
  innerBox.appendChild(inner2Box);
}
