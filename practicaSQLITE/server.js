/* Esta funcion devuelve una promesa que tiene que devolver toda la tabla de peliculas*/
const data = function () {
    const sqlite = new require('sqlite3')
    var sql = ""
    return new Promise((resolve, reject) => {
        const db = new sqlite.Database('./imdb.db', sqlite.OPEN_READWRITE, (error) => {
            if (error) {
                console.error('Error al intentar abrir la base de datos: ' + error.message)
                reject(error)
            } else {
                console.log('La base de datos fue abierta')
            }
        })

        sql = `
            SELECT * FROM Movie
        `

        db.all(sql, [], (error, rows) => {
            if (error) {
                console.error('Error al intentar leer datos: ' + error.message)
                reject(error)
            } else {
                let json = JSON.stringify(rows)
                resolve(json)
            }
        })
    })
}

//Muestro por consola que los datos fueron extraidos correctamente
data().then(result => {
    console.log(result)
})

// Uso de Path y express
const path = require('path')
const express = require('express')
const app = express()

//Establesco el sevidor local localhost:3000
app.listen(3000, () => { console.log("Escuchando el puerto 3000") })

//En la ruta por defecto establezco mi pagina index.html
app.get('/', (request, response) => {
    response.sendFile(path.resolve(__dirname, 'index.html'))
})

//Establesco una ruta en donde envio el JSON con los datos de la tabla Movie
app.get('/data', (request, response) => {
    data().then(result => {
        response.json(JSON.parse(result));
    }).catch(error => {
        console.error(error);
        response.status(500).send('Hubo un error al obtener los datos');
    });
})
