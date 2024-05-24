const sqlite = new require('sqlite3')
let sql = ""

const db = new sqlite.Database('./imdb.db', sqlite.OPEN_READWRITE, (error) => {
    if (error)
        console.error('Error la intentar abrir la base de datos: ' + error.message);
    else 
        console.log('La base de datos fue abierta');
})

/*sql = `
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL
    )
`

db.run(sql, (error) => {
    if (error)
        console.error('Error al intentar crear la tabla: ' + error.message);
    else 
        console.log('Tabla creada con éxito');
})

sql = `
    INSERT INTO categories (name) VALUES (?)
`

db.run(sql, ['Categoria 1'], (error) => {
    if (error)
        console.error('Error al intentar insertar datos: ' + error.message);
    else 
        console.log('Datos insertados con éxito');
})

sql = `
    UPDATE categories SET name = ? WHERE id = ?
`

db.run(sql, ['Categoria 1B', 1], (error) => {
    if (error)
        console.error('Error al intentar actualizar datos: ' + error.message);
    else 
        console.log('Datos actualizados con éxito');
})

sql = `
    DELETE FROM categories WHERE id=?
`

db.run(sql, [2], (error) => {
    if (error)
        console.error('Error al intentar eliminar datos: ' + error.message);
    else 
        console.log('Datos eliminados con éxito');
})

sql = `
    SELECT * FROM categories WHERE id=?
`

db.all(sql, [1], (error, rows) => {
    if (error)
        console.error('Error al intentar leer datos: ' + error.message);
    else 
        console.log(rows);
})

db.close((error) => {
    if (error)
        console.error('Error al intentar cerrar la base de datos: ' + error.message);
    else 
        console.log('La base de datos fue cerrada');
})*/


