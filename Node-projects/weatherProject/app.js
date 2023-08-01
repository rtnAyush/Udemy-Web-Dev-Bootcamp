const express = require('express');
const https = require('https');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req,res){
  res.sendFile( __dirname + "/index.html");
});

app.post("/", function(req,res){

  const city = req.body.city;
  const apiKey = "c64db01b466768cbeb69930bf9eeaa81";
  const unit = "metric";
  const url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+ apiKey +"&units=" + unit;

  // making get request from Open weather api server
  https.get(url , function(response){

    // fetching data from server
    response.on("data" , function(data){

      // parsing hex returned data into Json object
      const weatherData = JSON.parse(data);

      // now extrcting data from weatherData object as per need
      const temp = weatherData.main.temp;
      const weatherDiscription = weatherData.weather[0].description;
      const icon = weatherData.weather[0].icon;

      // getting weather icon as per need from weather server
      const imageUrl = 'https://openweathermap.org/img/wn/' + icon + '@2x.png';

      // organiging all response data as per choice
      res.write("<p> The discription of weather is " + weatherDiscription + "</p>");
      res.write("<h1>The temprature of the "+ city +" is " + temp + " degrees Celcius.</h1>");
      res.write("<img src = " + imageUrl + " >");

      // sending all written code at once
      res.send();
    })
  });


});

app.listen(3000,function(){
  console.log("server is started.");
});
