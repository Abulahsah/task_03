from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list" : [
  { "restaurant_name":"Applepez" , "food_type":"amrican" },
  { "restaurant_name":"Kentaki" , "food_type":"fride chicken" },
  { "restaurant_name":"Hardez" , "food_type":"bergar" },

    ] ,


    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object" : { "restaurant_name":"fridays" , "food_type":"italian" },

    }
    return render(request, 'detail.html', context)
