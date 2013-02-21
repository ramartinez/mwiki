# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from wiki.models import Page
from django.http import HttpResponseRedirect

def view_page(request, page_name):
		try:
			page = Page.objects.get(pk=page_name)
			content = page.content
		except Page.DoesNotExist:
			return render_to_response('wiki/create.html', {
				'page_name' : page_name,
			})

		return render_to_response('wiki/index.html', {
			'page_name' : page_name,
			'content' : content,
		})

def edit_page(request, page_name):
		try:
			page = Page.objects.get(pk=page_name)
			content = page.content
		except Page.DoesNotExist:
			content = ""
		c = {
			'page_name' : page_name,
			'content' : content,
		}
		c.update(csrf(request))
		return render_to_response('wiki/edit.html', c)

def save_page(request, page_name):
		content = request.POST['content']
		try:
			page = Page.objects.get(pk=page_name)
			page.content = content
		except:
			page = Page(
				name = page_name,
				content = content
			)
		page.save()
		return HttpResponseRedirect('/wiki/' + page_name + '/')
