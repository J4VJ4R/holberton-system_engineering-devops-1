#!/usr/bin/env ruby
name = ARGV[0]
my_name = name.scan(/hbt{1,}n/).join
puts "#{my_name}"
