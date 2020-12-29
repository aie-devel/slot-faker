from importlib import import_module

from faker.utils.loading import find_available_providers


META_PROVIDERS_MODULES = [
    'slot_faker.providers',
]

PROVIDERS = find_available_providers(
    [import_module(path) for path in META_PROVIDERS_MODULES])