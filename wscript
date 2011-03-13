from os import popen
import Utils

srcdir = "."
blddir = "build"
VERSION = "0.0.1"

def set_options(opt):
  opt.tool_options("compiler_cc")
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cc")
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  conf.sub_config('deps/libhashkit')
  conf.sub_config('deps/libmemcached')

def build(bld):
  bld.add_subdirs('deps/libhashkit')
  bld.add_subdirs('deps/libmemcached')
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.includes = 'deps'
  obj.target = "memcache-impl"
  obj.source = "src/binding.cc"
  obj.add_objects = 'memcached hashkit'
  obj.cxxflags = ["-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall"]

def lint(lnt):
  Utils.exec_command('cpplint.py ./src/*.cc')
