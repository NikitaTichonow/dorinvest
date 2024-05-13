import uuid
from django.shortcuts import redirect, render
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import FeedbackCreateForm, EndedShowForm, AnimalsForm
from .models import Show, EndedShow, Animals, Photoreport


class ShowDetail(FormMixin, DetailView):
    """Текущая выставка"""
    model = Show
    template_name = 'show.html'
    context_object_name = 'show'
    form_class = FeedbackCreateForm
    queryset = Show.objects.all()

    def get_context_data(self, **kwargs):
        """Переопределяет метод get_context_data для добавления дополнительных данных в контекст шаблона.
    Включает в себя животных, баннеры, истории, местоположения, социальные ссылки и партнеров, связанных с
    выставкой, а также форму для создания обратной связи."""
        context = super().get_context_data(**kwargs)
        show = self.get_object()

        animals = show.animals.all()
        banners = show.banners.all()
        stores = show.stores.all()
        locations = show.locations.all()
        social_links = show.social_links.all()
        partners = show.partners.all()

        context['animals'] = animals
        context['banners'] = banners
        context['stores'] = stores
        context['locations'] = locations
        context['social_links'] = social_links
        context['partners'] = partners
        context['feedback_form'] = FeedbackCreateForm()
        print(banners)
        return context

    def post(self, request, *args, **kwargs):
        """Обрабатывает POST-запрос, проверяет валидность формы и вызывает метод form_valid или
    form_invalid в зависимости от результата."""
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """Обрабатывает валидную форму, сохраняет данные формы в базу данных, генерирует уникальный slug для
    обратной связи,если он не был предоставлен, и перенаправляет пользователя на страницу детализации выставки."""
        form.instance.user = self.request.user
        form.instance.show = self.get_object()
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.name) + '-' + uuid.uuid4().hex
        form.save()

        return redirect('show', slug=self.get_object().slug)



class EndedShowList(ListView):
    """Список предыдущих выставок"""
    model = EndedShow
    ordering = '-id'
    template_name = 'ended_show_list.html'
    context_object_name = 'endedshow'
    form_class = EndedShowForm

    def get_context_data(self, **kwargs):
        """Переопределяет метод get_context_data для добавления дополнительных данных в контекст шаблона.
    Включает в себя форму для создания новой записи о прошедшей выставке"""
        context = super().get_context_data(**kwargs)
        context['form'] = EndedShowForm
        context['photoreports'] = Photoreport.objects.all()
        return context


class AnimalList(ListView):
    """Список животных"""
    model = Animals
    ordering = 'id'
    template_name = 'animals_list.html'
    context_object_name = 'animals'
    form_class = AnimalsForm

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['form'] = AnimalsForm
        return context


class AnimalDetail(DetailView):
    """Карточка животного"""
    model = Animals
    ordering = 'id'
    template_name = 'animals.html'
    context_object_name = 'animal'
    form_class = AnimalsForm

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['form'] = AnimalsForm
        context['animal_images'] = self.object.animal.all()
        return context