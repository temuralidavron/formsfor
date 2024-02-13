from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from app.forms import AuthorForm, BlogForm, FamilyMemberFormSet
from app.models import Author, Profile


class ProfileList(ListView):
    model = Profile
class ProfileFamilyMemberCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('profile-list')
    template_name = 'profile_form.html'

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberCreate, self).form_valid(form)


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return riderict('author-list')
    form = AuthorForm()

    return render(request,
                  template_name='author.html',
                  context={'form': form}
                  )

def author_list(request):
    authors = Author.objects.all()
    return render(request,
                  template_name='author_list.html',
                  context={'authors': authors}
                  )

    # if request.method == 'POST':
    #     form = AuthorForm(request.POST)
    #     form2 = BlogForm(request.POST)
    #     if form.is_valid() and form2.is_valid():
    #         form.save()
    #         form2.save()
    #         return render(request,
    #                       template_name='author.html',
    #                       context={'form': form}

# def author(request):
#     if request.method == 'POST':
#         print(request.POST)
#         full_name = request.POST.get('full_name', None)
#         email = request.POST.get('email', None)
#
#         list= request.POST.get('blogs')
#         list = list(list)
#         for i in list:
#              print(i.title)
#
#         # form = AuthorForm(request.POST)
#         # form2 = BlogForm(request.POST)
#         # if form.is_valid() and form2.is_valid():
#             # form.save()
#             # form2.save()
#             # return render(request,
#             #               template_name='author.html',
#             #               context={'form': form}
#             #               )
#     # form = AuthorForm()
#     # form2 = BlogForm()
#     return render(request,
#                   template_name='author.html',
#                   # context={'form': form,  'form2': form2}
#                   )