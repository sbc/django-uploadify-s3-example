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

"""
Defines an example model to which we want to associate file upload data. 

"""

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.exceptions import PermissionDenied

class Example(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    created = models.DateTimeField('date created', auto_now_add=True, blank=False)
    modified = models.DateTimeField('date modified', auto_now=True, blank=False)
    
    # These file fields are somewhat arbitrary but you'll want to at least capture the 
    # name or url of your upload. These fields are set by the upload_example_done view.
    
    file_url = models.CharField(max_length=2000, blank=True)
    file_name = models.CharField(max_length=255, blank=True)
    file_uploaded = models.DateTimeField('date file uploaded', null=True, blank=True)
    file_upload_speed = models.FloatField(null=True, blank=True)
    file_size = models.IntegerField(null=True, blank=True)

    # You can define methods based on the file fields. This one is helpful.
    
    def has_file(self):
        return len(self.file_url) > 0

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('examples_example_detail', [self.id])

class ExampleForm(ModelForm):
    class Meta:
        model = Example
        
        # You probably want to exclude your file upload fields from forms
        
        exclude = ('owner', 'file_url', 'file_name', 'file_uploaded', 'file_created', 'file_modified', 'file_upload_speed', 'file_size')