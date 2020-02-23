#!/usr/bin/env ruby
name = ARGV[0]
my_name = name.scan(/hbt{2,5}n/).join
puts "#{my_name}"
