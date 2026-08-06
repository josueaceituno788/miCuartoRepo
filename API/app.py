import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

@app.get("/superheroesMarvel")
def get_superheroes_marvel():
    rows = ["Spider-Man", "Iron Man", "Thor", "Hulk", "Black Widow", "Doctor Strange", "Black Panther", "Captain America"]
    return rows

@app.get("/LOTRWarriors")
def get_lotr_warriors():
    rows = ["Frodo", "Sam", "Gandalf", "Aragorn", "Legolas", "Gimli", "Boromir", "Gollum", "El anillo"]
    return rows

@app.get("/starwarsWarriors")
def get_starwars_warriors():
    rows = ['Obiwan', 'el pelón del sable morado', 'Darth Vader', 'El de la colita de caballo', 'Yoda']
    return rows

@app.get("/warriorsGOT")
def get_warriors_got():
    rows = ["Jon Snow", "Daenerys Targaryen", "Arya Stark", "Tyrion Lannister", "Cersei Lannister", "Jaime Lannister", "Bran Stark", "Sansa Stark"]
    return rows


@app.get("/juegos")
def get_games():
    rows = ["SUPER MARIO", "Super smash", "NFSMW", "Halo", "Zuma Beta", "Sonic dash", "Dk adventure", "WWF"]
    return rows


@app.get("/cursos")
def get_cursos():
    rows = ["Docker", "Js Script", "C#", "Git Hub"]
    return rows


@app.get("/deportes")
def get_deportes():
    rows = ["Futbol", "Basket", "Bassball", "Tenis"]
    return rows


@app.get("/musica")
def get_deportes():
    rows = ["electro", "reggaeton", "cumba", "rap"]
    return rows


@app.get("/programas")
def get_programas():
    rows = ["WWE", "TNA", "WCW", "AEW"]
    return rows


@app.get("/comida")
def get_comida():
    rows = ["macarrones", "paella", "pizza", "pupusas"]
    return rows


print("Agregue esto desde git hub")


print("Cambios desde locales")


print("otro cambio mas desde git hub")


print ("otro cambio mas local XD")
