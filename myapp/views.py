from django.shortcuts import render
from . models import Photographer, Content, Gallary, Subscriber

# Create your views here.

def index(request):
	obj = Photographer.objects.get(id=1)
	obj2 = Content.objects.get(id=1)
	obj3 = Gallary.objects.all()
	



	context = {
		'top_carousel_heading'  : obj.top_carousel_heading,
		'top_carousel_paragraph': obj.top_carousel_paragraph,
		'upper_content_heading' : obj.upper_content_heading,
		'profile_heading'       : obj.profile_heading,
		'profile_picture'       : obj.profile_picture,
		'profile_intro'         : obj.profile_intro,
		'lower_content_heading' : obj.lower_content_heading,
		'first_para'            : obj2.first_para,
		'second_para'           : obj2.second_para,
		'third_para'            : obj2.third_para,
		'gallary_image'         : obj3,
		
		
	}


	if request.method=='POST':
		if request.POST.get('full_name') and request.POST.get('email'):
			subscriber = Subscriber()			
			subscriber.email = request.POST.get('email')
			subscriber.full_name = request.POST.get('full_name')
			subscriber.save()

			return render(request, 'index.html', context)
	else:
			return render(request, 'index.html', context)






	



