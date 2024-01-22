from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

# form
from web.forms import ContactForm, EnquiryForm

# Model
from web.models import Client, Faq, Service, Testimonial, Updates

# Create your views here.


def index(request):
    context = {
        "is_index": True,
        "client": Client.objects.all(),
        "testimonials": Testimonial.objects.all(),
        "updates": Updates.objects.filter(is_updates=True)[:3],
    }
    return render(request, "web/index.html", context)


def about(request):
    faq = Faq.objects.all()
    context = {
        "faq": faq,
        "is_about": True,
    }
    return render(request, "web/about.html", context)


def service(request):
    services = Service.objects.filter(is_service=True)

    context = {
        "is_service": True,
        "services": services,
    }
    return render(request, "web/service.html", context)


def updates(request):
    updates = Updates.objects.filter(is_updates=True)

    context = {
        "is_updates": True,
        "updates": updates,
    }
    return render(request, "web/updates.html", context)


def contact(request):
    form = ContactForm
    context = {
        "is_contact": True,
        "form": form,
    }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully Submitted",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return JsonResponse(response_data)
    else:
        # Handle other HTTP methods as needed
        response_data = {
            "status": "false",
            "title": "Method Not Allowed",
            "message": "This endpoint only supports POST requests.",
        }
    return render(request, "web/contact.html", context)


def service_details(request, slug):
    service = get_object_or_404(Service, slug=slug)
    other_services = Service.objects.exclude(slug=slug)
    context = {
        "service": service,
        "request": request,
        "other_services": other_services,
    }

    if request.method == "POST":
        form = EnquiryForm(request.POST)

        if form.is_valid():
            form.instance.service = (
                service  # Link the EnquiryForm to the specific Service
            )
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully Submitted",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }

        return JsonResponse(response_data)

    return render(request, "web/service_details.html", context)


def update_details(request, slug):
    update = get_object_or_404(Updates, slug=slug)
    other_updates = Updates.objects.exclude(slug=slug)
    context = {
        "update": update,
        "request": request,
        "other_updates": other_updates,
    }
    return render(request, "web/update_details.html", context)
