#!/bin/sh

SOURCE_DIR=$1

if [ ! -d libmemcached ]; then
    mkdir libmemcached
fi
if [ ! -d libhashkit ]; then
    mkdir libhashkit
fi
if [ ! -d libmemcached/memcached ]; then
    mkdir libmemcached/memcached
fi

cp -f $SOURCE_DIR/libhashkit/*.[ch] libhashkit/
cp -f $SOURCE_DIR/libmemcached/*.[ch] libmemcached/
cp -f $SOURCE_DIR/libmemcached/memcached/*.h libmemcached/memcached
rm libmemcached/sasl.c
