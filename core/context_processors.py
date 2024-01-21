from django.conf import settings


def google_map_api_key(request):
    """
    The google_map_api_key function is a context processor that adds the Google Maps API key to the template context.
    This allows us to use it in our templates without having to pass it through every view.

    :param request: Get the current request
    :return: A dictionary with a key of google_maps_api_key and the value of settings
    :doc-author: Trelent
    """
    return {"GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY}
