# Copyright (c) 2010, Sam Charrington (@samcharrington), http://geekfactor.charrington.com
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of other contributors 
#       may be used to endorse or promote products derived from this software 
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from django.conf.urls.defaults import *
from models import Example, ExampleForm

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', { 'url': '/examples' }),
    
    # 
    # The upload_example view renders the Uploadify file upload form.
    #
    
    url(r'^examples/(?P<object_id>[\d]*)/upload$',
        'examples.views.upload_example',
        name='examples_example_upload'),
    
    #
    # The upload_example_done view is a callback that receives POST data
    # from uploadify when the download is complete.
    # See also /media/js/uploadify_event_handlers.js.
    #
    
    url(r'^examples/(?P<object_id>[\d]*)/upload/done$',
        'examples.views.upload_example_done',
        name='examples_example_upload_done'),

    # The rest are boring generic views
    
    url(r'^examples/$',
        'django.views.generic.list_detail.object_list',
        { 'queryset': Example.objects.all() },
        name='examples_example_list'),
    
    url(r'^examples/new$', 
        'django.views.generic.create_update.create_object',
        { 'model': Example },
        name='examples_example_new'),
    
    url(r'^examples/(?P<object_id>[\d]*)$',
        'django.views.generic.list_detail.object_detail',
        { 'queryset': Example.objects.all() },
        name='examples_example_detail'),
    
     url(r'^examples/(?P<object_id>[\d]*)/edit$',
         'django.views.generic.create_update.update_object',
         { 'form_class': ExampleForm },
         name='examples_example_edit'),
     
     url(r'examples/(?P<object_id>[\d]*)/delete$',
        'django.views.generic.create_update.delete_object',
        { 'model': Example, 'post_delete_redirect': '/examples' },
        name='examples_example_delete'),
)