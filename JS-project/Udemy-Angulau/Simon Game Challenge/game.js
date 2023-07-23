var buttonColors = ["red", "blue", "green", "yellow"];

var userClickedPattern = [];
var gamePattern = [];

var level = -1;
var started = false;

$(document).keypress(function() {
  if (!started) {

    nextSequence();
    started = true;

  }
});

$(".btn").click(function() {

  var userChosenColour = $(this).attr('id');
  userClickedPattern.push(userChosenColour);

  playSound(userChosenColour);
  animatePress(userChosenColour);

  checkAnswer(userClickedPattern.length - 1);
});

function checkAnswer(currentLevel) {

  if (userClickedPattern[currentLevel] === gamePattern[currentLevel]) {
    console.log("success");
    if (userClickedPattern.length == gamePattern.length) {
      setTimeout(function() {
        nextSequence();
      }, 1000);
    }
  } else {
    playSound("wrong");

    $("body").addClass("game-over");

    setTimeout(function() {
      $("body").removeClass("game-over");
    }, 200);

    $("#level-title").text("Game Over, Press Any Key to Restart.");

    startOver();
  }
}

function nextSequence() {

  userClickedPattern = [];

  level++;
  $("#level-title").html("level " + level);

  var randomNumber = Math.floor(Math.random() * 4);
  var randomChosenColour = buttonColors[randomNumber];
  gamePattern.push(randomChosenColour);

  $("#" + randomChosenColour).fadeIn(100).fadeOut(100).fadeIn(100);

  playSound(randomChosenColour);

}

function startOver(){

  started = false;
  level = -1;
  gamePattern = [];
}

function playSound(name) {
  var sound = new Audio("sounds/" + name + ".mp3");
  sound.play();
}

function animatePress(currentColor) {
  $("." + currentColor).addClass("pressed");

  setTimeout(function() {

    $("." + currentColor).removeClass("pressed");
  }, 100);

};
