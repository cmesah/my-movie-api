from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()
app.title = "Mi aplicacion con FastApi"
app.version = "0.0.1"

class Movie(BaseModel):
    id : Optional[int] = None
    title : str = Field(default= 'Mi pelicula',min_length= 5,max_length=15)
    overview : str = Field(default= 'Descripción pelicula',min_length= 15,max_length=50)
    year : int = Field(default= 2022,le= 2023)
    rating: float
    category:str 
    

movies =[
    {
       "id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción" 
    },
    {
       "id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción" 
    }
]

# @app.get('/', tags=['home'])
# def message():
#     return HTMLResponse('<h1>Hello Word</h1>')


@app.get('/movies',tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}',tags=['movies'])
def get_movie(id: int):
 
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/',tags=['movies'])
def get_movies_by_category(category:str, year: int):
    for item in movies:
        if item ["category"] == category or item ["year"] == year :
            return item
    return []

@app.post('/movies', tags=['movies'])
def create_movie(movie:Movie):
    movies.append(movie)
    return movies
    

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id:int, movie:Movie):
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            
            return movies 
        
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id:int):
    for num in movies:
        if num['id'] == id:
            movies.remove(num)
            
            return movies
