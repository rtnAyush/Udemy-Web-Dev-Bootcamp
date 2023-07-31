const express = require('express');
const bodyParser = require('body-parser');
const date = require(  __dirname + '/date.js' );


const app = express();

app.use(bodyParser.urlencoded({ extended:true }));

app.use(express.static("public"));
// installing ejs
app.set('view engine', 'ejs');

let items = ["Buy Food","Cook Food","Eat Food"];
let workItems = [];

app.get("/", function(req,res){

  let day = date.getDate();

  res.render('list', {
    listHeading: day,
    newListItems: items
    });

});

app.get("/work", function(req,res){

  res.render('list', {
    listHeading: "Work",
    newListItems: workItems
  });

});

app.get("/about", function(req,res){

  res.render('about');
});

app.post("/", function(req,res){

  let item = req.body.newItem;

  if (req.body.list === "Work") {
    workItems.push(item);
    res.redirect('/work');
  } else {
    items.push(item);
    res.redirect("/");
  }

});


app.listen(3000, function(req){
  console.log('Srever is started at port 3000');
});
