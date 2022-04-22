from django.contrib import admin
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

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'score')
	list_display_links = ('id', 'name')
	save_on_top = True

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'title')
	list_display_links = ('id', 'user')
	save_on_top = True

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'timestamp')
	list_display_links = ('id', 'name')
	save_on_top = True

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'role', 'is_active')
	list_display_links = ('id', 'name')
	save_on_top = True

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	save_on_top = True

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'date', 'is_active')
	list_display_links = ('id', 'name')
	save_on_top = True
	readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'author', 'is_active')
	list_display_links = ('id', 'name')
	save_on_top = True
	readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'date', 'is_active')
	list_display_links = ('id', 'name')
	save_on_top = True