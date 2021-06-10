from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
	tiempo= strftime("%d del %m de %Y a las %H:%M %p", gmtime())

	context = {
		"timedisplay": tiempo
	}
	return render(request,'index.html', context)
