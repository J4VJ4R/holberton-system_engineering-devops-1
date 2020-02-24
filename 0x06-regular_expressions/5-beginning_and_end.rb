#!/usr/bin/env ruby
name = ARGV[0]
my_name = name.scan(/h.+n/).join
puts "#{my_name}"
