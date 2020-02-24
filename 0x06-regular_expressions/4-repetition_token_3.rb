#!/usr/bin/env ruby
name = ARGV[0]
my_name = name.scan(/hbt{0,}n/).join
puts "#{my_name}"
