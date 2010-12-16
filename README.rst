========================================================================
Django Uploadify-S3 (DUS3) Example
========================================================================

*Copyright (c) 2010, Sam Charrington (@samcharrington), http://geekfactor.charrington.com*

Overview
--------

This is an example application that illustrates the use of the DUS3 
application.

See https://github.com/sbc/django-uploadify-s3.

Installation
------------

The recommended installation procedure uses virtualenv and buildout.

#. If you do not already have virtualenv you will need to install it using ``easy_install virtualenv``
#. Create a new virtualenv 'foo' with ``virtualenv foo``
#. Activate the virtualenv: ``cd foo; source bin/activate``
#. Clone the git repo: ``git clone git://github.com/sbc/django-uploadify-s3-example.git example``
#. Bootstrap the buildout environment: ``cd example; python bootstrap.py``
#. Run the build: ``bin/buildout``. This will download and install (to the virtualenv) all dependencies including Django, DUS3 and Uploadify
#. Sync the db: ``bin/django syncdb``
#. Edit ``src/settings/common.py``, and add your AWS information
#. Create a ``crossdomain.xml`` file and upload it to the root of your S3 bucket
#. Run the dev server: ``bin/django runserver``

Usage
-----

With installation complete and the dev server running, you may now open your web browswer and go to ``http://127.0.0.1:8000``. From here you can play with the demo app. For example, you can create an Example object and upload a file. 

Once you get a feel for what the demo app is doing, you can read the source code and integrate it into your own projects.

Troubleshooting
---------------

1. In order for the browser to communicate to your S3 bucket, you must
   upload a ``crossdomain.xml`` file to the root of your bucket. This example
   allows any browsers to communicate with your S3 bucket::
   
       <?xml version="1.0"?>
       <!DOCTYPE cross-domain-policy SYSTEM "http://www.macromedia.com/xml/dtds/cross-domain-policy.dtd">
       <cross-domain-policy>
         <allow-access-from domain="*" secure="false" />
       </cross-domain-policy>
   
2. Because Uploadify uses a Adobe Flash component to perform the actual
   upload, browser-based HTTP debugging tools like Firebug cannot see 
   the traffic between the browser and S3. You can however use a network
   sniffer like Wireshark (http://www.wireshark.org) to view the traffic.