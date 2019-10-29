# blog
Personal blog for https://blog.shaunfinglas.co.uk

New machine setup

    sudo apt-get update
    sudo apt install python-pip
    sudo apt install pelican

Clone repos

    $ git clone https://github.com/Finglas/blog.git
    $ git clone https://github.com/Finglas/finglas.github.io.git

Write content in markup

    $/home cd blog
    pelican content/ -o ../finglas.github.io

Commit and push to `finglas.github.io`.
