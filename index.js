let express = require("express");
let app = express();
app.set("view engine", "ejs");

app.use('/', express.static(__dirname + '/css'));


const knex = require('knex')({
    client: 'mysql2',
    connection: {
        host: '127.0.0.1',
        port: 3306,
        user: 'root',
        password: '1505Qtds',
        database: 'artistas'
    }
});

app.get('/', (req, res) => {
    res.render('pagina_principal')
})

app.get('/gustavo', (req, res) => {
    res.render('gustavo')
})

app.get('/Bruno', (req, res) => {
    knex.select()
    .from("artistas")
    .then((results) => {
        res.render("Bruno", { aArtista: results });
    });
})

app.get('/Jorge', (req, res) => {
    knex.select()
    .from("artistas")
    .then((results) => {
        res.render("jorge", { aArtista: results });
    });
})

app.get('/Jo%C3%A3o', (req, res) => {
    knex.select()
    .from("artistas")
    .then((results) => {
        res.render("joao", { aArtista: results });
    });
})



app.get("/artistas", (req, res) => {
    knex.select()
    .from("artistas")
    .then((results) => {
        res.render("displayartista", { aArtista: results });
    });

});






app.listen(3000)