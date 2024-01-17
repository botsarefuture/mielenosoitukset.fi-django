from modeltranslation.translator import translator, TranslationOptions
from .models import Organization

class OrganizationTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'location', 'activism_focus')
    
translator.register(Organization, OrganizationTranslationOptions)