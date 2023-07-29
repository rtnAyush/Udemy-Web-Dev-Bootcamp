// here express  is imported
const express = require('express');
const app = express();

app.get("/",function(req,res){
  console.log(req);
  res.send("<h1>Hello my server</h1>");
});

app.get("/contact",function(req,res){
  res.send("contact at ayush@gmail.com");
});

app.get("/about", function(req,res){
  res.send("<h3> My name is ayush kumar</h3>");
});

app.listen(3000,function(){
  console.log("server is started at 3000 port.")
});
