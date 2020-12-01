from story.models import Events
import wikipedia

for event in Events.objects.all():
    try:
        wiki_page=wikipedia.page(event.name)
    except:
        event.wiki="not_found"
    else :
        event.wiki=wiki_page.url
