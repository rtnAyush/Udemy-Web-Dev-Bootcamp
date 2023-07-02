const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const ejs = require('ejs');

const dbUrl = "mongodb://127.0.0.1:27017/wikiDB";

const app = express();
app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended: true}));

async function main(){
  mongoose.set('strictQuery', false);
  await mongoose.connect(dbUrl);
  console.log("Mongodb is connected");
}
main();

const articleSchema = new mongoose.Schema ({
  title: String,
  content: String
});

const Article = mongoose.model("Article", articleSchema);

app.route("/articles")

.get((req,res)=>{
  Article.find((err, ariticles)=>{
    if(!err){
      res.send(ariticles);
    }
  });
})

.post((req, res)=>{

  const newArticle = new Article ({
    title : req.body.title,
    content : req.body.content
  });
  newArticle.save((err)=>{
    if(!err){
      res.send("Successfully added a new article.")
    } else {
      res.send(err);
    }
  });
})

.delete((req,res)=>{
  Article.deleteMany((err)=>{
    if (!err) {
      res.send("Successfully deleted all articles.");
    } else {
      res.send(err);
    }
  })
})

app.route("/articles/:articleTitle")

.get((req,res)=>{
  Article.findOne({title: req.params.articleTitle}, (err, foundArticle)=>{
    if (!err) {
      if (foundArticle) {
        res.send(foundArticle);
      } else {
        res.send("Article has not found")
      }
    }
  })
})

.put((req,res)=>{
  Article.updateOne(
    {title: req.params.articleTitle},
    {title: req.body.title, content: req.body.content},
    (err)=>{
      if(!err){
        res.send("Successfully updated");
      }
    }
  )
})

.patch((req, res)=>{
  Article.updateOne(
    {title: req.params.articleTitle},
    req.body,
    (err)=>{
      if (!err) {
        res.send("Updated Successfully");
      }
    }
  )
})

.delete((req, res)=>{
  Article.deleteOne({title: req.params.articleTitle}, (err)=>{
    if (!err) {
      res.send("Successfully deleted");
    }
  })
})


const port = 3000;
app.listen(port, ()=>{
  console.log(`server is started at ${port}`);
})
