# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import os
from django.shortcuts import render_to_response
from forms import ContactForm
from django import forms
from models import CompareInstance
from bs4 import BeautifulSoup
import urllib2


image_url = "http://dduke.inside-box.net:86/www/img_diff/" 


def base(request):
    return render_to_response('base.html') 

def contact(request):

    envs = parse_index(image_url)
    env_names = [x[1] for x in envs]
    groups = [parse_index(env[0]) for env in envs]
    groups = [item for sublist in groups for item in sublist]
    group_names = [x[1] for x in groups]
    versions = [parse_index(group[0]) for group in groups]
    versions = [item for sublist in versions for item in sublist]
    version_names = [x[1] for x in versions]

    #form = ContactForm(env_names, group_names, version_names)
    form = ContactForm(env=[(i,i) for i in env_names], group=[(i,i) for i in group_names], version=[(i,i) for i in version_names])
    return render_to_response('img_viewer/contact.html', {'form': form}, context_instance=RequestContext(request))


def parse_index(url):

    f = urllib2.urlopen(url)
    s = f.read()
    soup = BeautifulSoup(s)
    tds = soup.findAll('td')

    tds_with_a = [i for i in tds if i.findAll('a')]
    return [(''.join([url, i.text]), i.text) for i in tds_with_a if i.text != u'Parent Directory']

    

def list_dir_full(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def process_images(expected_dir_url, new_dir_url):
    expected_files_urls = [x[0] for x in parse_index(expected_dir_url)]
    new_files_urls = [x[0] for x in parse_index(new_dir_url)]
    comparisons = []
    for f1, f2 in zip(expected_files_urls, new_files_urls):
        comparisons.append(process_image(f1, f2))
    return comparisons
        


def process_image(image_1, image_2):
    print image_1
    print image_2
    return CompareInstance(expected_img_url=image_1, new_img_url=image_2)
    

def imgview(request):
    post = request.POST.copy()
    env = post['environment']
    group = post['group']
    version = post['version']

    latest_version = 'latest/'

    base_url = ''.join([image_url, env, group, version])
    new_url = ''.join([image_url, env, group, latest_version])

    print base_url
    print new_url



    comparisons = process_images(base_url, new_url)
    return render_to_response('img_viewer/img_compare.html', {'comparisons' : comparisons})
