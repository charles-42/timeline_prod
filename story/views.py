from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Events



# needed to print events distributed in period with périod order
PERIOD = (
(1, 'Préhistoire'), (2, 'Première antiquité'), (3, 'VIème siècle av-jc'),
(4, 'Vème siècle av-jc'),(5, 'IVème siècle av-jc'),(6, 'IIIème siècle av-jc'),
(7, 'IIème siècle av-jc'),(8, 'Ier siècle av-jc'), (9, 'Ier siècle'),
(10, 'IIème siècle'),(11, 'IIIème siècle'),(12, 'IVème siècle'),
(13, 'Vème siècle'),(14, 'VIème siècle'), (15, 'VIIème siècle'),
(16, 'VIIIème siècle'),(17, 'IXème siècle'),(18,'Xème siècle'),
(19, 'XIème siècle'),(20, 'XIIème siècle'),(21, 'XIIIème siècle'),
(22, 'XIVème siècle'),(23, 'XVème siècle'), (24, 'XVIème siècle'),
(25, 'XVIIème siècle'),(26, 'XVIIIème siècle'),(27,'XIXème siècle'),
(28, 'XXème siècle'),(29, 'XXIème siècle'),
)
period_dict = dict(PERIOD)


def index(request):
    pers = Events.objects.values_list('period', flat=True).distinct().order_by('period')
    events = Events.objects.order_by('date').all()
    # create a list of the period labels in the right order (here all the period are used)
    long_per = [period_dict[p] for p in pers]
    context = {
        'events': events,
        'long_per':long_per,
        'page_name':'Globale',
        'page_infos':'Histoire du monde et des hommes depuis leur création'

        }
    template = loader.get_template('story/index.html')

    return HttpResponse(template.render(context, request=request))


pages = {
    'Philosophique':("PH",'Ce qui compte en philosophie depuis que les hommes ont commencé à penser'),
    'Scientifique':( "SC",'Histoire des progrès réalisés par l\'humanité'),
    'Artistique':("LI",'Une brève histoire de l\'art'),
    'Religieuse':("RE",'Histoire des choses éternelles')
}

def frise(request, p_name):
    page_infos=pages[p_name]
    # create a list of the distinct period integer used in the page
    pers = Events.objects.filter(category=page_infos[0]).values_list('period', flat=True).distinct().order_by('period')
    events = Events.objects.filter(category=page_infos[0]).order_by('date').all()
    # create a list of the period labels in the right order (for some page some periods are not used)
    long_per = [period_dict[p] for p in pers]
    context = {
        'events': events,
        'long_per':long_per,
        'page_name':p_name,
        'page_infos':page_infos[1]
    }
    template = loader.get_template('story/index.html')

    return HttpResponse(template.render(context, request=request))
