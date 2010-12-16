/*
    Copyright (c) 2010, Sam Charrington (@samcharrington), http://geekfactor.charrington.com
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
        * Redistributions of source code must retain the above copyright
          notice, this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
          notice, this list of conditions and the following disclaimer in the
          documentation and/or other materials provided with the distribution.
        * Neither the name of the author nor the names of other contributors 
          may be used to endorse or promote products derived from this software 
          without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
    DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
    ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/*
 * Uploadify supports several events that are fired at various stages of the 
 * file upload process. In this example, we configure Uploadify to call this 
 * function when the OnComplete event fires upon completion of each upload.
 * (The actual configuration is done in the upload_example view.)
 * 
 * This file is included using a <script> tag on our upload page.
 *
 * The 
 */
 
var uploadifyOnComplete = function(e, id, fobj, r, d) {
    /*
     * See the uploadify docs for more information on the
     * arguments passed to the onComplete function:
     * http://www.uploadify.com/documentation/events/oncomplete-2/
     *
     */

    $.post(
        /* 
         *  Our call to jQuery.post() includes three params:
         *   - A string containing the URL to which the request is sent,
         *    which we grab from a hidden form field
         *   - A map or string containing data that is sent to the server
         *     with the request
         *   - A callback function that is executed if the request succeeds
         *
         */
        $('#next').val(),
        {'s3_response': r,
         'file_obj': fobj,
         'upload_data': d},
        function(data) {
            window.location.href = data;
        }
    );
}

