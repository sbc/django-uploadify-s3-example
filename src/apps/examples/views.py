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
View illustrating how to render a file upload form using django-uploadify-s3

"""

from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime
from urllib import unquote_plus
import re
from models import Example, ExampleForm
from uploadify_s3 import uploadify_s3

def upload_example(request, object_id):
    """
    This view renders the Uploadify file upload form.
    
    """
    
    example = get_object_or_404(Example, id=object_id)

    #
    # Create an options dictionary and pass it to uploadify_s3.UploadifyS3()
    # to set Uploadify options. See http://www.uploadify.com/documentation/.
    #
    # These options override any set in your project settings file.
    #
    # Here we specify the name of our JavaScript onComplete event handler.
    # See /media/js/uploadify_event_handlers.js.
    #

    options={
        'onComplete'    : 'uploadifyOnComplete',
    }

    #
    # The key_pattern set here will be sent to S3 as the 'key' form field
    # below. You can use it to set the key (e.g. name) of your uploaded objects. 
    #
    
    key_pattern = 'example-%s/${filename}' % object_id
    
    #
    # Create a post_data dictionary and pass it to uploadify_s3.UploadifyS3()
    # to set any desired S3 POST variables.
    #
    # See:
    # http://docs.amazonwebservices.com/AmazonS3/latest/index.html?UsingHTTPPOST.html
    #
    # 'key' is the only required field that is not automatically set by DUS3. It
    # may be set here in the view or by setting the AWS_DEFAULT_KEY_PATTERN in
    # your project settings.
    #
    # Note: Some reports indicate that Flash/Uploadify has problems with HTTP 
    # responses with an empty body. To avoid this, set a success_action_status
    # of 201, which forces S3 to return an XML document.
    #
    
    post_data={
        'key': key_pattern,
        'success_action_status': "201",
        }

    #
    # S3 uses conditions to validate the upload data. DUS3 automatically constructs
    # and includes conditions for most of the elements that will be sent to S3, but you 
    # need to pass in conditions for:
    #   - 'key', whose value changes at upload time. Note that the condition's value
    #     must correspond to the key pattern set above.
    #   - any extra elements set at upload time
    #
    # See the DUS3 README for more information on the conditions mapping:
    #   https://github.com/sbc/django-uploadify-s3
    #

    conditions={
        'key': {'op': 'starts-with', 'value': 'example-%s/' % object_id},
        }

    #
    # Initialize UploadifyS3 and call get_options_json() to get the Uploadify
    # JSON payload. 
    #
    
    uploadify_options = uploadify_s3.UploadifyS3(
                            uploadify_options=options,
                            post_data=post_data, 
                            conditions=conditions
                            ).get_options_json()

    #
    # Pass the Uploadify JSON payload to the file_upload template as extra_context.
    # 
    
    return direct_to_template(request, 'examples/example_file_upload.html', extra_context={ 'example': example, 'uploadify_options': uploadify_options })


def upload_example_done(request, object_id):
    """
    This view is a callback that receives POST data
    from uploadify when the download is complete.
    See also /media/js/uploadify_event_handlers.js.
    
    """

    example = get_object_or_404(Example, id=object_id)

    #
    # Grab the post data sent by our OnComplete handler and parse it. Set the fields 
    # on our example object as appropriate and save.
    #

    if request.method == 'POST':
        post_response = request.POST['s3_response']
        location_rexp = '<Location>(.*)</Location>'
        example.file_url = unquote_plus(re.search(location_rexp, post_response).group(1))
        example.file_name = request.POST['file_obj[name]']
        example.file_size = request.POST['file_obj[size]']
        example.file_upload_speed = request.POST['upload_data[speed]']
        example.file_uploaded = datetime.now()
        example.save()
        
        print example.file_url
        print example.file_name
        print example.file_uploaded
        
    return HttpResponse((reverse('examples_example_detail', args=[example.id])))

