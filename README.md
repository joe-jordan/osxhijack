oxshijack
=========

*tiny python utility to allow trivial control of existing Terminal.app windows from ssh.*

**OS X ONLY**

I have a big beefy iMac at work, and a little laptop at home. I often SSH into the real machine to see how
long processes are holding up, and so on. Occasionally, it would be nice to be able to run a command remotely and have it continue after I log out.

Since `nohup` seems bugged on OS X for this purpose (without a magical collection of filedescriptor redirects,) especially
if you want to do any IO, I used an applescript snippet to take over a local terminal and run a command.

So I don't have to remember the applescript, I hacked together this little wrapper which 'hijacks' existing terminal processes
(sometimes seems to open in a new window, which isn't a bad thing) and runs the command you pass, returning your terminal immidiately.

Additionally, the library has another applescript function to open Terminal.app if it isn't already.

Installation
============

    sudo python setup.py install

Usage
=====

    hijack command -arguments -and -things

