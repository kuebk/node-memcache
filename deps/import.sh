#!/bin/sh

SOURCE_DIR=$1

mkdir libmemcached
mkdir libhashkit
mkdir libmemcached/memcached

cp $SOURCE_DIR/libhashkit/*.[ch] libhashkit/
cp $SOURCE_DIR/libmemcached/*.[ch] libmemcached/
cp $SOURCE_DIR/libmemcached/memcached/*.h libmemcached/memcached
