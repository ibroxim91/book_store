from modeltranslation.translator import translator, TranslationOptions
from .models import *

class CategoryTranslator(TranslationOptions):
    fields = ("name" ,)

class BooksTranslator(TranslationOptions):
    fields = ("name" ,"text")

translator.register(Book , BooksTranslator)
translator.register(Category , CategoryTranslator)
