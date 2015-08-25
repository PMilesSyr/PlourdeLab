// conn = new Mongo()
// db = conn.getDB("test");

db = connect("localhost:27017/test");


for(i=0; i < 10; ++i) {
 
  db.posts.insert({
    title: "A MongoDB Article"
  });
 
}