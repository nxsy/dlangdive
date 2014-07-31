chapter_header: "Hello World"
title: "Simplest D program"
date: 2014-06-27 05:11:33
published: 2014-06-27 05:11:33
chapter: 1
section: 1
subtitle: 
description:
created: !!timestamp 2014-06-27 05:11:33
type: page

## void main ##

The simplest D program is this:

    :::d
    void main() {
    }

Using `rdmd`, a companion to the compiler in the `Digital Mars D Compiler`, you
can build and execute this program in one command (assuming you named the file
`simplest.d`):

    :::sh
    $ rdmd simplest.d

This does nothing - at least not visibly.  But it does nothing successfully
(much like the `true` command), returning exit code 0:

    :::sh
    $ echo $?
    0

## int main ##

If you're familiar with Unix process execution, you may be wondering how you
specify the exit code.  You can just use `int main` instead of `void main`,
like so:

    :::d
    int main() {
        return 1;
    }


