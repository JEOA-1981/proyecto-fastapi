from curses import nl
import imp
import spacy
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(tags= ['enunciado'])
nlp = spacy.load('es_core_news_lg')


class Entrada(BaseModel):
    enunciado: str


@app.post('/comparacion_textos')
def similitud_textual(primer_enunciado: Entrada, segundo_enunciado: Entrada):
    primero = nlp(primer_enunciado.enunciado)
    segundo = nlp(segundo_enunciado.enunciado)
    similitud = primero.similarity(segundo)
    return 'La semejanza entre los enunciados es de {:.0%}'.format(similitud)


