const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({extended : true}));

app.get("/",function(req,res){

  res.sendFile(__dirname + "/index.html");

});

app.post("/", function(req,res){

  var num1 = Number(req.body.num1);
  var num2 = Number(req.body.num2);

  var result = num1 + num2;

  res.send("The result is : " + result);
});

app.get("/bmicalculator", function(req,res){

  res.sendFile(__dirname + "/bmiCalculator.html");

});

app.post("/bmicalculator", function(req,res){

  var w = parseFloat(req.body.w);
  var h = parseFloat(req.body.h);

  var bmi = w / (h*h);

  res.send("<h1>BMI CALCULATOR </h1> <h2> Your bmi is : "+ bmi +"</h2>");

});

app.listen(3000, function(){
  console.log("server is started");
});
