"""
The register.filter decorator is used to register the get_dict_val function as a custom filter.
"""
from django.template.defaulttags import register

@register.filter # This filter can be used in Django templates to retrieve a value from a dictionary using a specified key.
def get_dict_val(dictionary, key, key_as_str=True):
    if not isinstance(dictionary, dict):
        return None
    if key_as_str:
        key=f"{key}"
    return dictionary.get(key)
