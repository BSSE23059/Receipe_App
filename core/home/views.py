from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

peoples = [
    {'Name' : 'Muhammad Hazim', 'Age' : 21},
    {'Name' : 'Aiman', 'Age' : 20},
    {'Name' : 'Farhan', 'Age' : 21},
    {'Name' : 'Irfan', 'Age' : 17},
    {'Name' : 'Aisyah', 'Age' : 19},
]

text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit corrupti odit, porro dolor odio, suscipit cupiditate architecto maiores autem doloribus, ab ad voluptatum repudiandae nam pariatur? Mollitia rem alias accusamus distinctio, quibusdam doloribus incidunt saepe tenetur quae animi similique ipsum quod laborum voluptate. Autem laborum illum sint recusandae ea iure, officiis alias esse dolore inventore nostrum! Iure doloremque quia molestiae natus, similique aliquid ipsa voluptatem totam qui officia a adipisci debitis officiis veritatis deserunt numquam, ducimus vel in. Modi voluptatem sunt iusto, quidem sequi sapiente reiciendis magni saepe dolor ullam voluptatibus, tempore veritatis optio illo temporibus dicta molestiae. Aliquam, aperiam!"
vegetables = ["Pumpkin", "Tomato", "Potato"]

for people in peoples:
    print(people)

def home(request):
    return render(request,"home/index.html", context={"page": "Django Tutorial 2025","peoples": peoples, "text": text, "vegetables": vegetables})

def about(request):
    context = {'page' : 'About'}
    return render(request,"home/about.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request,"home/contact.html", context)


def success_page(request):
    return HttpResponse("<h1>This is a success page.</h1>")