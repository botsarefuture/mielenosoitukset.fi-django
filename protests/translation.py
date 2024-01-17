from modeltranslation.translator import translator, TranslationOptions
from .models import Protest, Role

class ProtestTranslationOptions(TranslationOptions):
    fields = ('title', 'location', 'details')  # Add the fields you want to translate

translator.register(Protest, ProtestTranslationOptions)

class RoleTranslationOptions(TranslationOptions):
    fields = ('name', 'description')  # Add the fields you want to translate

translator.register(Role, RoleTranslationOptions)


