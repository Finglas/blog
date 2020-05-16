# blog
Personal blog for https://blog.shaunfinglas.co.uk

New machine setup

    sudo apt-get update
    sudo apt install python-pip
    sudo apt install pelican

Clone repos

    $ mkdir blog && cd blog
    $ git clone https://github.com/Finglas/blog.git content
    $ git clone https://github.com/Finglas/finglas.github.io.git

Write content in markup

    $/home cd blog/content
    pelican content/ -o ../finglas.github.io

Commit and push to `finglas.github.io`.
