This project implements a RESTful API for a message board using Django
and DjangoRestFramework (DRF). The message board contains 3 resources:
Users, Threads, and Messages. Users are modified only by the site admin,
and are read-only to the outside world. Threads represent a collection
of messages. In addition to a list of messages, they have an owner and a
topic. Messages represent posts to the message board. They are organized
by threads. Each message contains a thread reference, an owner, and some
body text representing the post.

Documentation
=============

Detailed Documentation along with access and modification capabilities
can be found here: <http://minds57.pythonanywhere.com/>

Authentication
==============

In order to make changes to threads and messages a user must log in.
Once authenticated, a user can only modify the threads and messages that
he has created. No user can modify threads or messages from another
user. A user can, however, add new messages to a thread owned by another
user. For evaluation purposes please use the following credentials.

Username: admin

Password: password123

Endpoints
=========

                         **GET**             **POST**          **PUT**               **DELETE**
  ---------------------- ------------------- ----------------- --------------------- ---------------------
  /users/                Show all users      N/A               N/A                   N/A
  /users/&lt;id&gt;      Show &lt;id&gt;     N/A               N/A                   N/A
  /threads/              Show all threads    Add new thread    Update all threads    Delete all threads
  /threads/&lt;id&gt;    Show &lt;id&gt;     N/A               Update &lt;id&gt;     Delete &lt;id&gt;
  /messages/             Show all messages   Add new message   Update all messages   Delete all messages
  /messages/&lt;id&gt;   Show &lt;id&gt;     N/A               Update &lt;id&gt;     Delete &lt;id&gt;

Code
====

All code for the project has been uploaded to github.
<https://github.com/mhinds/message_board_rest_api>

Unit Tests
==========

<https://github.com/mhinds/message_board_rest_api/blob/master/board/tests.py>

Functionality is included to test each endpoint. Users are only read.
Threads and messages are read, created, modified, or deleted.
