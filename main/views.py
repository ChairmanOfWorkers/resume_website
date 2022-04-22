from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from .models import(
	Skill,
	UserProfile,
	ContactProfile,
	Testimonial,
	Media,
	Portfolio,
	Blog,
	Certificate
)

from .forms import ContactForm

class IndexViews(generic.TemplateView):
	template_name = 'main/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolios = Portfolio.objects.filter(is_active=True)

		context['testimonials'] = testimonials
		context['certificates'] = certificates
		context['blogs'] = blogs
		context['portfolios'] = portfolios
		return context

class ContactViews(generic.FormView):
	template_name = 'main/contact.html'
	form_class = ContactForm
	success_url = '/'

	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)

class PortfolioViews(generic.ListView):
	model = Portfolio
	template_name = 'main/portfolio.html'
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class PortfolioDetailViews(generic.DetailView):
	model = Portfolio
	template_name = 'main/portfolio-detail.html'

class BlogViews(generic.ListView):
	model = Blog
	template_name = 'main/blog.html'
	paginate_by = 10
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class BlogDetailViews(generic.DetailView):
	model = Blog
	template_name = 'main/blog-detail.html'