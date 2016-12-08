CREATE DATABASE estrenos;

USE estrenos;

CREATE TABLE peliculas(
	id int auto_increment PRIMARY KEY,
    titulo VARCHAR(50)  NOT NULL,
    titulo_original VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    nacionalidad VARCHAR(50) NOT NULL,
	anio VARCHAR(50) NOT NULL,
    director VARCHAR(50) NOT NULL,
    guion VARCHAR(50) NOT NULL, 
    fecha_estreno VARCHAR(50) NOT NULL
);

CREATE TABLE users (
	pw VARCHAR(10) NOT NULL PRIMARY KEY,
    username VARCHAR(25) COLLATE latin1_spanish_ci NOT NULL
);

INSERT INTO users VALUES('mikei0908','KeeiSoto');

SELECT * FROM users;

INSERT INTO peliculas VALUES(1,'Nacido en Siria', 'Nacido en Siria', 'Documenal', 'España', 2016, 'Hernan Zin', 'Jose F. Ortuno', '2017/01/12');
INSERT INTO peliculas VALUES(2,'La Autopsia de Jane Doe', 'The Autopsy of Jane Doe', 'Terror', 'Reino unido', 2016, 'Andre Ovredal', 'Ian B. Goldberg', '2017/01/13');
INSERT INTO peliculas VALUES(3,'Underworld: Guerras de Sangre', 'Underworld: Blood Wars', 'Terror', 'USA', 2016, 'Anna foerster', 'Cory Goodman', '2017/01/12');    
INSERT INTO peliculas VALUES(4,'Resident Evil: El Capitulo final', 'Resident Evil: The Final Chapter', 'Accion', 'Alemnia', 2017, 'Paul WS Anderson', 'Paul WS Anderson', '2017/02/03');
INSERT INTO peliculas VALUES(5,'Cincuenta Sombras  Mas Oscuras', 'Fifty Shades Darker', 'Drama', 'USA', 2017, 'James Foley', 'Niall Leonard', '2017/02/10');
INSERT INTO peliculas VALUES(6,'La Gran Muralla', 'the Great Wall', 'Msterio', 'USA', 2017, 'Zhang Yimou', 'Thomas Tull', '2017/02/17');
INSERT INTO peliculas VALUES(7,'La Bella y la Bestia', 'Beauty an the Beast', 'Fantasia', 'USA', 2017, 'Bill Condon', 'Stephen Chbosky', '2017/03/17');
INSERT INTO peliculas VALUES(8,'Ghost in the Shell', 'Ghost in the Shell', 'Accion', 'USA', 2017, 'Rupert Sanders', 'William Wheeler', '2017/03/31');
INSERT INTO peliculas VALUES(9,'Dia de Patriotas', 'Patriots Day', 'Drama', 'USA', 2016, 'Peter Berg', 'Eric Johnson', '2017/04/00');
INSERT INTO peliculas VALUES(10,'Power Rangers', 'Power Rangers', 'Accion', 'USA', 2017, 'Dean Israelite', 'Ashley Miller', '2017/04/00');
INSERT INTO peliculas VALUES(11,'Fast 8', 'Fast & Furious 8', 'Accion', 'USA', 2017, 'F. Gray Gray', 'Chris Morgan', '2017/04/14');
INSERT INTO peliculas VALUES(12,'Piratas del Caribe: La Venganza de Salazar', 'Pirates of the Caribbean: Dead Men Tell No Tales', 'Aventuras', 'USA', 2017, 'Joachim Ronning', 'Jeff Nathanson', '2017/05/01');
INSERT INTO peliculas VALUES(13,'Star Wars: Episodio VIII', 'Star Wars: Episode VIII', 'Aventura', 'USA', 2017, 'Rian Johnson', 'Rian Johnson', '2017/05/26');
INSERT INTO peliculas VALUES(14,'La Momia', 'The Mummy', 'Accion', 'USA', 2017, 'Alex Kurtzman', 'Jon Spaihts', '2017/05/09');
INSERT INTO peliculas VALUES(15,'Guerra Mundial Z 2', 'World War Z 2', 'Accion', 'USA', 2017, 'Juan Antonio Bayona', ' 6ennis Kelly', '2017/06/09');
INSERT INTO peliculas VALUES(16,'Mujer Maravilla', 'Wonder Woman', 'Aventuras', 'USA', 2017, 'Patty Jenkins', 'Michael Goldenberg', '2017/06/23');
INSERT INTO peliculas VALUES(17,'Annabelle 2', 'Annabelle 2', 'Terror', 'USA', 2017, 'David F. Sendberg', 'Gary Dauberman', '2017/06/30');
INSERT INTO peliculas VALUES(18,'Valerian y la Ciudad de los mil planetas', 'Valerian and the City of a Thousand Planet', 'Ciencia Ficcion', 'Francia', 2017, 'Luc Besson', 'Luc Besson', '2017/06/03');
INSERT INTO peliculas VALUES(19,'Cars 3', 'Cars 3', 'Animacion', 'USA', 2017, 'Brian Fee', 'Brian Fee', '2017/07/16');
INSERT INTO peliculas VALUES(20,'Solo se vive una vez', 'Solo se vive una vez', 'Accion', 'Argentina', 2017, 'Federico Cueva', 'Nicolas Allegro', '2017/07/18');
INSERT INTO peliculas VALUES(21,'Dunkerque', 'Dunkirk', 'Accion', 'Reino Unido', 2017, 'Christopher Nolan', 'Chirstopher Nolan', '2017/07/21');
INSERT INTO peliculas VALUES(22,'Transformers: El Ultimo Caballero', 'Transformers: The Last Knight', 'Accion', 'USA', 2017, 'Michael Bay', 'Andrew Barrer', '2017/07/28');
INSERT INTO peliculas VALUES(23,'La Torre Oscura', 'The dark Tower', 'Aventuras', 'USA', 2017, 'Nikolaj Arcel', 'Akiva Goldsman', '2017/08/04');
INSERT INTO peliculas VALUES(24,'Tadeo Jones 2: El Secreto del Rey Midas', 'Tadeo Jones 2: The Hero Returns', 'Animacion', 'España', 2017, 'Enrique Gato', 'Jordi Gasull', '2017/08/25');
INSERT INTO peliculas VALUES(25,'It', 'It', 'Terror', 'USA', 2017, 'Andres Muschietti', 'Chase Palmer', '2017/09/08');
INSERT INTO peliculas VALUES(26,'Ninjago 3D', 'Ninjago 3D', 'Animacion', 'USA', 2016, 'Charlie Bean', 'Kevin Chesley', '2017/09/22');
INSERT INTO peliculas VALUES(27,'Blade Runner 2', 'Blade Runner 2', 'Ciencia Ficcion', 'USA', 2017, 'Ridley Scott', 'Hampton Fancher', '2017/10/06');
INSERT INTO peliculas VALUES(28,'Geostorm 3D', 'Geostorm 3D', 'Accion', 'USA', 2016, 'Dean Devlin', 'Paul Guyot', '2017/10/20');
INSERT INTO peliculas VALUES(29,'Thor: Ragnarok', 'Thor: Ragnarok', 'Accion', 'USA', 2017, 'Craig Kyle', 'Christopher Yost', '2017/11/07');
INSERT INTO peliculas VALUES(30,'Toy Story 4', ' Toy Story 4', 'Animacio', 'Animacion', 2017, 'John Lasseter', 'John Lasseter', '2018/01/01');
INSERT INTO peliculas VALUES(31,'Black Panther', 'Black panther', 'Ciencia Ficcioin', 'USA', 2018, 'F. Gary Gray', ' Mark Baily', '2018/02/10');
INSERT INTO peliculas VALUES(32,'Tomb Raider', 'Tomb Raider', 'Accion', 'USA', 2018, ' Roar Uthaug', 'Ginebra robertson-Dworet', '2018/03/18');
INSERT INTO peliculas VALUES(33,'Scooby-Doo', 'Scooby-Doo', 'Animacio', 'USA', 2018, 'Tony Cervone', 'Matt Lieberman', '2017/10/11');
INSERT INTO peliculas VALUES(34,'El Libro de la Selva: Origenes', 'The Jungle Book: Origins', 'Drama', 'USA', 2018, 'Andy Serkis', 'Callie Kloves', '2018/10/19');
INSERT INTO peliculas VALUES(35,'Animales Fantasticos y Donde Encontralos 2', 'Fantastic Beasts an Where to Find Them 2', 'Aventuras', 'Reino Unido', 2018, ' David Yates', 'JK Rowling', '2018/11/16');
INSERT INTO peliculas VALUES(36,'Avatar 2', 'Avatar 2', 'Aventuras', 'USA', 2018, 'James Cameron', 'James Cameron', '2018/12/15');
INSERT INTO peliculas VALUES(37,'El Regreso de Mary Poppins', 'Mary Poppins Returns', 'Musical', 'USA', 2016, 'Rob Marshall', 'David Magee', '2018/12/25');

SELECT * FROM peliculas;

       