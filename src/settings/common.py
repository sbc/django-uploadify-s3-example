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

import os
import logging
import sys
from path import path


MEDIA_URL = '/media/'

# *********************************************
#
# The Uploadify stuff is up top
#
# *********************************************

#
# This is a dictionary of default Uploadify options. They are called defaults 
# because they can be overriden in your views.
#
# See the Uploadify docs for additional details:
#    http://www.uploadify.com/documentation/
#
# Notes:
#    - Setting 'fileDataName' to 'file' is necessary for S3 uploads to work
#    - Multi file upload hasn't been tested and the onComplete event handler
#      used in this example prevents it anyway
#

UPLOADIFY_DEFAULT_OPTIONS = {
    'cancelImg'     : MEDIA_URL + "uploadify/cancel.png",
    'fileDataName'  : 'file',
    'method'        : 'post',    
    'scriptAccess'  : 'sameDomain',
    'auto'          : False,
    'multi'         : False,
    'buttonText'    : 'Select File',
    'folder'        : '',
}

#
# Include your S3 details here
#

AWS_BUCKET_NAME = 'my.bucket.name'   # Bucket name
AWS_BUCKET_URL = 'http://%s.s3.amazonaws.com' % ( AWS_BUCKET_NAME )   # Bucket URL. DUS3 uses virtual hosted buckets

AWS_ACCESS_KEY_ID = 'MY_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'MY_SECRET_ACCESS_KEY'

AWS_DEFAULT_ACL = 'private'   # Any canned S3 ACL
AWS_DEFAULT_KEY_PATTERN = '${filename}'
AWS_S3_SECURE_URLS = True   # Use https?

AWS_DEFAULT_FORM_LIFETIME = 36000   # Form expiration time, in seconds


# *********************************************
#
# The rest is standard Django fare
#
# *********************************************

PROJECT_ROOT = path(__file__).abspath().dirname().dirname()
SITE_ROOT = PROJECT_ROOT.dirname()

sys.path.append(SITE_ROOT)
sys.path.append(PROJECT_ROOT / 'apps')
sys.path.append(PROJECT_ROOT / 'libs')

ADMINS = (
    ('Admin Name', 'admin_email@example.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Don't share this with anybody.
SECRET_KEY = '***CHANGE ME***'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',    
)

ROOT_URLCONF = 'src.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sites',    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'debug_toolbar',
    'uploadify_s3',
    'examples'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

LOG_DATE_FORMAT = '%d %b %Y %H:%M:%S'
LOG_FORMATTER = logging.Formatter(
    u'%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
    datefmt=LOG_DATE_FORMAT)

CONSOLE_HANDLER = logging.StreamHandler() # defaults to stderr
CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)
CONSOLE_HANDLER.setLevel(logging.DEBUG)


